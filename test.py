#!/usr/bin/python3

import unittest
from match import Match
from player_stub import StubPlayer
from player_robin import RobinPlayer


class TestStringMethods(unittest.TestCase):


    def test_round_r_vs_s(self):

        p1 = StubPlayer()
        p1.always_shoot("R")
        p2 = StubPlayer()
        p2.always_shoot("S")
        m = Match(p1, p2)

        w = m.perform_round()

        self.assertEqual(w, 1)


    def test_round_r_vs_p(self):

        p1 = StubPlayer()
        p1.always_shoot("R")
        p2 = StubPlayer()
        p2.always_shoot("P")

        m = Match(p1, p2)

        r = m.perform_round()

        self.assertEqual(r, 2)


    def test_round_r_vs_r(self):

        p1 = StubPlayer()
        p1.always_shoot("R")
        p2 = StubPlayer()
        p2.always_shoot("R")

        m = Match(p1, p2)

        r = m.perform_round()

        self.assertEqual(r, 3)


    def test_round_invalid(self):

        p1 = StubPlayer()
        p1.always_shoot("x")
        p2 = StubPlayer()
        p2.always_shoot("x")

        with self.assertRaises(AssertionError):

            m = Match(p1, p2)
            r = m.perform_round()

    def test_robin(self):

        robin = RobinPlayer()
        robin.start_match()

        shot1 = robin.shoot()
        shot2 = robin.shoot()
        shot3 = robin.shoot()
        shot4 = robin.shoot()

        self.assertEqual(shot1, "R")
        self.assertEqual(shot2, "P")
        self.assertEqual(shot3, "S")
        self.assertEqual(shot4, "R")


if __name__ == '__main__':
    unittest.main()
