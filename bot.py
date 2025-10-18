import discord
import os
import asyncio
import logging
import pprint
from dotenv import load_dotenv
from services import AssemblyAIService, AssemblyAIError

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Discord bot configuration
TOKEN = os.getenv("DISCORD_TOKEN", "")
INTENTS = discord.Intents.default()
INTENTS.message_content = True  # necessário para ler mensagens
client = discord.Client(intents=INTENTS)

# Initialize AssemblyAI service
try:
    assemblyai_service = AssemblyAIService()
    logger.info("AssemblyAI service initialized")
except AssemblyAIError as e:
    logger.warning(f"AssemblyAI service not available: {e}")
    assemblyai_service = None

async def process_audio_task(message: discord.Message, attachment: discord.Attachment, filename: str, file_path: str) -> None:
    """Process audio file with transcription (async task).

    This function runs in the background without blocking the Discord event loop.
    It handles transcription, posts results, and cleans up the audio file.

    Args:
        message: Discord message object to send responses to
        attachment: Audio file attachment
        filename: Original filename
        file_path: Local path where audio was saved

    Returns:
        None (posts results to Discord channel)
    """
    try:
        logger.info(f"Starting audio processing for {filename}")

        # Check if AssemblyAI service is available
        if not assemblyai_service:
            await message.channel.send(
                "⚠️ Serviço de transcrição não está configurado. "
                "Configure a variável ASSEMBLYAI_API_KEY."
            )
            return

        # Transcribe audio with speaker labels
        transcription_data = await assemblyai_service.transcribe_audio(file_path)

        # Extract data
        formatted_text = transcription_data["formatted_text"]
        audio_duration = transcription_data["audio_duration"]
        confidence = transcription_data.get("confidence")
        num_speakers = len(set(u["speaker"] for u in transcription_data["utterances"]))

        # Format duration (milliseconds to minutes:seconds)
        duration_seconds = audio_duration / 1000
        duration_str = f"{int(duration_seconds // 60)}:{int(duration_seconds % 60):02d}"

        # Build header with metadata
        header = f"📝 **Transcrição Completa** ({duration_str})"
        if num_speakers > 1:
            header += f" - {num_speakers} pessoas identificadas"
        if confidence:
            header += f" - Confiança: {confidence:.1%}"

        await message.channel.send(header)

        # Post formatted transcription (split if too long for Discord's 2000 char limit)
        if len(formatted_text) > 1900:
            # Split into chunks
            chunks = [formatted_text[i:i+1900] for i in range(0, len(formatted_text), 1900)]
            for i, chunk in enumerate(chunks):
                await message.channel.send(f"```{chunk}```")
        else:
            await message.channel.send(f"```{formatted_text}```")

        logger.info(
            f"Transcription completed for {filename}: "
            f"{num_speakers} speakers, {duration_str}, confidence: {confidence}"
        )

    except AssemblyAIError as e:
        logger.error(f"AssemblyAI error for {filename}: {e}")
        try:
            await message.channel.send(f"⚠️ Erro na transcrição: {str(e)}")
        except Exception as send_error:
            logger.error(f"Failed to send error message to Discord: {send_error}")
    except Exception as e:
        logger.error(f"Unexpected error processing {filename}: {e}", exc_info=True)
        try:
            await message.channel.send(f"⚠️ Ocorreu um erro inesperado na transcrição: {str(e)}")
        except Exception as send_error:
            logger.error(f"Failed to send error message to Discord: {send_error}")
    finally:
        # Clean up: delete local audio file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Deleted audio file: {file_path}")
        except Exception as e:
            logger.error(f"Failed to delete audio file {file_path}: {e}")


@client.event
async def on_ready():
    logger.info(f"✅ Bot conectado como {client.user}")
    print(f"✅ Bot conectado como {client.user}")


@client.event
async def on_message(message):
    """Handle incoming Discord messages.

    Responds to !ping command and processes audio file attachments.
    """
    # Ignora as mensagens do próprio bot
    if message.author == client.user:
        return

    # Teste simples - !ping command (existing functionality preserved)
    logger.info(f"📨 Comando recebido: {message}")
    
    # Printar atributos específicos do objeto message
    message_info = {
        'id': message.id,
        'content': message.content,
        'author': str(message.author),
        'channel': str(message.channel),
        'guild': str(message.guild) if message.guild else None,
        'created_at': message.created_at,
        'edited_at': message.edited_at,
        'type': message.type,
        'flags': message.flags,
        'attachments': [str(att) for att in message.attachments],
        'embeds': [str(emb) for emb in message.embeds],
        'reactions': [str(react) for react in message.reactions],
        'mentions': [str(mention) for mention in message.mentions],
        'role_mentions': [str(role) for role in message.role_mentions],
        'channel_mentions': [str(channel) for channel in message.channel_mentions]
    }
    
    logger.info(f"📨 Objeto message detalhado: {pprint.pformat(message_info, width=120)}")
    if message.content.lower() == "!ping":
        logger.info(f"📨 Comando !ping recebido de {message.author} no canal #{message.channel}")
        await message.channel.send("🏓 Pong!")
        return

    # Se houver um arquivo anexado
    if message.attachments:
        for attachment in message.attachments:
            # Verifica se é um tipo de áudio comum
            if attachment.filename.endswith(('.mp3', '.wav', '.m4a', '.ogg')):
                logger.info(f"🎵 Arquivo de áudio recebido: {attachment.filename} de {message.author}")
                # Cria a pasta audios/ se não existir
                os.makedirs("audios", exist_ok=True)

                file_path = os.path.join("audios", attachment.filename)
                await attachment.save(file_path)
                logger.info(f"🎧 Áudio salvo em: {file_path}")

                # Send immediate confirmation (non-blocking)
                await message.channel.send(
                    f"🎙️ Recebi o arquivo `{attachment.filename}`, transcrevendo..."
                )

                # Process audio in background task (async, non-blocking)
                asyncio.create_task(
                    process_audio_task(message, attachment, attachment.filename, file_path)
                )

                # Return immediately so bot remains responsive
                return


if __name__ == "__main__":
    if not TOKEN:
        logger.error("DISCORD_TOKEN not found in environment variables!")
        print("❌ Erro: Configure a variável DISCORD_TOKEN no arquivo .env")
    else:
        client.run(TOKEN)
