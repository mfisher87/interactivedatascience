import sketchingpy

from tutorial4.screen import WIDTH, HEIGHT


def line(sketch: sketchingpy.Sketch2D) -> None:
    sketch.draw_line(
        230 * 4,
        270 * 4,
        270 * 4,
        270 * 4,
    )

def lines(sketch: sketchingpy.Sketch2D) -> None:
    shape = sketch.start_shape(230 * 4, 270 * 4)
    shape.add_line_to(270 * 4, 270 * 4)
    shape.add_line_to(250 * 4, 230 * 4)
    shape.end()
    sketch.draw_shape(shape)
