from dataclasses import dataclass
import time

import sketchingpy

from tutorial3.ball import Ball, BALL_DIAMETER
from tutorial3.screen import WIDTH, HEIGHT


@dataclass
class Simulation:
    def __init__(self):
        self._balls = [
            Ball(WIDTH / 2, HEIGHT / 2, -40, -40),
            Ball(WIDTH / 2, HEIGHT / 2, -40, 40),
            Ball(WIDTH / 2, HEIGHT / 2, 40, 10)
        ]
        self._last_time = time.time()

    def update(self, sketch_step):
        mouse = sketch_step.get_mouse()
        mouse_x = mouse.get_pointer_x()
        mouse_y = mouse.get_pointer_y()

        self._update_balls(mouse_x, mouse_y)

        for ball in self._balls:
            sketch_step.draw_ellipse(
                ball.position_x,
                ball.position_y,
                BALL_DIAMETER,
                BALL_DIAMETER,
            )

    def _update_balls(self, mouse_x, mouse_y):
        new_time = time.time()
        duration = new_time - self._last_time
        self._last_time = new_time

        for ball in self._balls:
            ball.update(duration, mouse_x, mouse_y)


def main():
    sketch = sketchingpy.Sketch2D(WIDTH, HEIGHT)
    simulation = Simulation()

    sketch.on_step(simulation.update)
    sketch.show()


if __name__ == "__main__":
    main()
