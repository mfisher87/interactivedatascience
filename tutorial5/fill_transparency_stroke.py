import sketchingpy


def main():
    sketch = sketchingpy.Sketch2D(500, 500)

    sketch.set_stroke("#1f78b4")
    sketch.set_stroke_weight(6)
    sketch.clear_fill()
    sketch.draw_ellipse(150, 250, 100, 100)

    sketch.set_fill("#C0C0C0")
    sketch.clear_stroke()
    sketch.draw_ellipse(250, 250, 100, 100)

    sketch.set_stroke("#33a02c")
    sketch.set_stroke_weight(1)
    sketch.set_fill("#b2df8a99")
    sketch.draw_ellipse(350, 250, 100, 100)

    sketch.show()


if __name__ == "__main__":
    main()
