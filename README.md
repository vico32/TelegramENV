# TgENV
Subir a video con su información a mi mensajero favorito.
## Instalación propia funcional, con ia y sin conocimientos previos, Gracias ciencia por la oportunidad.

```sh
git clone https://github.com/vico32/TelegramENV
cd TelegramENV
pip3 install telethon python-dotenv
python3 start_bot.py
```

```sh
Estructura

TelegramENV/
│
├── start_bot.py       # Archivo principal que ejecuta todo
├── watcher.py         # Monitorea la carpeta
├── main.py            # Envía los archivos al bot
└── /media/      # Carpeta que contiene los archivos para procesar
    ├── archivo1.jpg
    ├── archivo1.txt   # Descripción para archivo1.jpg
    └── archivo1.mp4

El script recoge la información y la sube al servidor como descripciòn del jpg.
```
