from math import exp, log, sqrt, cos, sin, asin, pi


class Stone:
    diameter = 1
    f = 0.05

    def __init__(self, initial_y: float):
        self.x_position = 0
        self.y_position = initial_y

    def __repr__(self):
        return f"<Stone{{x:{self.x_position}, y:{self.y_position}}}>"

    def do_push(self, v: float, angle_to_x_axis: float = 0):
        if v == 0:
            return
        elif v < 0:
            raise ValueError
        time_when_stops = (log(v) + 100) / self.f
        distance_travelled_along_line = (v / self.f) * (1 - exp(-self.f * time_when_stops))
        if angle_to_x_axis == 0:
            self.x_position += distance_travelled_along_line
        else:
            x_distance_travelled = distance_travelled_along_line * cos(angle_to_x_axis)
            y_distance_travelled = distance_travelled_along_line * sin(angle_to_x_axis)

            self.x_position += x_distance_travelled
            self.y_position += y_distance_travelled


class Curling:
    target_x_position = 30
    target_width = 10

    def __init__(self):
        self.first_stone = None
        self.second_stone = None

        self.first_stone_v = None
        self.second_stone_v = None

    def __repr__(self):
        return f"<Curling>"

    def push_first_stone(self):
        self.first_stone.do_push(self.first_stone_v)

    def push_second_stone(self):
        self.second_stone.do_push(self.second_stone_v)

    def stones_y_difference(self):
        return self.second_stone.y_position - self.first_stone.y_position

    def check_stones_collided(self):
        difference_in_y = abs(self.stones_y_difference())
        if difference_in_y < Stone.diameter:
            will_collide_at_x = self.first_stone.x_position - sqrt((Stone.diameter ** 2) - (difference_in_y ** 2))
            if self.second_stone.x_position >= will_collide_at_x:
                self.second_stone.x_position = will_collide_at_x
                return True
        return False

    def get_second_stone_v_from_x_during_first_push(self):
        try:
            time_of_x_displacement = -(log(1 - ((Stone.f * self.second_stone.x_position) / self.second_stone_v)) / Stone.f)
        except ValueError:
            raise ValueError("Expected collision, could not find correct t for second stone displacement.")

        velocity_at_that_time = exp(-Stone.f * time_of_x_displacement) * self.second_stone_v
        return velocity_at_that_time

    def do_collision_pushes(self):
        difference_in_y = -self.stones_y_difference()
        first_stone_velocity_angle = asin(difference_in_y / Stone.diameter)
        if first_stone_velocity_angle < 0:
            second_stone_velocity_angle = first_stone_velocity_angle + pi/2
        elif first_stone_velocity_angle > 0:
            second_stone_velocity_angle = first_stone_velocity_angle - pi/2
        else:
            second_stone_velocity_angle = 0

        velocity_of_second_stone_at_collision = self.get_second_stone_v_from_x_during_first_push()

        first_stone_velocity_magnitude = abs(cos(first_stone_velocity_angle)) * velocity_of_second_stone_at_collision
        second_stone_velocity_magnitude = abs(sin(first_stone_velocity_angle)) * velocity_of_second_stone_at_collision

        self.first_stone.do_push(first_stone_velocity_magnitude, first_stone_velocity_angle)
        self.second_stone.do_push(second_stone_velocity_magnitude, second_stone_velocity_angle)

    def push_stones(self, v1, y1, v2, y2):
        self.first_stone = Stone(y1)
        self.second_stone = Stone(y2)

        self.first_stone_v = v1
        self.second_stone_v = v2

        self.push_first_stone()
        self.push_second_stone()

        print(self.first_stone.x_position, self.first_stone.y_position)
        print(self.second_stone.x_position, self.second_stone.y_position)

        if self.check_stones_collided():
            self.do_collision_pushes()

        print(self.first_stone.x_position, self.first_stone.y_position)
        print(self.second_stone.x_position, self.second_stone.y_position)

        first_stone_distance = self.get_stone_distance_to_target(self.first_stone)
        second_stone_distance = self.get_stone_distance_to_target(self.second_stone)

        print(first_stone_distance, second_stone_distance)

        if first_stone_distance is None and second_stone_distance is None:
            return -1
        elif first_stone_distance is None and second_stone_distance is not None:
            return second_stone_distance
        elif first_stone_distance is not None and second_stone_distance is None:
            return first_stone_distance
        elif first_stone_distance <= second_stone_distance:
            return first_stone_distance
        else:
            return second_stone_distance

    @staticmethod
    def get_stone_distance_to_target(stone: Stone):
        if stone.x_position is None or stone.y_position is None:
            return None

        x_difference = stone.x_position - Curling.target_x_position
        y_difference = stone.y_position
        distance_from_stone_to_target = round(sqrt(x_difference ** 2 + y_difference ** 2), 2)
        disqualify_difference = (Curling.target_width/2) - (Stone.diameter/2)
        if abs(x_difference) > disqualify_difference:
            return None
        elif abs(y_difference) > disqualify_difference:
            return None

        return distance_from_stone_to_target
