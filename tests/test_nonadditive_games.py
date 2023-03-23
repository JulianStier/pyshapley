import unittest

import pyshapley.game
import pyshapley.solution


class TestSmallDictGames(unittest.TestCase):
    def test_three_player_dict_game(self):
        game = pyshapley.game.ManualDictGame(
            {"a", "b", "c"},
            {
                "": 0,
                "a": 0.99,
                "b": 0,
                "c": 0.99,
                "ab": 0.0,
                "ac": 1.0,
                "bc": 0.0,
                "abc": 0.0,
            },
        )
        solution = pyshapley.solution.Shapley(game)

        vs = []
        for p in game.players:
            vs.append(solution.shapley(p))
            print("phi(%s) = %.4f" % (p, solution.shapley(p)))

        print("-")

    def test_three_player_dict_game2(self):
        game = pyshapley.game.ManualDictGame(
            {"a", "b", "c"},
            {
                "": 0,
                "a": 1.0,
                "b": 0.9,
                "c": 0,
                "ab": 1.0,
                "ac": 1.0,
                "bc": 0.0,
                "abc": 0.0,
            },
        )
        solution = pyshapley.solution.Shapley(game)

        vs = []
        for p in game.players:
            vs.append(solution.shapley(p))
            print("phi(%s) = %.4f" % (p, solution.shapley(p)))

        print("-")

        # self.assertAlmostEqual(grand_coalitional_payoff, sum(vs))

    def test_three_player_dict_game3(self):
        game = pyshapley.game.ManualDictGame(
            {"a", "b", "c"},
            {
                "": 0,
                "a": 1.0,
                "b": 0,
                "c": 1.0,
                "ab": 0,
                "ac": 1.0,
                "bc": 0,
                "abc": 0,
            },
        )
        solution = pyshapley.solution.Shapley(game)
        vs = []
        for p in game.players:
            vs.append(solution.shapley(p))
            print("phi(%s) = %.4f" % (p, solution.shapley(p)))

        print("-")

    def test_four_player_dict_game(self):
        game = pyshapley.game.ManualDictGame(
            {"a", "b", "c", "d"},
            {
                "": 0,
                "a": 0,
                "b": 0,
                "c": 0,
                "d": 0,
                "ab": 0,
                "ac": 0,
                "ad": 0,
                "bc": 0,
                "bd": 0.5,
                "cd": 0,
                "abc": 0,
                "abd": 0,
                "acd": 0,
                "bcd": 1.0,
                "abcd": 0,
            },
        )
        solution = pyshapley.solution.Shapley(game)

        vs = []
        for p in game.players:
            vs.append(solution.shapley(p))
            print("phi(%s) = %.4f" % (p, solution.shapley(p)))
        print("-")
