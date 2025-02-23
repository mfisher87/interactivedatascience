import sketchingpy


def curve(sketch: sketchingpy.Sketch2D) -> None:
    shape = sketch.start_shape(230 * 4, 270 * 4)
    shape.add_line_to(270 * 4, 270 * 4)
    shape.add_bezier_to(280 * 4, 250 * 4, 250 * 4, 230 * 4, 270 * 4, 210 * 4)
    shape.end()
    sketch.draw_shape(shape)
