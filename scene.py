"""
 scene.py by Thomas on 8/22/2021
"""


class Scene:
    """Scene has all the information needed for the ray tracing engine"""

    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
        self.lights = lights
