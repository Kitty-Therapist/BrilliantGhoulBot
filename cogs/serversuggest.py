import discord
import time
import datetime
from discord.ext import commands
from discord import utils

class serversuggest: 
    """This cog includes the ability to allow Bug Hunters to submit to Trello."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def suggest(self, ctx, *, suggestion = ""):
        channel= ctx.bot.get_channel(12345678901234567)
        upvote = utils.get(self.bot.emojis, id=12345678901234567)
        downvote = utils.get(self.bot.emojis, id=12345678901234567)
        if(suggestion != ""):
            try:
                embed = discord.Embed(title="New Suggestion!", colour=discord.Colour(0xf47b67), description=f"{suggestion}", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
                embed.set_footer(text="Want to suggest? Use +suggest [your idea here!]")
                message = await channel.send(embed=embed)
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
            except discord.Forbidden:
                await ctx.send("I was not able to send to the suggestion channel, make sure I have permissions.")
        else: 
            await ctx.send("There's nothing there, and I can't give a empty suggestion.")

def setup(bot):
    bot.add_cog(serversuggest(bot))
