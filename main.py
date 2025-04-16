#Importamos la clase discord que nos ayuda a ta ta
import discord
from discord.ext import commands


def segundo_saludo (mensaje):
    
    if 'como estas' in mensaje:
        
        responder = 'Estoy bien, gracias por preguntar. ¿Y tú?'
            
        return responder
        
    elif 'que haces' in mensaje:
            
        responder = 'Nada y tu'
            
        return responder

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_momento():
    print(f'Tu bot {bot.user} esta en linea')
    
@bot.command()
async def kodland(ctx):
    
    await ctx.send('\U0001F642')
    
@bot.command()
async def repetir(ctx, *, mensaje:str): 

    await ctx.send(mensaje)
    
@bot.command()
async def saludo(ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if 'hola' in mensaje:
        
        await ctx.send('Hola, ¿cómo estás?')
        
        opcion =  segundo_saludo(mensaje)
        
        await ctx.send(opcion)
        
        
    elif 'que onda' in mensaje:
        
        await ctx.send('Hola, ¿qué tal?')
        
        opcion =  segundo_saludo(mensaje)
        
        await ctx.send(opcion)
        
    else:
        
        await ctx.send('No entendi tu saludo pero holaaa')
        
@bot.command()
async def sumar(ctx, num1: str, num2: str):
    try:
        # Convertimos los argumentos a enteros
        num1 = int(num1)
        num2 = int(num2)
        
        # Realizamos la suma
        resultado = num1 + num2
        await ctx.send(f'La suma de {num1} y {num2} es: {resultado}')
    except ValueError:
        # Si no se pueden convertir a enteros, enviamos un mensaje de error
        await ctx.send('Por favor, asegúrate de ingresar números válidos.')
    
@bot.command()
async def restar(ctx, num1:int, num2:int):
    
    resultado = num1 - num2
    
    await ctx.send(f'La resta de {num1} y {num2} es: {resultado}')
    
@bot.command()
async def multiplicar(ctx, num1:int, num2:int):
    
    resultado = num1 * num2
    
    await ctx.send(f'La multiplicacion de {num1} y {num2} es: {resultado}')
    
@bot.command()
async def dividir(ctx, num1:int, num2:int):
    
    if num2 == 0:
        await ctx.send('No se puede dividir entre cero.')
    else:
        resultado = num1 / num2
        await ctx.send(f'La division de {num1} y {num2} es: {resultado}')
        
token = ''

bot.run(token)