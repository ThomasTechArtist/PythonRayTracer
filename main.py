#!/usr/bin/env python
"""Python Ray Tracer"""

from color import Color
from engine import RenderEngine
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector
from light import Light
from material import Material



def main():
    WIDTH = 640
    HEIGHT = 360
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(-0.4, 0, 1), 0.5, Material(Color.from_hex("#FF0000"))),
               Sphere(Point(0.4, 0, 1), 0.5, Material(Color.from_hex("#0000FF")))]
    lights = [Light(Point(2, -3, -10.0), Color.from_hex("#FFFFFF"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("test04.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
