import discord
import time
import datetime
from discord.ext import commands
from discord import utils
class polling(commands.Cog): 
    """This cog includes the ability to allow Bug Hunters to submit to Trello."""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(hidden=True)
    @commands.guild_only()
    async def poll(self, ctx, *, polling):
        """Allows the selected staff role to post their ideas in community voting channel."""
        role = discord.utils.get(ctx.guild.roles, id=468567532337496084)
        channel = ctx.guild.get_channel(488996984783634432)
        upvote = utils.get(self.bot.emojis, id=481648022795714562)
        downvote = utils.get(self.bot.emojis, id=481648023169007616)
        if role not in ctx.author.roles:
            return await ctx.send("You do not have permission to use this feature.")
            
        if polling != None:
            try:
                embed = discord.Embed(title="New Idea!", colour=discord.Colour(0xf47b67), description=f"{polling}", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
                message = await channel.send(embed=embed)
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the polling channel. Please check that I am able to talk.")
        else: 
            await ctx.send("What are you doing? :(")
    
def setup(bot):
    bot.add_cog(polling(bot))
