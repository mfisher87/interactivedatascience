import sketchingpy


def transform(sketch: sketchingpy.Sketch2D) -> None:
    sketch.set_ellipse_mode("radius")

    sketch.draw_ellipse(0, 0, 100, 100)
    sketch.translate(800, 800)

    sketch.set_fill("blue")
    sketch.draw_ellipse(0, 0, 40, 40)

    sketch.translate(400, 400)

    sketch.set_fill("green")
    sketch.draw_ellipse(0, 0, 80, 80)

    sketch.push_transform()
    sketch.translate(200, 0)
    sketch.translate(200, 0)

    sketch.set_fill("yellow")
    sketch.draw_ellipse(0, 0, 160, 160)

    sketch.pop_transform()
    sketch.translate(200, 200)

    sketch.set_fill("red")
    sketch.draw_ellipse(0, 0, 320, 320)
