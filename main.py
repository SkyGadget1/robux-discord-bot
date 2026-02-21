import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def calcular_robux(robux):
    valor_gamepass = robux / 0.7
    a_cuanto_vendo = robux * 7.5 / 1000 * 1530
    a_cuanto_compro = valor_gamepass * 4 / 1000 * 1530
    ganancia = a_cuanto_vendo - a_cuanto_compro

    return valor_gamepass, a_cuanto_vendo, a_cuanto_compro, ganancia

@bot.command()
async def robux(ctx, cantidad: float):
    valor_gamepass, vendo, compro, ganancia = calcular_robux(cantidad)

    embed = discord.Embed(
        title="💰 Calculadora de Robux",
        color=discord.Color.green()
    )

    embed.add_field(name="Cantidad de Robux", value=f"{cantidad:,.0f}", inline=False)
    embed.add_field(name="Valor Gamepass", value=f"{valor_gamepass:,.2f}", inline=True)
    embed.add_field(name="A cuánto lo vendo", value=f"${vendo:,.2f}", inline=True)
    embed.add_field(name="A cuánto lo compro", value=f"${compro:,.2f}", inline=True)
    embed.add_field(name="Ganancia", value=f"💵 ${ganancia:,.2f}", inline=False)

    await ctx.send(embed=embed)


bot.run(TOKEN)
