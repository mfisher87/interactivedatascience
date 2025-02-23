from dataclasses import dataclass

from tutorial3.screen import WIDTH, HEIGHT

# In pixels:
BALL_DIAMETER = 8
COLLISION_THRESHOLD = 40


@dataclass
class Ball:
    # In pixels:
    position_x: int
    position_y: int
    
    # In pixels / second:
    velocity_x: int
    velocity_y: int

    def update(self, duration, mouse_x: int, mouse_y: int):
        self.position_x = self.position_x + self.velocity_x * duration
        self.position_y = self.position_y + self.velocity_y * duration

        # Bounce off the walls
        if self.position_x > WIDTH:
            self.position_x = WIDTH
            self._reverse_x()
        elif self.position_x < 0:
            self.position_x = 0
            self._reverse_x()

        # Bounce off the floor and ceiling
        if self.position_y > HEIGHT:
            self.position_y = HEIGHT
            self._reverse_y()
        elif self.position_y < 0:
            self.position_y = 0
            self._reverse_y()

        # Bounce off the mouse
        if self._is_near_mouse(mouse_x=mouse_x, mouse_y=mouse_y):
            if self._is_hit_mouse_in_axis(
                coordinate=self.position_x,
                mouse_coordinate=mouse_x,
                velocity=self.velocity_x
            ):
                self._reverse_x()

            if self._is_hit_mouse_in_axis(
                coordinate=self.position_y,
                mouse_coordinate=mouse_y,
                velocity=self.velocity_y
            ):
                self._reverse_y()

    def _reverse_x(self) -> None:
        self.velocity_x = self.velocity_x * -1

    def _reverse_y(self) -> None:
        self.velocity_y = self.velocity_y * -1

    def _is_near_mouse(self, *, mouse_x: int, mouse_y: int) -> bool:
        x_near = abs(mouse_x - self.position_x) < COLLISION_THRESHOLD
        y_near = abs(mouse_y - self.position_y) < COLLISION_THRESHOLD
        return x_near and y_near
    
    def _is_hit_mouse_in_axis(
        self,
        *,
        coordinate: int,
        mouse_coordinate: int,
        velocity: float,
    ) -> bool:
        if mouse_coordinate > coordinate and velocity > 0:
            distance = mouse_coordinate - coordinate
            return distance < COLLISION_THRESHOLD
        elif mouse_coordinate < coordinate and velocity < 0:
            distance = mouse_coordinate - coordinate
            return distance > -COLLISION_THRESHOLD
        else:
            return False
