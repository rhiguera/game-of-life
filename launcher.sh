#!/bin/bash

# Script de lanzamiento para el Juego de la Vida
# Permite ejecutar el proyecto sin invocar manualmente el intérprete o activar el venv

# Obtener el directorio donde reside el script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Activar el entorno virtual
if [ -d "$DIR/venv" ]; then
    source "$DIR/venv/bin/activate"
else
    echo "Error: No se encontró el entorno virtual en $DIR/venv"
    echo "Por favor, sigue las instrucciones de instalación en README.md"
    exit 1
fi

# Ejecutar la aplicación pasando todos los argumentos recibidos
python3 "$DIR/main.py" "$@"
