# Documentación Técnica: Juego de la Vida (Conway) con Envejecimiento de Celdas

Esta documentación detalla la arquitectura, tecnologías y uso de la implementación modular del Juego de la Vida.

## 1. Tecnologías Usadas
- **Lenguaje**: Python 3.12+
- **Interfaz Gráfica**: Pygame 2.6.1 (Abstracción sobre SDL).
- **Entorno**: Entorno virtual (venv) para gestión de dependencias.
- **Testing**: Unittest (Framework estándar de Python).
- **Control de Versiones**: Git.

## 2. Arquitectura de la Solución

El proyecto sigue un patrón de diseño similar a **MVC (Modelo-Vista-Controlador)** para garantizar la separación de responsabilidades.

### Diagrama Conceptual
```text
[ Grid (Core/Modelo) ] <--- [ Interface (Abstract Base) ]
        ^                               |
        |                      /--------+--------\
        |                     v                  v
[ main.py (Entry) ] --> [ PygameUI ]       [ ConsoleUI ]
```

### Componentes:
- **Core (Modelo)**: Contiene el estado de la simulación, el contador de generaciones y las leyes físicas (reglas de Conway). No conoce nada de la interfaz.
- **UI (Vista/Controlador)**: Se encarga de representar el estado del `Grid` y capturar la entrada del usuario (ratón y teclado) para modificar el estado o controlar el flujo de la simulación.
- **Main (Orquestador)**: Configura la aplicación basándose en los parámetros de la línea de comandos e inicializa el bucle principal.

## 3. Estructura de Directorios y Ficheros

```text
game-of-life/
├── core/
│   ├── __init__.py
│   └── grid.py         # Clase Grid: Lógica de evolución, edad y contador de generaciones.
├── ui/
│   ├── __init__.py
│   ├── interface.py    # Clase base abstracta BaseUI.
│   ├── console_view.py # Implementación CLI para terminal.
│   └── pygame_view.py  # Implementación GUI avanzada con Pygame.
├── tests/
│   ├── __init__.py
│   └── test_grid.py    # Tests unitarios de la lógica central.
├── main.py             # Punto de entrada, población inicial aleatoria y gestión de argumentos.
├── launcher.sh         # Script Bash para ejecución simplificada.
├── README.md           # Guía rápida de inicio y presentación.
├── DOCUMENTATION.md    # Esta documentación detallada.
├── PLAN.md             # Plan de diseño inicial.
├── requirements.txt    # Dependencias del proyecto.
└── .gitignore          # Archivos excluidos de Git.
```

## 4. Lógica de Envejecimiento y Visualización

### Sistema de Edad
A diferencia de la implementación estándar, cada celda almacena un valor entero:
- **0**: Muerta.
- **1**: Recién nacida.
- **n**: Ha sobrevivido durante *n* generaciones consecutivas.

### Representación Visual (Pygame)
La interfaz gráfica utiliza un gradiente de color interpolado para representar la madurez de la colonia:
- **Fase Inicial (Verde Neón)**: Celdas jóvenes y vibrantes.
- **Fase de Transición (Cian)**: Celdas que han sobrevivido varias generaciones.
- **Fase de Madurez (Azul Eléctrico)**: Celdas longevas que forman parte de estructuras estables.

## 5. Uso de la Aplicación

### Instalación de dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Lanzamiento
Se recomienda usar el script `launcher.sh` para una ejecución rápida:

```bash
# Ejecución estándar (GUI, 80x120)
./launcher.sh

# Ejecución en modo consola
./launcher.sh --mode console

# Configuración personalizada
./launcher.sh --rows 100 --cols 150 --cell-size 8
```

### Controles en modo GUI
- **Clic Izquierdo + Arrastrar**: Pinta celdas vivas (edad 1) en tiempo real.
- **Clic Derecho + Arrastrar**: Borra celdas de la cuadrícula.
- **Barra Espaciadora**: Pausa o reanuda la simulación.
- **Tecla R**: Resetea la cuadrícula y pone el contador de generaciones a cero.
- **Cerrar ventana**: Finaliza el proceso de forma segura.

## 6. Ejecución de Tests
Para asegurar que los cambios no rompen la lógica del juego:
```bash
python3 -m unittest discover tests
```
