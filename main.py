try:
    import conf
except:
    pass
import discord
from discord.ext import commands
import img_handler as imhl
import os

intense = discord.Intents.default()
intense.members = True

s = "!"
bot = commands.Bot(command_prefix="!", intents=intense)
channel = 827854542291992637
servname = "Bots"
flag = False

@bot.command(name = "hello")
async def command_hello(ctx):
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            msg = f'Привет, {ctx.author.name}!'
            await ctx.channel.send(msg)

@bot.command(name = "about_me")
async def command_about_me(ctx):
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:   
            msg = f'{ctx.author.name}, твое имя на сервере {ctx.author.nick}. Твой айди {ctx.author.id}'
    await ctx.channel.send(msg)

@bot.command(name = "get_channels")
async def command_getch(ctx):
    msg = " "
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            msg += "Список каналов, к которым у меня есть доступ:" + "\n"
            cat = ctx.author.guild.by_category()
            for i in range(len(cat)):
                msg += f"Категория: {cat[i][0].name}, id: {cat[i][0].id}"
                if cat[i][0].nsfw == True:
                    msg += f" (18+)" + "\n"
                else:
                    msg += "\n"
                for j in range(len(cat[i][1])):
                    msg += f"{j+1}. Канал: {cat[i][1][j].name}, id: {cat[i][1][j].id}"
                    if cat[i][1][j].nsfw == True:
                        msg += f" (18+)" + "\n"
                    else:
                        msg += "\n"
    await ctx.channel.send(msg)

@bot.command(name = "repeat")
async def command_rep(ctx, *args):
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            if (len(args) == 0):
                msg = f"Умно, ничего не скажешь"
            else:
                message = " ".join(args)
                msg = f"{message}"
            await ctx.channel.send(msg)

@bot.command(name = "get_members")
async def command_get_members(ctx, *args):
    msg = " "
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            m = 10
            if (len(args) != 0):
                if (args[0].isdigit()):
                    m = int(args[0])
                    for idx, member in list(enumerate(ctx.author.guild.members)):
                        msg += f'{idx+1}. {member.name} ({member.nick if member.nick else "" }) - {member.id}\n'
                        if (idx+1 == m):
                            break
                elif (args[0]=="all"):
                    for idx, member in list(enumerate(ctx.author.guild.members)):
                        msg += f'{idx+1}. {member.name} ({member.nick if member.nick else "" }) - {member.id}\n'
                else:
                    msg = f"Я не могу вывести такое кол-во пользователей\n"
            else:
                if (len(ctx.author.guild.members) > 10):
                    msg = f"Кол-во пользователей больше 10, выведены первые 10. (Для получения списка введите !get_members (кол-во пользователей))\n"
                    for idx, member in list(enumerate(ctx.author.guild.members)):
                        msg += f'{idx+1}. {member.name} ({member.nick if member.nick else "" }) - {member.id}\n'
                        if (idx+1 == m):
                            break
                else:
                    for idx, member in list(enumerate(ctx.author.guild.members)):
                        msg += f'{idx+1}. {member.name} ({member.nick if member.nick else "" }) - {member.id}\n'
        await ctx.channel.send(msg)

@bot.command(name = "get_member")
async def command_getmember(ctx, member:discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            if member:
                msg = f'Member {member.name} {f"({member.nick})" if member.nick else ""} - {member.id}'
            if msg == None:
                msg = "Ошибка!"
            
            await ctx.channel.send(msg)

@bot.command(name = "mk")
async def command_mk(ctx, f1:discord.Member=None, f2:discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            if f1 and f2:
                msg = f'Щас начнут бой {f1.name} {f"({f1.nick})" if f1.nick else ""} и {f2.name} {f"({f2.nick})" if f2.nick else ""}'
                await imhl.vs_create(f1.avatar_url, f2.avatar_url)
            elif f1:
                msg = f'Щас начнут бой {f1.name} {f"({f1.nick})" if f1.nick else ""} и {bot.user.name}'
                await imhl.vs_create(f1.avatar_url, bot.user.avatar_url)
            else:
                msg = f'Введите имена через @'
        await ctx.channel.send(msg)
        await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))

@bot.command(name="join")
async def vc_join(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            msg = f"Подключаюсь к {voice_channel.name}"
            await ctx.channel.send(msg)
            await voice_channel.connect()

@bot.command(name="leave")
async def vc_leave(ctx):
    msg = ""
    global channel
    voice_channel = ctx.author.voice.channel

    if ctx.channel.id == channel:
        msg = f"Отключаюсь от {voice_channel.name}"
        await ctx.channel.send(msg)
        await ctx.voice_client.disconnect()

@bot.command(name="ost")
async def vs_ost(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        msg = f"mk..."

        await ctx.channel.send(msg)
        await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))



@bot.command(name="fight")
async def babuin(ctx, f1:discord.Member=None, f2:discord.Member=None):
    msg = ""
    global channel
    voice_channel = ctx.author.voice.channel

    if ctx.channel.id == channel:
        if voice_channel:
            if ctx.author.guild.name == servname:
                if f1 and f2:
                    msg = f'Щас начнут бой {f1.name} {f"({f1.nick})" if f1.nick else ""} и {f2.name} {f"({f2.nick})" if f2.nick else ""}'
                    await imhl.vs_create(f1.avatar_url, f2.avatar_url)
                    await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))
                    msg = f"Подключаюсь к {voice_channel.name}"
                    await ctx.channel.send(msg)
                    await voice_channel.connect()
                    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
                    await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))
                else:
                    msg = f'Введите имена через @'
            await ctx.channel.send(msg)

bot.run(os.environ["BOT_TOKEN"])