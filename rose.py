import discord
from discord.ext import commands

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

# Comando de teste
@bot.command()
async def oi(ctx):
    await ctx.send("oi 😭🌹")

# Comando para criar mensagem fixa
@bot.command()
async def setup(ctx):

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
            "Pega um café, um chá ou só o cansaço da madrugada mesmo e fica à vontade.\n\n"

            "Esse é um cantinho que temos para converçar, ouvir músicas que dizem coisas "
            "que às vezes faltam palavras para explicar, jogos e aquelas prozas "
            "que começam aleatórias e acabam ficando tão profundas que acabamos indo"
            "preparar um cafe ou chá pra continuar a converça.\n\n"

            "Não precisa ter pressa para se enturma, Às vezes uma amizade começa "
            "por uma música, uma conversa qualquer ou só pela companhia tranquila "
            "de alguém. 🌿"

            "Caso você não saiba oque dizer, ou como dizer, por timidez apenas diga algo "
            "que você gosta, como por exemplo alguma musica que você gosta de ouvir ou tocar "
            "um filme que você tenha assistido ultimamente e etc, mais nao se prenda a timidez, "
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

# Token do bot
import os

bot.run(os.getenv("TOKEN"))
