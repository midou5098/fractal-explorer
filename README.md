# Fractal Explorer

An interactive Pygame fractal viewer for exploring Mandelbrot and Julia sets. The renderer uses NumPy arrays for fast escape-time calculation and converts the result into a Pygame surface for display.

## Features

- Mandelbrot set rendering.
- Julia set rendering with a time-varying constant.
- NumPy-based vectorized fractal calculation.
- Interactive panning with arrow keys.
- Mouse zoom in/out.
- Menu screen for choosing the active fractal family.
- Color-table based rendering for clear escape-time bands.

## Tech Stack

- Python
- Pygame
- NumPy

## Project Structure

```text
.
|-- app.py           # Main Pygame application and interaction loop
|-- source.py        # Button class, Mandelbrot/Julia calculations, rendering helpers
|-- requirements.txt # Python dependency list
|-- font.ttf         # Optional UI font
`-- __pycache__/     # Generated Python cache files
```

## Install

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install pygame numpy
```

If `requirements.txt` is populated in your copy, you can use:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Controls

| Input | Action |
| --- | --- |
| Mandelbrot button | Select Mandelbrot mode. |
| Julia button | Select Julia mode. |
| Start button | Render the selected fractal. |
| Arrow keys | Pan the viewport. |
| Left mouse click | Zoom in. |
| Right mouse click | Zoom out. |
| Window close | Quit. |

## How It Works

`source.py` builds a complex plane from the current viewport bounds using `numpy.linspace()` and `numpy.meshgrid()`. It then iterates the escape-time formula over the full array instead of calling a Python function for every pixel.

The result is reduced to color indexes, mapped through a small RGB color table, transposed into Pygame's surface layout, and blitted to the screen.

## Current Limitations

- Rendering is synchronous, so large iteration counts can pause the UI while the frame is generated.
- The menu and controls are intentionally minimal.
- There is no screenshot/export feature yet.
