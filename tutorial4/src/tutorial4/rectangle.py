import sketchingpy

from tutorial4.screen import WIDTH, HEIGHT


def rect(sketch: sketchingpy.Sketch2D) -> None:
    sketch.set_rect_mode('radius')
    sketch.draw_rect(
        WIDTH / 2,
        HEIGHT / 2,
        80,
        80,
    )


def rect_modes(sketch: sketchingpy.Sketch2D) -> None:
    rect_params = (1000, 1000, 80, 40)
    modes_colors = (
        ("corners", "red"),
        ("radius", "yellow"),
        ("center", "green"),
        ("corner", "blue")
    )

    for mode, color in modes_colors:
        sketch.set_rect_mode(mode)
        sketch.set_fill(color)
        sketch.draw_rect(*rect_params)
