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
- **Core (Modelo)**: Contiene el estado de la simulación y las leyes físicas (reglas de Conway). No conoce nada de la interfaz.
- **UI (Vista/Controlador)**: Se encarga de representar el estado del `Grid` y capturar la entrada del usuario para modificarlo.
- **Main (Orquestador)**: Configura la aplicación basándose en los parámetros de la línea de comandos e inicializa el bucle principal.

## 3. Estructura de Directorios y Ficheros

```text
game-of-life/
├── core/
│   ├── __init__.py
│   └── grid.py         # Clase Grid: Lógica de evolución y seguimiento de edad.
├── ui/
│   ├── __init__.py
│   ├── interface.py    # Clase base abstracta BaseUI.
│   ├── console_view.py # Implementación CLI para terminal.
│   └── pygame_view.py  # Implementación GUI con Pygame.
├── tests/
│   ├── __init__.py
│   └── test_grid.py    # Tests unitarios de la lógica central.
├── main.py             # Punto de entrada y gestión de argumentos CLI.
├── README.md           # Guía rápida de inicio.
├── DOCUMENTATION.md    # Esta documentación detallada.
├── PLAN.md             # Plan de diseño inicial.
├── requirements.txt    # Dependencias del proyecto.
└── .gitignore          # Archivos excluidos de Git.
```

## 4. Lógica de Envejecimiento

A diferencia de la implementación estándar, cada celda no solo está "viva" o "muerta". Si está viva, almacena un número entero que representa su **edad** (generaciones consecutivas sobreviviendo).

- **Nacimiento**: Valor inicial = 1.
- **Supervivencia**: Valor = Valor anterior + 1.
- **Muerte**: Valor = 0.

### Representación Visual
En `PygameUI`, el color se calcula dinámicamente:
- **Edad 1**: Verde Brillante `(0, 255, 100)`.
- **Edad 10+**: Azul Profundo `(0, 50, 200)`.
- Las edades intermedias se calculan mediante interpolación lineal de colores.

## 5. Uso de la Aplicación

### Instalación de dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Lanzamiento
Se recomienda usar el script `launcher.sh` para una ejecución rápida sin gestionar el entorno virtual manualmente:

```bash
# Ejecución estándar (GUI)
./launcher.sh

# Ejecución en modo consola
./launcher.sh --mode console

# Personalizar tamaño de cuadrícula
./launcher.sh --rows 50 --cols 80 --cell-size 10
```

También es posible la ejecución manual:

### Controles en modo GUI
- **Mouse Click**: Cambia el estado de una celda manualmente.
- **Barra Espaciadora**: Pausa o reanuda la simulación.
- **Tecla R**: Resetea la cuadrícula (todas las celdas a 0).
- **Cerrar ventana**: Finaliza el proceso.

## 6. Ejecución de Tests
Para asegurar que los cambios no rompen la lógica del juego:
```bash
python3 -m unittest discover tests
```
