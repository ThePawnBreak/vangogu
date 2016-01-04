from __future__ import division
import png
import math
from random import randint as rint

width = 1600
length = 1200
MAXITER = rint(280, 520)

img = [[0, 0, 0] * width for row in xrange(length)]
palette = []

def gen_image():
    for y in xrange(length):
        for x in xrange(width):
            r, g, b = compute_val(x, y)
            img[y][x * 3] = r
            img[y][x * 3 + 1] = g
            img[y][x * 3 + 2] = b

def compute_val(x, y):
    a, b, rx, ry = 0, 0, 0, 0

    offsetx = -width/2;
    offsety = -length/2;
    panx = -100;
    pany = 0;
    zoom = 3000;
    x0 = (x + offsetx + panx) / zoom;
    y0 = (y + offsety + pany) / zoom;

    iters = 0

    c = x0 + 1j * y0
    z0 = c
    z1 = z0 * z0 + c
    z1 = 0

    # while (iters < MAXITER and (rx * rx + ry * ry <= 2)):
    while (iters < MAXITER and (z0.real * z0.real + z0.imag * z0.imag <= 2)):
        # rx = a * a - b * b + x0
        # ry = 2 * a * b + y0
        # a = rx
        # b = ry
        z2 = z1 * z1 * z1 + z0 + c
        z0 = z1
        z1 = z2
        

        # z1 = z0 * z0 * z0 + c
        # z0 = z1

        
        iters += 1


    if iters is MAXITER:
        return 0, 0, 0
    else:
        proc = iters / (MAXITER - 1)
        index = int(math.floor(proc * 255))
        return palette[index]

def floorToMax(nr, maxNr):
    rez = int(nr)
    if rez > maxNr:
        rez = maxNr
    return rez

def gen_palette(colorNr = 2):
    interval = 256 / colorNr
    r, g, b = 0, 0, 0

    for x in xrange(colorNr):
        dr = (rint(0,255) - r) / interval
        dg = (rint(0,255) - g) / interval
        db = (rint(0,255) - b) / interval

        start = x * int(interval)
        end = (x + 1) * int(interval)
        if x == (colorNr - 1):
            end = 256
        for i in xrange(start, end):
            r,g,b = r+dr, g+dg, b+db
            palette.append((floorToMax(r, 255),floorToMax(g, 255),floorToMax(b, 255)))

def main():
    f = open('fractal.png', 'wb')
    w = png.Writer(width, length)
    # w = png.Writer(800, 600)

    gen_palette(5)
    gen_image()
    w.write(f, img)
    f.close()

main()
