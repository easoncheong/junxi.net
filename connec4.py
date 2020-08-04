description = """ree"""

# discord system imports
import discord
from discord.ext import commands

# python stdlib imports
import random
import asyncio
from io import BytesIO
from datetime import datetime


class connec4(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getInput(self, ctx, nerd):
        try:
            def check(message):
                return message.author == nerd and \
                 message.channel == ctx.channel
            msg = await ctx.bot.wait_for('message', check=check, timeout=90)
            return int(msg.content.split()[0])-1
        except:
            return -1

    async def printBoard(self, ctx, board):
        msg = ""
        for i in board:
            msg+=(' '.join(list(map(self.convert, i))))
            msg+="\n"
        await ctx.send(msg)

    def convert(self, nerd):
        if nerd == 1:
            return ":red_circle:"
        elif nerd == 2:
            return ":blue_circle:"
        else:
            return ":white_medium_square:"

    async def makeMove(self, ctx, nerdToMove, board, nerdToMoveNumber):
        await ctx.send(f"{nerdToMove.mention} enter a column number from 1 to 7")
        q = 0
        while True:
            q+= 1
            if q > 10:
                return None
            column = await self.getInput(ctx, nerdToMove)
            if column >= 0 and column <= 6:
                for i in range(6):
                    if board[i][column] == 0:
                        board[i][column] = nerdToMoveNumber
                        break
            else:
                await ctx.send("Clearly you can't follow instructions nerd, try again")
                continue
            break

        await self.printBoard(ctx, board)
        return board

    def check_winner(self, board, player):
        boardheight = 5
        boardwidth = 6
        #check horizontal spaces
        for y in range(6):
            for x in range(4):
                if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                    return True

        #check vertical spaces
        for x in range(7):
            for y in range(3):
                if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                    return True

        #check / diagonal spaces
        for x in range(4):
            for y in range(3, 6):
                if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                    return True

        #check \ diagonal spaces
        for x in range(4):
            for y in range(3):
                if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                    return True

        return False

    async def playConnec4(self, ctx, nerd1, nerd2):
        board = [[0 for i in range(7)] for j in range(6)]
        move = 0
        while True:
            board = await self.makeMove(ctx, nerd1, board, 1)
            if board == None:
                await ctx.send("Aight that's it neither of yall nerds win i'm out")
                break
            if self.check_winner(board, 1):
                await ctx.send(f"{nerd1.mention} wins bragging rights and absolutely nothing else")
                break
            move += 1
            board = await self.makeMove(ctx, nerd2, board, 2)
            if board == None:
                await ctx.send("Aight that's it neither of yall nerds win i'm out")
                break
            if self.check_winner(board, 2):
                await ctx.send(f"{nerd2.mention} wins bragging rights and absolutely nothing else")
                break
            move += 1
            if move == 42:
                await ctx.send("yall somehow managed to draw this game, epic nerds")
                break

    @commands.command()
    async def connec(self, ctx, nerd: discord.Member):
        #if nerd == ctx.author:
        #    await ctx.send(f"imagine playing connec 4 against yourself lmao, sorry this is illegal, get an alt or smth")
        #    return
        try:
            await ctx.send(f"ok connec 4 time {nerd.mention} respond within 90 seconds and we start")
            def check(message):
                return message.author == nerd and \
                 message.channel == ctx.channel
            await ctx.bot.wait_for('message', check=check, timeout=90)
        except:
            await ctx.send("ok cancelled")
        await self.playConnec4(ctx, ctx.author, nerd)
