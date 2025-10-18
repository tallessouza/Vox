import discord
import os
import aiohttp
import logging
from transcription import transcrever_audio

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

TOKEN = ""
INTENTS = discord.Intents.default()
INTENTS.message_content = True  # necessário para ler mensagens
client = discord.Client(intents=INTENTS)

@client.event
async def on_ready():
    print(f"✅ Bot conectado como {client.user}")

@client.event
async def on_message(message):
    # ignora as mensagens do próprio bot
    if message.author == client.user:
        return

    # Teste simples
    if message.content.lower() == "!ping":
        await message.channel.send("🏓 Pong!")
        return

    # Se houver um arquivo anexado
    if message.attachments:
        for attachment in message.attachments:
            # Verifica se é um tipo de áudio comum
            if attachment.filename.endswith(('.mp3', '.wav', '.m4a', '.ogg')):
                # Cria a pasta audios/ se não existir
                os.makedirs("audios", exist_ok=True)

                file_path = os.path.join("audios", attachment.filename)
                await attachment.save(file_path)
                print(f"🎧 Áudio salvo em: {file_path}")

                await message.channel.send(f"🎙️ Recebi o arquivo `{attachment.filename}`, transcrevendo...")

                try:
                    texto = transcrever_audio(file_path)
                    await message.channel.send(f"📝 Transcrição:\n```{texto}```")
                except Exception as e:
                    await message.channel.send(f"⚠️ Ocorreu um erro na transcrição: `{e}`")
                return

client.run(TOKEN)
