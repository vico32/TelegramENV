import os
import time
import logging
from main import upload_file

# Expandir el directorio base del proyecto
BASE_DIR = os.path.expanduser('~/TelegramENV')

# Configuración del logging
log_file = os.path.join(BASE_DIR, 'subidas.log')
logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def process_file(file, path):
    logging.info(f"Procesando archivo: {file}")
    upload_file(file, path)

def watch_folder(path):
    seen_files = set()

    # Procesar todos los archivos presentes en la carpeta al iniciar
    current_files = set(os.listdir(path))
    for file in current_files:
        if file.endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mkv', '.avi', '.mov')):
            logging.info(f"Archivo inicial detectado: {file}")
            process_file(file, path)
            seen_files.add(file)

    # Monitorear la carpeta para detectar nuevos archivos
    while True:
        current_files = set(os.listdir(path))
        new_files = current_files - seen_files

        # Procesar nuevos archivos
        for file in new_files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mkv', '.avi', '.mov')):
                logging.info(f"Nuevo archivo detectado: {file}")
                process_file(file, path)
                seen_files.add(file)

        time.sleep(10800)

if __name__ == "__main__":
    carpeta_media = os.path.join(BASE_DIR, 'media')
    logging.info(f"Monitoreando la carpeta: {carpeta_media}")

    if os.path.exists(carpeta_media):
        watch_folder(carpeta_media)
    else:
        logging.error(f"Error: La carpeta {carpeta_media} no existe.")
