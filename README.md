# mandelbrot_logistic
## Shows the chaos behind mandelbrot set by calculating attractor cycle points in each point orbit.

This code will show you where the "chaos" is in the Mandelbrot set
the idea is to extract the Logistic map from the set.

This is a very basic, slow, and bad quality mandelbrot set calculator
with the purpose to show the attractor points from mandelbrot recursion
instead of only the points c where the equation  _z = z^2 + c_  does not diverge.

The idea is to plot in the XY axis the usual points c in the mandelbrot set (complex plane)
where z=z^2 + c does not diverge where iterated, and in the Z axis the limit points (attractors)
for that c. 

This is a lame implementation and the attractors are calculated by looking for cycles
after rounding the whole orbit, so is not too precise.

**Wanna see this stuff in 3D?  (need gnuplot)**
```
$ python< mandelbrot_with_attractor_points.py | gnuplot -p -e "splot '<cat' u 1:2:3 w d;pause 300"
```

 Eduardo Ruiz Duarte
 toorandom@gmail.com

