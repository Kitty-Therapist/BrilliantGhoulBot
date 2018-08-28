import discord
from discord.ext import commands

class announce:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def ping(self, ctx):
            """Shows that the bot is still alive"""
            await ctx.send("I am brilliant!")
            
    @commands.command(hidden=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def giveaways(self, ctx, *, giveaways):
        luminous = [ok, ok, ok]
        channel = ctx.guild.get_channel(hi)
        role = discord.utils.get(ctx.guild.roles, id=ok)
        if role is None:
            return await ctx.send("Did you delete that role, <@29090493204903-34343248>?")
        
        if ctx.author.id not in luminous:
            return await ctx.send("You do not have permission to ping this role. SHAME ON YOU FOR TRYING TO PING PEOPLE FOR NO REASON!")
            
        if giveaways != None:
            try:
                await role.edit(mentionable=True)
                await channel.send(f"{role.mention}\n{giveaways}")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the announcement channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")
    
    @commands.command(hidden=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def announce(self, ctx, *, announce):
        luminous = [ok]
        channel = ctx.guild.get_channel(ok2)
        role = discord.utils.get(ctx.guild.roles, id=sfdfsfgretertregrtgrtgt)

        if role is None:
            return await ctx.send("Did you delete that role, <@258>?")
        
        if ctx.author.id not in luminous:
            return await ctx.send("You do not have permission to use that role. SHAME ON YOU FOR TRYING TO PING PEOPLE FOR NO REASON!")
            
        if announce != None:
            try:
                await role.edit(mentionable=True)
                await channel.send(f"{role.mention}\n{announce}")
                await role.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the announcement channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")

def setup(bot):
    bot.add_cog(announce(bot))
