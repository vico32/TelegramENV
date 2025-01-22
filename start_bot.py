# -*- coding: utf-8 -*-
import os
import subprocess

# Ruta al directorio base del proyecto
BASE_DIR = os.path.expanduser('~/TelegramENV')

def add_cron_job():
    """
    Agrega una tarea a cron para ejecutar watcher.py cada 3 horas.
    """
    cron_command = f"python3 {os.path.join(BASE_DIR, 'watcher.py')}"
    job = f"0 */3 * * * {cron_command}\n"

    try:
        # Leer las tareas actuales de cron
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_cron_jobs = result.stdout.splitlines()

        # Verificar si ya existe la tarea
        if any(cron_command in job for job in current_cron_jobs):
            print("La tarea de cron ya está configurada.")
            return

        # Agregar la nueva tarea
        current_cron_jobs.append(job)
        updated_cron_jobs = '\n'.join(current_cron_jobs)

        # Actualizar las tareas de cron
        subprocess.run(['crontab', '-'], input=updated_cron_jobs, text=True)
        print("Tarea de cron configurada para ejecutar watcher.py cada 3 horas.")

    except Exception as e:
        print(f"Error al configurar la tarea de cron: {e}")

def remove_cron_job():
    """
    Elimina la tarea de cron relacionada con watcher.py.
    """
    cron_command = f"python3 {os.path.join(BASE_DIR, 'watcher.py')}"
    try:
        # Leer las tareas actuales de cron
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_cron_jobs = result.stdout.splitlines()

        # Filtrar la tarea a eliminar
        updated_cron_jobs = [job for job in current_cron_jobs if cron_command not in job]

        # Actualizar las tareas de cron
        subprocess.run(['crontab', '-'], input='\n'.join(updated_cron_jobs), text=True)
        print("Tarea de cron eliminada.")
    except Exception as e:
        print(f"Error al eliminar la tarea de cron: {e}")

if __name__ == "__main__":
    print("Configurando cron para watcher.py...")
    add_cron_job()
