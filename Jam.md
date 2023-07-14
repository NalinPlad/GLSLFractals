# GLSL Fractals
Time estimate: 60 minutes

![[Mandlebrot.png]]

You may have seen or heard of fractals. Even if you haven't, you've probably seen an hour long video of someone zooming into a picture, revealing more and more detail the farther they go.

![[Zoom.gif]]

Well this particular geometrical shape shown in the GIF is part of a large family of *infinitely* detailed, *infinitely* precise object, called **fractals**. Today, we are going to write a computer program that will allow us to create the same fractal you see in the images above, namely, the ***Mandelbrot set***

## What is the Mandelbrot set?
Fractals come in many varieties, some very interesting and some very boring. Lets look at the simplest fractals for example.

Lets imagine creating a tree. We start by placing one trunk in the ground.

![[gen1.jpeg|200]]

Now lets imagine that this tree splits into two branches

![[gen2.jpeg|200]]

And then splitting each of these branches into two additional branches, and so on and so on, splitting each new branch into two identical branches

![[gen3.jpeg|300]]

![[gen4.jpeg|300]]

![[gen5.jpeg|400]]

And you can imagine this process continuing onto infinity, leaving a tree with infinitely many branches.

At this point we can notice something very interesting. If you focus on only the first green branch, you can see that if you rotate it by 45 degrees, you are left with our original drawing. This property is called ***Self Similarity*

![[pano.jpeg]]