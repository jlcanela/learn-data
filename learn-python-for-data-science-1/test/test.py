import unittest
import subprocess


class TestPrediction(unittest.TestCase):
    """test methods"""

    def exec(self, file, count):
        """execute provided file and expects ['male'] for success"""
        results = 0
        for i in range(count):
            result = subprocess.run(['python', file], stdout=subprocess.PIPE)
            print("%d - %s" % (i, result))
            if result.stdout == b"['male']\n":
                results += 1
        return results

    def test_demo_result_male_10_times(self):
        """test demo.py provided by siraj"""
        results = self.exec('learn-python-for-data-science-1/demo.py', 10)
        self.assertEqual(results, 10)

    def test_learn_result_fails_at_least_once(self):
        """test buggy buggy.py not to return always the same result"""
        results = self.exec('learn-python-for-data-science-1/buggy.py', 10)
        self.assertLess(results, 10)


if __name__ == '__main__':
    unittest.main()
