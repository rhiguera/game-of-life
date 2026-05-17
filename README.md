# 🧬 Game of Life - Aging Cells

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by Pygame](https://img.shields.io/badge/Powered%20by-Pygame-green.svg)](https://www.pygame.org/)

Una implementación moderna, modular y visualmente atractiva del Juego de la Vida de Conway, desarrollada en Python. Esta versión introduce un **sistema de envejecimiento dinámico** donde las celdas cambian su color basándose en su longevidad.

---

## ✨ Características Principales

*   **🎨 Gradiente de Envejecimiento**: Las celdas nacen con un verde brillante y evolucionan hacia un azul profundo conforme sobreviven generaciones.
*   **🕹️ Interfaz Dual**: Elige entre una experiencia gráfica rica con **Pygame** o una interfaz minimalista de **consola**.
*   **🖱️ Interactividad Total**: Dibuja tus propios patrones en tiempo real haciendo clic en la cuadrícula.
*   **🏗️ Arquitectura Robusta**: Código modular con separación clara entre lógica de simulación y capas de presentación.
*   **🧪 Testeado**: Suite de pruebas unitarias para garantizar la fidelidad de las reglas de Conway.

---

## 🚀 Instalación Rápida

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/rhiguera/game-of-life.git
   cd game-of-life
   ```

2. **Configurar el entorno**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## 🛠️ Uso

### Método Recomendado (Launcher)
Hemos incluido un script de conveniencia que gestiona el entorno virtual por ti:

```bash
# Iniciar GUI (Modo por defecto)
./launcher.sh

# Iniciar en modo Terminal
./launcher.sh --mode console

# Configuración personalizada (ej. rejilla más grande)
./launcher.sh --rows 50 --cols 80
```

### Controles de la GUI
*   **Barra Espaciadora**: Pausar / Reanudar la simulación.
*   **Clic Izquierdo**: Alternar estado de una celda (viva/muerta).
*   **R**: Reiniciar la cuadrícula (borrar todo).
*   **ESC / Cerrar ventana**: Salir de la aplicación.

---

## 📁 Estructura del Proyecto

*   `core/`: El "motor" del juego. Lógica de celdas y reglas de evolución.
*   `ui/`: Capas de visualización (Pygame y Consola).
*   `tests/`: Pruebas automatizadas.
*   `launcher.sh`: Script de ejecución rápida.
*   `DOCUMENTATION.md`: Documentación técnica detallada.

---

## 🧪 Pruebas Unitarias

Para verificar que todo funciona correctamente, ejecuta:
```bash
python3 -m unittest discover tests
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` (próximamente) para más detalles.

---
Desarrollado con ❤️ para aprendizaje y experimentación.
