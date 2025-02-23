import sketchingpy


def draw_circles(*, sketch: sketchingpy.Sketch2D, y: int):
    sketch.set_stroke("#000000")

    sketch.set_fill("#edf8fb")
    sketch.draw_ellipse(150, y, 20, 20)

    sketch.set_fill("#b2e2e2")
    sketch.draw_ellipse(200, y, 20, 20)

    sketch.set_fill("#66c2a4")
    sketch.draw_ellipse(250, y, 20, 20)

    sketch.set_fill("#2ca25f")
    sketch.draw_ellipse(300, y, 20, 20)

    sketch.set_fill("#006d2c")
    sketch.draw_ellipse(350, y, 20, 20)


def main() -> None:
    sketch = sketchingpy.Sketch2D(500, 500)
    # sketch.set_stroke_weight(0)  # Makes it harder to see the circles

    sketch.clear('#FFFFFF')
    sketch.set_ellipse_mode("radius")

    draw_circles(sketch=sketch, y=125)

    sketch.set_rect_mode("corner")
    sketch.clear_stroke()
    sketch.set_fill("#555555")
    sketch.draw_rect(0, 250, 500, 250)

    draw_circles(sketch=sketch, y=375)

    sketch.show()


if __name__ == "__main__":
    main()
