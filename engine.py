"""
 engine.py by Thomas on 8/22/2021
"""

from color import Color
from image import Image
from point import Point
from ray import Ray


class RenderEngine:
    """Renders 3D objects into 2D objects using ray tracing"""

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                ray = Ray(camera, Point(x, y) - camera)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))
            print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")
        return pixels

    def ray_trace(self, ray, scene):
        color = Color(0, 0, 0)
        # Find the nearest object hit by the ray in the scene
        distance_hit, object_hit = self.find_nearest(ray, scene)
        if object_hit is None:
            return color
        hit_position = ray.origin + ray.direction * distance_hit
        hit_normal = object_hit.normal(hit_position)
        color += self.color_at(object_hit, hit_position, hit_normal, scene)
        return color

    def find_nearest(self, ray, scene):
        distance_min = None
        object_hit = None
        for obj in scene.objects:
            distance = obj.intersects(ray)
            if distance is not None and (object_hit is None or distance < distance_min):
                distance_min = distance
                object_hit = obj
        return distance_min, object_hit

    def color_at(self, obj_hit, hit_position, normal, scene):
        material = obj_hit.material
        object_color = material.color_at(hit_position)
        to_camera = scene.camera - hit_position
        specular_S = 50
        color = material.ambient * Color.from_hex("#000000")
        # Light calculations
        for light in scene.lights:
            to_light = Ray(hit_position, light.position - hit_position)
            # Diffuse Shading (Lambert)
            color += (
                    object_color
                    * material.diffuse
                    * max(normal.dot_product(to_light.direction), 0)
            )
            # Specular Shading (Blinn-Phong)
            half_vector = (to_light.direction + to_camera).normalize()
            color += (
                    light.color
                    * material.specular
                    * max(normal.dot_product(half_vector), 0) ** specular_S
            )
        return color
