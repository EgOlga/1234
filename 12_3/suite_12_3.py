import unittest
import tests_12_3 as t_3

test_suite = unittest.TestSuite()
test_suite.addTest((unittest.TestLoader().loadTestsFromTestCase(t_3.RunnerTest)))
test_suite.addTest((unittest.TestLoader().loadTestsFromTestCase(t_3.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
