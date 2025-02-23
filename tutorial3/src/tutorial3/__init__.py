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

    @property
    def balls(self):
        return self._balls


    def update(self, mouse_x, mouse_y):
        new_time = time.time()
        duration = new_time - self._last_time
        self._last_time = new_time

        for ball in self._balls:
            ball.update(duration, mouse_x, mouse_y)


def main():
    sketch = sketchingpy.Sketch2D(WIDTH, HEIGHT)
    simulation = Simulation()

    def update_and_draw_balls(self):
        mouse = sketch.get_mouse()
        mouse_x = mouse.get_pointer_x()
        mouse_y = mouse.get_pointer_y()

        simulation.update(mouse_x, mouse_y)

        for ball in simulation.balls:
            sketch.draw_ellipse(
                ball.position_x,
                ball.position_y,
                BALL_DIAMETER,
                BALL_DIAMETER,
            )

    sketch.on_step(update_and_draw_balls)
    sketch.show()


if __name__ == "__main__":
    main()
