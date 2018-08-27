import shapley.game
import shapley.solution
import unittest

class TestSmallDictGames(unittest.TestCase):
    def test_four_player_dict_game(self):
        game = shapley.game.ManualDictGame({'a', 'b', 'c', 'd'}, {
            '': 0,
            'a': 50,
            'b': 0,
            'c': 0,
            'd': 0,
            'ab': 100,
            'ac': 80,
            'ad': 110,
            'bc': 0,
            'bd': 0,
            'cd': 0,
            'abc': 350,
            'abd': 300,
            'acd': 500,
            'bcd': 0,
            'abcd': 1000
        })
        solution = shapley.solution.Shapley(game)

        grand_coalitional_payoff = game.payoff(game.players)
        vs = []
        for p in game.players:
            vs.append(solution.shapley(p))
            print('phi(%s) = %.4f' % (p, solution.shapley(p)))

        self.assertAlmostEqual(grand_coalitional_payoff, sum(vs))

    def test_general_council_game(self):
        game = shapley.game.GeneralCouncilGame({'a', 'b', 'c', 'd', 'e', 'f'}, 3, 4)

        solution = shapley.solution.Shapley(game)

        grand_coalitional_payoff = game.payoff(game.players)
        vs = []
        for p in game.players:
            vs.append(solution.shapley(p))
            print('phi(%s) = %.4f' % (p, solution.shapley(p)))

        self.assertAlmostEqual(grand_coalitional_payoff, sum(vs))