import sketchingpy

from tutorial6.transform import transform

WIDTH, HEIGHT = (2000, 2000)


def main() -> None:
    sketch = sketchingpy.Sketch2D(WIDTH, HEIGHT)

    transform(sketch)

    sketch.show()


if __name__ == "__main__":
    main()
