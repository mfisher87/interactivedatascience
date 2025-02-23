import sketchingpy

from tutorial4.screen import WIDTH, HEIGHT


def arc_center(sketch: sketchingpy.Sketch2D) -> None:
    sketch.set_ellipse_mode('radius')
    sketch.set_angle_mode('degrees')
    sketch.draw_arc(WIDTH / 2, HEIGHT / 2, 160, 160, -90, 180)
