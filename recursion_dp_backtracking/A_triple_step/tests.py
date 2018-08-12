from unittest import TestCase

from exercises.recursion_dp_backtracking.A_triple_step.algorithm import amount_of_ways_to_run_up_the_stairs


class TripleStepTest(TestCase):
    def test_the_amount_of_ways_to_climb_a_stair_with_triple_step_is_correctly_calculated(self):
        self.assertEquals(amount_of_ways_to_run_up_the_stairs(4), 7)