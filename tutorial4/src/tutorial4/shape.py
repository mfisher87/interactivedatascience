import sketchingpy

from tutorial4.screen import WIDTH, HEIGHT


def shape(sketch: sketchingpy.Sketch2D) -> None:
    sketch.set_ellipse_mode('radius')
    sketch.draw_ellipse(150 * 4, 250 * 4, 20 * 4, 20 * 4)

    shape = sketch.start_shape(230 * 4, 270 * 4)
    shape.add_line_to(270 * 4, 270 * 4)
    shape.add_line_to(250 * 4, 230 * 4)
    shape.close()
    sketch.draw_shape(shape)

    sketch.set_rect_mode('radius')
    sketch.draw_rect(350 * 4, 250 * 4, 20 * 4, 20 * 4)
