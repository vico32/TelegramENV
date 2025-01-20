# -*- coding: utf-8 -*-

import subprocess

def run_watcher():
    try:
        print("Iniciando watcher.py para monitorear la carpeta...")
        subprocess.Popen(['python3', 'watcher.py'])
    except Exception as e:
        print(f"Error al iniciar watcher.py: {e}")

if __name__ == "__main__":
    run_watcher()

    # Mantén el script en ejecución indefinidamente
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Bot detenido manualmente.")
