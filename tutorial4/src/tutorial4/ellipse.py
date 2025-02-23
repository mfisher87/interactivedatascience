import sketchingpy

from tutorial4.screen import WIDTH, HEIGHT

def ellipse_center(sketch: sketchingpy.Sketch2D) -> None:
    sketch.set_ellipse_mode('radius')
    sketch.draw_ellipse(WIDTH / 2, HEIGHT / 2, 80, 80)


def ellipse_modes(sketch: sketchingpy.Sketch2D) -> None:
    params = (1000, 1000, 80, 40)
    modes_colors = (
        ("corners", "red"),
        ("radius", "yellow"),
        ("center", "green"),
        ("corner", "blue")
    )

    for mode, color in modes_colors:
        sketch.set_ellipse_mode(mode)
        sketch.set_fill(color)
        sketch.draw_ellipse(*params)
