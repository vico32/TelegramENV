# TgENV
Subir a video con su información a mi mensajero favorito.
## Instalación propia funcional, con ia y sin conocimientos previos, Gracias ciencia por la oportunidad.

```sh
git clone https://github.com/vico32/TelegramENV.git
cd TelegramENV
mkdir media
pip3 install telethon python-dotenv psutil
python3 watcher.py
```
```
#Insertas tu número de cell con prefijo y te pedira el codigo de confirmación de telegram.
#Para que inicie cron de 3 horas y no recargues el sistema ejecuta el siguiente comando.
python3 start_bot.py
```

```sh
Estructura

TelegramENV/
│
├── .env               # Archivo con las credenciales
├── start_bot.py       # Archivo principal que ejecuta todo
├── watcher.py         # Se ejecuta una primera vez, termina de loguearte y queda monitoreando la carpeta media
├── main.py            # Envía los archivos al canal publico en el servidor.
└── /media/            # Carpeta que contiene los archivos para procesar
    ├── archivo1.jpg
    ├── archivo1.txt   # Descripción para archivo1.jpg
    └── archivo1.mp4

El script recoge la información y la sube al servidor como descripciòn del jpg.
```
```sh

Archivo .env

API_ID y API_HASH: Los obtienes desde el portal de desarrolladores de Telegram (my.telegram.org).
PHONE_NUMBER: El número de teléfono que usas para iniciar sesión en Telegram (formato internacional con el prefijo).
CHAT_ID: El chat_id o el nombre del canal creado donde quieres enviar los archivos (tiene que ser publico).

Primera ejecución python3 watcher.py

```
