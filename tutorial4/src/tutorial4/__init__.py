import sketchingpy

from tutorial4.arc import arc_center
from tutorial4.curve import curve 
from tutorial4.ellipse import ellipse_center, ellipse_modes
from tutorial4.line import line, lines
from tutorial4.rectangle import rect, rect_modes
from tutorial4.screen import WIDTH, HEIGHT
from tutorial4.shape import shape


def main() -> None:
    sketch = sketchingpy.Sketch2D(WIDTH, HEIGHT)
    sketch.set_stroke_weight(4)
    sketch.set_stroke("#ffffff")

    shape(sketch)

    sketch.show()


if __name__ == "__main__":
    main()
