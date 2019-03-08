from unittest import TestCase

from recursion_dp_backtracking.A_triple_step.algorithm import amount_of_ways_to_run_up_the_stairs


class TripleStepTest(TestCase):
    def test_the_amount_of_ways_to_climb_a_stair_of_4_is_7(self):
        self.assertEquals(amount_of_ways_to_run_up_the_stairs(4), 7)

    def test_the_amount_of_ways_to_climb_a_stair_of_5_is_13(self):
        self.assertEquals(amount_of_ways_to_run_up_the_stairs(5), 13)

    def test_the_amount_of_ways_to_climb_a_stair_of_6_is_24(self):
        self.assertEquals(amount_of_ways_to_run_up_the_stairs(6), 24)

    def test_the_amount_of_ways_to_climb_a_stair_of_7_is_44(self):
        self.assertEquals(amount_of_ways_to_run_up_the_stairs(7), 44)
