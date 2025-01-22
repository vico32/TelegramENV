# -*- coding: utf-8 -*-

import os
import subprocess
import psutil  # Biblioteca para verificar procesos activos

def is_watcher_running():
    """
    Verifica si watcher.py ya está en ejecución.
    """
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if 'python3' in proc.info['name'] and 'watcher.py' in proc.info['cmdline']:
            return True
    return False

def run_watcher():
    """
    Inicia watcher.py si no está en ejecución.
    """
    if is_watcher_running():
        print("watcher.py ya está en ejecución. No se iniciará un nuevo proceso.")
    else:
        try:
            print("Iniciando watcher.py para monitorear la carpeta...")
            subprocess.Popen(['python3', 'watcher.py'])
        except Exception as e:
            print(f"Error al iniciar watcher.py: {e}")

if __name__ == "__main__":
    run_watcher()

    # Mantener el script principal en ejecución para manejo de eventos futuros
    try:
        print("start_bot.py ejecutándose. Presiona Ctrl+C para detener.")
        while True:
            pass
    except KeyboardInterrupt:
        print("Bot detenido manualmente.")
