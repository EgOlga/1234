import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        rnn_1 = runner.Runner(name="Olga")
        for _ in range(10):
            rnn_1.walk()
        self.assertEqual(rnn_1.distance, 50)


    def test_run(self):
        rnn_2 = runner.Runner(name="Serg")
        for _ in range(10):
            rnn_2.run()
        self.assertEqual(rnn_2.distance, 100)

    def test_challenge(self):
        rnn_3 = runner.Runner(name="Anna")
        rnn_4 = runner.Runner(name="Maria")
        for _ in range(10):
            rnn_3.walk()
            rnn_4.run()
        self.assertNotEqual(rnn_3, rnn_4)

if __name__ == "__main__":
    unittest.main()

"""
Результат_1:
Ran 3 tests in 0.003s

OK

Примечания:
Попробуйте поменять значения в одном из тестов, результаты

(изменено значение для проверки 100 на 1000 в функции test_run)
Результат_2:
    
Ran 3 tests in 0.009s

FAILED (failures=1)


1000 != 100

Expected :100
Actual   :1000
<Click to see difference>

Traceback (most recent call last):
  File "C:\Users\olgaa\PycharmProjects\pythonProject1\module_12_1.py", line 18, in test_run
    self.assertEqual(rnn_2.distance, 1000)
AssertionError: 100 != 1000
"""
