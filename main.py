import os
import logging
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configuración del logging
log_file = os.path.expanduser('~/TelegramENV/subidas.log')  # Usar ~ para rutas relativas al usuario
logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Credenciales de Telegram desde el archivo .env
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
chat_id = os.getenv('CHAT_ID')

# Inicializar cliente de Telegram con sesión personalizada
session_file = os.path.expanduser('~/TelegramENV/session_name')  # Archivo de sesión en la misma estructura
client = TelegramClient(session_file, api_id, api_hash)

async def authenticate():
    """
    Verifica si el cliente está autenticado. Si no, realiza el inicio de sesión automáticamente.
    """
    if not await client.is_user_authorized():
        logging.info("El cliente no está autenticado. Solicitando código de inicio de sesión.")
        await client.send_code_request(phone_number)
        code = input("Ingrese el código que recibió: ")
        try:
            await client.sign_in(phone_number, code)
            logging.info("Autenticación exitosa.")
        except SessionPasswordNeededError:
            password = input("Ingrese la contraseña de autenticación de dos pasos: ")
            await client.sign_in(password=password)
            logging.info("Autenticación completada con éxito.")

async def send_file_to_chat(file, path):
    """
    Sube un archivo al canal/chat especificado.
    """
    file_path = os.path.join(path, file)
    logging.info(f"Iniciando la subida del archivo: {file}")

    try:
        if file.endswith(('.mp4', '.mov', '.avi', '.mkv')):
            await client.send_file(
                chat_id,
                file_path,
                supports_streaming=True,
                caption=file.split('.')[0]
            )
        elif file.endswith(('.jpg', '.jpeg', '.png')):
            description_file = file.replace(file.split('.')[-1], 'txt')
            description = None
            if os.path.exists(os.path.join(path, description_file)):
                with open(os.path.join(path, description_file), 'r') as f:
                    description = f.read()

            await client.send_file(
                chat_id,
                file_path,
                caption=description if description else file.split('.')[0]
            )
        else:
            await client.send_file(chat_id, file_path, caption=file.split('.')[0])

        logging.info(f"Archivo subido exitosamente: {file}")

    except Exception as e:
        logging.error(f"Error durante la subida del archivo {file}: {e}")

async def start_upload(file, path):
    """
    Inicia el proceso de autenticación y subida de archivos.
    """
    await authenticate()
    await send_file_to_chat(file, path)

def upload_file(file, path):
    """
    Punto de entrada para el cliente de Telegram.
    """
    with client:
        client.loop.run_until_complete(start_upload(file, path))
