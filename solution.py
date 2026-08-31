import sys
from game_env import GameEnv
from game_state import GameState

"""
solution.py

This file is a template you should use to implement your solution.

You should implement each of the method stubs below. You may add additional methods and/or classes to this file if you 
wish. You may also create additional source files and import to this file if you wish.

COMP3702 Assignment 1 Crystal Rover Support Code

Last updated by vp 03/08/26
"""


class Solver:

    STUDENT_NAME = "Yuyang Gong" # replace with your name
    STUDENT_ID = "s4907998"  # replace with your student ID
    GITHUB_USERNAME = "49079986" # replace with your GitHub username

    def __init__(self, game_env):
        self.game_env = game_env
        self.crystals = game_env.crystal_positions
        self.launches = game_env.launch_positions
        self.min_action_cost = min(game_env.ACTION_COST.values())


    @staticmethod
    def get_testcases():
        """
        Select which testcases you wish the autograder to test you on.
        The autograder will not run any excluded testcases.
        e.g. [1, 4, 6] will only run testcases 1, 4, and 6, excluding, 2, 3, and 5.
        :return: a list containing the testcase number to run (testcases in 1-6).
        """
        return [1, 2, 3, 4, 5, 6]

    # === Uniform Cost Search ==========================================================================================
    def search_ucs(self):
        """
        Find a path which solves the environment using Uniform Cost Search (UCS).
        :return: path (list of actions, where each action is an element of GameEnv.ACTIONS)
        """
        # Simplify sorting using heapq (Source: Chat-gpt)
        import heapq
        from itertools import count

        # Step1: get the initial state of the game env
        init_state = self.game_env.get_init_state()

        frontier = []
        counter = count()

        heapq.heappush(frontier, (0, next(counter), init_state, []))  # (cost, counter, state, path)

        visited_cost = {init_state: 0}  # (state, cost)

        while frontier:

            # Find the state with the lowest cost.
            cost, _, current_state, path = heapq.heappop(frontier)
            if self.game_env.is_solved(current_state):
                return path

            # If the cost of the current state is greater than the cost recorded in visited_cost, it means there is a better path to this state, so skip it.
            if cost > visited_cost[current_state]:
                continue

            # Try all possible actions, the specific actions of which are provided by GameEnv.ACTIONS.
            for action in GameEnv.ACTIONS:
                next_state, success, error_msg = self.game_env.perform_action(current_state,action)
                if not success:
                    continue

                # If an error occurs, skip this state.
                if self.game_env.is_game_over(next_state):
                    continue

                new_cost = cost + self.game_env.ACTION_COST[action]

                # 1. I've never seen this state before; 2. I've seen this state before, but the cost is lower.
                if next_state not in visited_cost or new_cost < visited_cost[next_state]:
                    visited_cost[next_state] = new_cost
                    new_path = path + [action]
                    heapq.heappush(frontier, (new_cost, next(counter), next_state, new_path))

        return []  # Return an empty path if no solution is found

    # === A* Search ====================================================================================================
    def preprocess_heuristic(self):
        """
        Perform pre-processing (e.g. pre-computing repeatedly used values) necessary for your heuristic,
        """
        min_walk_cost_per_cell = min(self.game_env.ACTION_COST[action] for action in GameEnv.ACTIONS)

        min_boost_cost_per_cell = min(self.game_env.ACTION_COST[action] for action in GameEnv.ACTIONS if action != 'BOOST')

        min_jump_cost_per_cell = min(self.game_env.ACTION_COST[action] for action in GameEnv.ACTIONS if action != 'JUMP')

        self.min_walk_cost_per_cell = min(min_walk_cost_per_cell, min_boost_cost_per_cell, min_jump_cost_per_cell)


    def compute_heuristic(self, state):
        """
        Compute a heuristic value h(n) for the given state.
        :param state: given state (GameState object)
        :return a real number h(n)
        """
        min_cost = min(self.game_env.ACTION_COST.values())
        collected = sum(state.crystal_status)

        def dist(pos1, pos2):
            return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) * min_cost

        current = (state.row, state.col)

        if collected >= self.game_env.min_samples:
            return min(dist(current, launch) for launch in self.game_env.launch_positions)

        remaining_crystals = [
            self.game_env.crystal_positions[i]
            for i, got in enumerate(state.crystal_status)
            if not got
        ]

        return min(
            dist(current, crystal) +
            min(dist(crystal, launch) for launch in self.game_env.launch_positions)
            for crystal in remaining_crystals
        )

    def search_a_star(self):
        """
        Find a path which solves the environment using A* Search.
        Your heuristic computation must be implemented within compute_heuristic and called from this method
        If you have any expensive pre-computation you can implment it in preprocess_heuristic
        :return: path (list of actions, where each action is an element of GameEnv.ACTIONS)
        """
        import heapq
        from itertools import count

        init_state = self.game_env.get_init_state()

        frontier = []
        counter = count()

        start_h = self.compute_heuristic(init_state)
        heapq.heappush(frontier, (start_h, next(counter),0, init_state, []))

        visited_cost = {init_state: 0}  # (state, cost)

        while frontier:
            _, _, cost, current_state, path = heapq.heappop(frontier)

            if self.game_env.is_solved(current_state):
                return path

            if cost > visited_cost[current_state]:
                continue

            for action in GameEnv.ACTIONS:
                next_state, success, error_msg = self.game_env.perform_action(current_state, action)
                if not success:
                    continue

                if self.game_env.is_game_over(next_state):
                    continue

                new_cost = cost + self.game_env.ACTION_COST[action]

                if next_state not in visited_cost or new_cost < visited_cost[next_state]:
                    visited_cost[next_state] = new_cost
                    new_path = path + [action]
                    h = self.compute_heuristic(next_state)
                    f = new_cost + h
                    heapq.heappush(frontier, (f, next(counter), new_cost, next_state, new_path))
        return []
