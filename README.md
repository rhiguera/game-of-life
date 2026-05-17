# Game of Life - Aging Cells

Una implementación modular del Juego de la Vida de Conway en Python, con seguimiento de edad de las celdas y visualización dinámica.

## Características
- **Arquitectura Modular**: Separación de lógica central, interfaces y tests.
- **GUI Visual (Pygame)**: Celdas que cambian de color según su longevidad (Verde -> Azul).
- **Modo Consola**: Interfaz ligera para terminal.
- **Interactividad**: Dibujo de celdas con el ratón, pausa y reset.

## Requisitos
- Python 3.12+
- Pygame

## Instalación

1. Crear entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecutar la GUI (por defecto):
```bash
python3 main.py
```

Ejecutar en modo consola:
```bash
python3 main.py --mode console
```

### Controles (GUI)
- **Click Izquierdo**: Activar/Desactivar celda.
- **Espacio**: Pausa / Reanudar.
- **R**: Limpiar cuadrícula (Reset).

## Tests
Ejecutar la suite de pruebas unitarias:
```bash
python3 -m unittest discover tests
```
