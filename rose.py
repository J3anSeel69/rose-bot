import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask('')

#comandos ativos
oi_ativo = False
setup_ativo = False

@app.route('/')
def home():
    return "Rose está viva 🌹"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run_web)
    t.start()


# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True

# Criando o bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# Quando a Rose ligar
@bot.event
async def on_ready():
    print(f'{bot.user} está online! 🌹')

    # Status da Rose
    await bot.change_presence(
        activity=discord.CustomActivity(
            name="preparando um chá de hibisco 🍵"
        )
    )

@bot.event
async def on_disconnect():
    print("Bot desconectou 😭")

@bot.event
async def on_resumed():
    print("Bot reconectou 🌹")


# Comando de teste
@bot.command()
async def oi(ctx):

    if not oi_ativo:
        return
        
    await ctx.send("oi 😭🌹")

# Comando para criar mensagem fixa
@bot.command()
async def setup(ctx):

    if not setup_ativo:
        return

    # Procurar canal
    canal = discord.utils.get(
        ctx.guild.text_channels,
        name="boas-vindas"
    )

    # Caso não encontre
    if canal is None:
        await ctx.send(
            "Não encontrei o canal #boas-vindas 😭"
        )
        return

    # Criando embed
    embed = discord.Embed(
        title="🌙 Bem-vindo ao TV-Girls Night",
        description=(
            "Ola eu sou a Rose, eu procuro sempre mostra hospitalidade e dar as primeiras boas vindas "
            "pega um café, um chá ou só o cansaço da madrugada mesmo e fica à vontade.\n\n"

            "Esse é um cantinho que temos para converçar, ouvir músicas que dizem coisas "
            "que às vezes faltam palavras para explicar, jogos e aquelas prozas "
            "que começam aleatórias e acabam ficando tão profundas que acabamos indo "
            "preparar um cafe ou chá pra continuar a converça.\n\n"

            "Não precisa ter pressa para se enturma, Às vezes uma amizade começa "
            "por uma música, uma conversa qualquer ou só pela companhia tranquila "
            "de alguém. 🌿\n\n"

            "Caso você não saiba oque dizer, ou como dizer, por timidez apenas diga algo "
            "que você gosta, como por exemplo alguma musica que você gosta de ouvir ou tocar "
            "um filme que você tenha assistido ultimamente e etc, mais não se prenda a timidez, "
            "entre nas converças tambem, tenho certeza que todos iram lhe acolher aqui.\n\n"

            "Bom agora eu vo procurar pelo Noah, ate Logo 😊"
        ),
        color=0xd88cff
    )

    # IMAGEM GRANDE NO TOPO
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1513743197812293692/1513750683424133130/Boavinda.jpg?ex=6a28ddaf&is=6a278c2f&hm=4b4dac00f09fe414f8d7b2f28ae7265191fee63ce28dfe5ef63b68ba7d59511e&"
    )

    # Rodapé
    embed.set_footer(
        text="Rose 🌹 • entre o rosa das lembranças e o azul das madrugadas"
    )

    # Enviar mensagem
    mensagem = await canal.send(
        embed=embed
    )

    # Fixar mensagem
    await mensagem.pin()

    # Confirmar
    await ctx.send(
        "Mensagem enviada e fixada no #boas-vindas 🌹"
    )

#Mensagem fake nao conta pra ninguem
@bot.command()
async def msg(ctx, canal_nome, *, mensagem):

    # Só você pode usar
    if ctx.author.id != 1343655943828930560:
        return

    # Procurar canal
    canal = discord.utils.get(
        ctx.guild.text_channels,
        name=canal_nome
    )

    # Caso não encontre
    if canal is None:
        await ctx.send("Não achei esse canal 😭")
        return

    # Apaga o comando
    await ctx.message.delete()

    # Rose envia mensagem
    await canal.send(mensagem)

# Token do bot
import os

keep_alive()


bot.run(
    os.getenv("TOKEN"),
    reconnect=True
)
