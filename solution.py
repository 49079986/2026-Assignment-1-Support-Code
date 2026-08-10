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

    STUDENT_NAME = "Crystal Rover" # replace with your name
    STUDENT_ID = "s4123456"  # replace with your student ID
    GITHUB_USERNAME = "cool-comp3702-student" # replace with your GitHub username

    def __init__(self, game_env):
        self.game_env = game_env

        #
        #
        # TODO: Define any class instance variables you require here (avoid performing any computationally expensive
        #  heuristic preprocessing operations here - use the preprocess_heuristic method below for this purpose).
        #
        #

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

        #
        #
        # TODO: Implement your UCS code here.
        #
        #

        pass

    # === A* Search ====================================================================================================
    # TODO: this method is unnecessary if multiple searches on the same environment are not performed
    def preprocess_heuristic(self):
        """
        Perform pre-processing (e.g. pre-computing repeatedly used values) necessary for your heuristic,
        """

        #
        #
        # TODO: (Optional) Implement code for any preprocessing required by your heuristic here (if your heuristic
        #  requires preprocessing).
        #
        # If you choose to implement code here, you should call this method from your search_a_star method (e.g. once at
        # the beginning of your search).
        #
        #

        pass

    def compute_heuristic(self, state):
        """
        Compute a heuristic value h(n) for the given state.
        :param state: given state (GameState object)
        :return a real number h(n)
        """

        #
        #
        # TODO: Implement your heuristic function for A* search here. Note that your heuristic can be tested on
        #  gradescope even if you have not yet implemented search_a_star.
        #
        # You should call this method from your search_a_star method (e.g. every time you need to compute a heuristic
        # value for a state).
        #
        #

        pass

    def search_a_star(self):
        """
        Find a path which solves the environment using A* Search.
        Your heuristic computation must be implemented within compute_heuristic and called from this method
        If you have any expensive pre-computation you can implment it in preprocess_heuristic
        :return: path (list of actions, where each action is an element of GameEnv.ACTIONS)
        """

        #
        #
        # TODO: Implement your A* search code here.
        #
        #

        pass
