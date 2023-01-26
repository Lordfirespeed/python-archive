from random import randrange, choice
from threading import Thread, Lock


class MontyHallGame:
    true_or_false = (True, False)

    def __init__(self):
        self.prize_door = None
        self.first_selected_door = None
        self.revealed_door = None
        self.final_selected_door = None
        self.switched_selected_door = None
        self.won_prize = None

    def simulate(self):
        self.prize_door = randrange(1, 4)
        self.first_selected_door = randrange(1, 4)

        revealable_doors = {1, 2, 3}
        revealable_doors.discard(self.prize_door)
        revealable_doors.discard(self.first_selected_door)

        self.revealed_door = choice(list(revealable_doors))

        pickable_doors = {1, 2, 3}
        pickable_doors.discard(self.revealed_door)

        self.final_selected_door = choice(list(pickable_doors))
        self.switched_selected_door = self.first_selected_door != self.final_selected_door

        self.won_prize = self.final_selected_door == self.prize_door


class MassMontyHallGameSimulator:
    def __init__(self, number_games_to_simulate, number_threads_to_use):
        self.sample_size = number_games_to_simulate
        self.number_threads = number_threads_to_use
        self.simulated_games_stack = []
        self.simulate_games_stack_lock = Lock()
        self.threads = []
        self.create_threads()

    def create_threads(self):
        for thread_index in range(self.number_threads):
            new_thread = Thread(target=self.thread_task)
            self.threads.append(new_thread)

    def start_threads(self):
        [thread.start() for thread in self.threads]

    def thread_task(self):
        while len(self.simulated_games_stack) < self.sample_size:
            new_game = MontyHallGame()
            new_game.simulate()

            with self.simulate_games_stack_lock:
                self.simulated_games_stack.append(new_game)

    def join_threads(self):
        [thread.join() for thread in self.threads]


def main():
    sample_size = 1000000
    number_threads = 25

    mass_simulator = MassMontyHallGameSimulator(sample_size, number_threads)
    mass_simulator.start_threads()
    mass_simulator.join_threads()

    games_where_switched = [game for game in mass_simulator.simulated_games_stack if game.switched_selected_door]
    games_where_won_given_switched = [game for game in games_where_switched if game.won_prize]
    probability_of_win_given_switch = len(games_where_won_given_switched) / len(games_where_switched)
    print(f"Likelihood of winning given switch, sample size {mass_simulator.sample_size:,}: {probability_of_win_given_switch:.2%}")


if __name__ == "__main__":
    main()
