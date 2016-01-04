from __future__ import division
import png
import math


width = 1600
length = 1200
MAXITER = 50

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
    zoom = 300;
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
        z2 = z1 * z1 * z1 + z0 * z0 + c
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

def gen_palette():
    r, g, b = 24, 16, 0
    for i in xrange(256):
        palette.append((r, g, b))
        if i < 64:
            r += 3
        elif i < 128:
            g += 3
        elif i < 192:
            b += 3

def main():
    f = open('fractal.png', 'wb')
    w = png.Writer(width, length)
    # w = png.Writer(800, 600)

    gen_palette()
    gen_image()
    w.write(f, img)
    f.close()

main()
