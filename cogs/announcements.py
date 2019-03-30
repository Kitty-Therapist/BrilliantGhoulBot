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

class announcements(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_result = None 
    
    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.bot_has_permissions(manage_roles=True)       
    @commands.command()
    async def announce(self, ctx: commands.Context, role_name, *, message):
        Admins = discord.utils.get(ctx.guild.roles, id=485125261470203905)
        role = Configuration.get_role(ctx, role_name)
        channel = Configuration.get_channel(ctx, role_name)

        if 485125261470203905 not in [role.id for role in ctx.author.roles]:
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
    async def update(self, ctx: commands.Context, role_name, message_id:int, *, new_message):
        channel = Configuration.get_channel(ctx, role_name)
        Admins = discord.utils.get(ctx.guild.roles, id=485125261470203905)

        if 485125261470203905 not in [role.id for role in ctx.author.roles]:
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
    async def mention(self, ctx: commands.Context, role_name):
        role = Configuration.get_role(ctx, role_name)
        Mods = discord.utils.get(ctx.guild.roles, id=485125261470203905)

        if 485125261470203905 not in [role.id for role in ctx.author.roles]:
            return

        if role.mentionable:
            await role.edit(mentionable=False)
            await ctx.send(f"{role.name} is now unmentionable!")
        else:
            await role.edit(mentionable=True)
            await ctx.send(f"{role.name} is now mentionable!")
    
    @commands.command(pass_context=True, hidden=True, name='eval')
    async def eval(self, ctx, *, body: str):
        """Evaluates a code"""
        Admins = discord.utils.get(ctx.guild.roles, id=485125261470203905)

        if 485125261470203905 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")


        if "token" in body:
            await ctx.send("No token stealing allowed.")
            return

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

def setup(bot):
    bot.add_cog(announcements(bot))
