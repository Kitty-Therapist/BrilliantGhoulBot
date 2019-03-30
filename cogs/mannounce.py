import asyncio
from subprocess import Popen
import subprocess
import configparser
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import traceback
import discord
from discord.ext import commands 
import os
from discord import utils
from utils import Util, Configuration

class mannounce(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.bot_has_permissions(manage_roles=True)       
    @commands.command()
    async def minecraftannounce(self, ctx: commands.Context, role_name, *, message):
        Minecraft = discord.utils.get(ctx.guild.roles, id=547868949094727683)
        role = Configuration.get_minecraftrole(ctx, role_name)
        channel = Configuration.get_minecraftchannel(ctx, role_name)

        if 547868949094727683 not in [role.id for role in ctx.author.roles]:
            return

        if role is None:
            return await ctx.send("This role might have been deleted, oops!")
        
        if message != None:
            await role.edit(mentionable=True)
            try:
                await channel.send(f"{role.mention}\n{message}")
            except discord.Forbidden:
                await ctx.send("I was not able to send a message. Can you check to make sure I have permission?")
            await role.edit(mentionable=False)
        else: 
            await ctx.send("I am unsure of what you are attempting to do.")

    @commands.command()
    async def minecraftupdate(self, ctx: commands.Context, role_name, message_id:int, *, new_message):
        channel = Configuration.get_minecraftchannel(ctx, role_name)
        Minecraft = discord.utils.get(ctx.guild.roles, id=547868949094727683)

        if 547868949094727683 not in [role.id for role in ctx.author.roles]:
            return
        try:
            message = await channel.fetch_message(message_id)
        except (discord.Forbidden) as e:
            await ctx.send("Hmmm.. Seems like I no longer have READ_MESSAGES permission for that channel for some reason.")
            return
        except (discord.Forbidden, discord.NotFound) as e:
            await ctx.send("It is possible that you gave me the wrong ID or I cannot find the message in the channel due to either the message or channel being deleted.")
            return

        if channel is None:
            return await ctx.send("Are you sure this is in a correct channel?")
        if message != None:
            try:
                await message.edit(content=f"{new_message}")
            except discord.Forbidden:
                await ctx.send("it appears that my SEND_MESSAGES perms have been revoked and I cannot edit the message.")
        else:
            await ctx.send("I'm not really sure what you are trying to do.")

    @commands.bot_has_permissions(manage_roles=True)  
    @commands.command()
    async def minecraftmention(self, ctx: commands.Context, role_name):
        role = Configuration.get_minecraftrole(ctx, role_name)
        Minecraft = discord.utils.get(ctx.guild.roles, id=547868949094727683)

        if 547868949094727683 not in [role.id for role in ctx.author.roles]:
            return

        if role.mentionable:
            await role.edit(mentionable=False)
            await ctx.send(f"{role.name} is now unmentionable!")
        else:
            await role.edit(mentionable=True)
            await ctx.send(f"{role.name} is now mentionable!")


def setup(bot):
    bot.add_cog(mannounce(bot))
