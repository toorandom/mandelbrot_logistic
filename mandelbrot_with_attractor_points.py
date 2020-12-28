# This code will show you where the "chaos" is in the Mandelbrot set
# the idea is to extract the Logistic map from the set.
#
# This is a very basic, slow, and bad quality mandelbrot set calculator
# with the purpose to show the attractor points from mandelbrot recursion
# instead of only the points c where the equation  z = z^2 + c  does not diverge.

# The idea is to plot in the XY axis the usual points c in the mandelbrot set (complex plane)
# where z=z^2 + c does not diverge where iterated, and in the Z axis the limit points (attractors)
# for that c. 

# This is a lame implementation and the attractors are calculated by looking for cycles
# after rounding the whole orbit, so is not too precise.

# Wanna see this stuff in 3D?  (need gnuplot)
# python mandelbrot_with_attractor_points.py | gnuplot -p -e "splot '<cat' u 1:2:3 w d;pause 300"
#
# Eduardo Ruiz Duarte
# toorandom@gmail.com

maxorbitsize = 800
def mandelbrot(c):
    z = 0
    n = 0
    l = []
    while abs(z) <= 2 and n < maxorbitsize:
        z = z*z + c
        n += 1
        if n>maxorbitsize-10:
            l.append(complex(round(z.real,6),round(z.imag,6)))
    return list(set(l)),n
Xaxis =  300
Yaxis = 200
realinit = -2
realend = 1
imstart = -1
imend = 1
for x in range(0, Xaxis):
    for y in range(0, Yaxis):
        c = complex(realinit + (x / Xaxis) * (realend - realinit),
                    imstart + (y / Yaxis) * (imend - imstart))
        l,m = mandelbrot(c)
        color = 255 - int(m * 255 / maxorbitsize)
        for z in l:
            print(x,y,z.real,z.imag,color,m)
