# TgENV
Subir a video con su información a mi mensajero favorito.
## Instalación propia funcional, con ia y sin conocimientos previos, Gracias ciencia por la oportunidad.

```sh
git clone https://github.com/vico32/TelegramENV.git
cd TelegramENV
mkdir media
pip3 install telethon python-dotenv psutil
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
