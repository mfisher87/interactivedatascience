import sketchingpy
import time


def main():
    width, height = (2000, 1600)
    sketch = sketchingpy.Sketch2D(width, height)

    center_x = width / 2
    center_y = height / 2
    end_x = 100
    end_y = 50
    sketch.draw_line(center_x, center_y, end_x, end_y)

    def draw_moving_line(self):
        mouse = sketch.get_mouse()
        sketch.draw_line(center_x, center_y, mouse.get_pointer_x(), mouse.get_pointer_y())

    sketch.on_step(draw_moving_line)

    sketch.show()


if __name__ == "__main__":
    main()
