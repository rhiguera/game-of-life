# Plan de Implementación: Juego de la Vida (Conway)

Este documento detalla la estrategia para implementar el Juego de la Vida con una arquitectura modular y visualmente atractiva.

## Objetivos
- Implementación modular: Separación clara entre lógica de juego e interfaces.
- Interfaz dual: GUI (Pygame) y CLI (Consola).
- Visualización avanzada: Indicación de "edad" de las celdas mediante gradientes de color.
- Calidad de código: Tests unitarios y entorno virtual.

## Arquitectura de Archivos
- `core/grid.py`: Lógica del autómata celular y seguimiento de edad.
- `ui/interface.py`: Clase base abstracta para las UIs.
- `ui/pygame_view.py`: Interfaz gráfica con Pygame y visualización de edad.
- `ui/console_view.py`: Interfaz de terminal simple.
- `main.py`: Punto de entrada con selector de modo.
- `tests/test_grid.py`: Suite de pruebas unitarias.

## Fases de Implementación

### Fase 1: Configuración e Inicialización
- Crear entorno virtual y dependencias.
- Inicializar Git y estructura de carpetas.

### Fase 2: Lógica del Juego (Core)
- Implementar clase `Grid` con reglas B3/S23.
- Añadir contador de generaciones por celda (edad).
- Crear tests unitarios iniciales.

### Fase 3: Interfaces (UI)
- Crear interfaz base abstracta.
- Implementar `ConsoleUI` para depuración rápida.
- Implementar `PygameUI` con gradientes de color según edad.

### Fase 4: Integración
- Unificar en `main.py` con `argparse`.
- Documentación final.
