import discord
import requests
import random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Hello there! my username and ID is  {bot.user.name}({bot.user.id})")

@bot.command()
async def ifacts(ctx):
    try:
        fact_1 = requests.get("http://numbersapi.com/random/trivia?json")
        fact1_data = fact_1.json()
        fact1 = fact1_data["text"]

        fact_2 = requests.get("http://numbersapi.com/random/trivia?json")
        fact2_data = fact_2.json()
        fact2 = fact2_data["text"]

        fact_3 = requests.get("http://numbersapi.com/random/trivia?json")
        fact3_data = fact_3.json()
        fact3 = fact3_data["text"]

        fact_information = (
            f"Fact 1: {fact1}\n"
            f"Fact 2: {fact2}\n"
            f"Fact 3: {fact3}"
        )

        await ctx.send(fact_information)
    except Exception as exc:
        await ctx.send(f"An error occurred: {exc}")

@bot.command()
async def roll_it(ctx):
    outcome = random.randint(1, 6)
    await ctx.send(f"Hey!! Move by {outcome}!!!")

@bot.command()
async def Fun_Facts(ctx):
    try:
        Fun_Fact= requests.get("https://official-joke-api.appspot.com/random_joke")
        Fun_data = Fun_Fact.json()
        setup = Fun_data["setup"]
        punchline = Fun_data["punchline"]
        
        await ctx.send(f"Try not to laugh:\n{setup}\n{punchline}")
    except Exception as exc:
        await ctx.send(f"An error occurred: {exc}")

bot.run("")#Enter discord authentication token here
