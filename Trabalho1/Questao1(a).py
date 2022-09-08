#!/usr/bin/env python

import math
import cairo

def arrow(context, x, y, width, height, a, b): 
    context.move_to(x, y + b) 
    context.line_to(x, y + height - b) 
    context.line_to(x + a, y + height - b) 
    context.line_to(x + a, y + height) 
    context.line_to(x + width, y + height/2) 
    context.line_to(x + a, y) 
    context.line_to(x + a, y + b) 
    context.close_path() 

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 700, 700)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas


ctx.translate(1, 1)  # Changing the current transformation matrix

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity

"=======================triangulo============================="
ctx.move_to(0, 0)
ctx.line_to(0.5, 0.0)  # Line to (x,y)
ctx.line_to(0.25, -0.4)
ctx.close_path()
ctx.set_source_rgb(0.0, 0.8, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.fill()
ctx.stroke()

"=======================retangulo============================="
ctx.move_to(1, 1)
ctx.line_to(0.5, 1.0)  # Line to (x,y)
ctx.line_to(0.5, 0.6)
ctx.line_to(1, 0.6)
ctx.close_path()
ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.fill()
ctx.stroke()
"=======================circulo============================="
ctx.arc(-0.4,0.3,0.3,0.9,0.8)
ctx.close_path()
ctx.set_source_rgb(0.3, 0.2, 0.0)  # Solid color
ctx.set_line_width(0.02)
ctx.fill()
ctx.stroke()

"=======================seta================================"
ctx.set_source_rgb(0, 0, 0.5) 
arrow(ctx, 0.7, -0.7, 1, 1, 0.5, 0.3)    
ctx.fill()
ctx.stroke()
surface.write_to_png("example.png")  # Output to PNG