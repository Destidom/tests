import unittest
from pathlib import Path
from test.score import Score
from test.code_extractor import extract
from user.DAT110.exercise1 import falling_object, sum_integers


print('Extracting code fro ipynb.')
path_wo_fileending = '../user/DAT110/exercise1'
try:
    filename = path_wo_fileending + '.ipynb'
    f = Path(filename)
    print('Could find filename: {}'.format(f.is_file()))

    success = extract(path_wo_fileending + '.ipynb', path_wo_fileending + '.py')

    filename = path_wo_fileending + '.py'
    f = Path(filename)
    print('Could find filename: {}'.format(f.is_file()))

    print('Code extraction was successful.')
except:
    print('Code extraction was unsuccessful.')
#print('Code extraction was {}'.format('successful.' if success else 'unsuccessful.'))



class TestFallingObject(unittest.TestCase):
    score = Score(10, 10, 'TestFallingObject')
    points_worth = 0

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)
        print(self.score.write_json())

    def test_normal_case_1(self):
        self.points_worth = 4
        self.assertEqual(falling_object(10), 981.00)

    def test_normal_case_2(self):
        self.points_worth = 4
        self.assertEqual(falling_object(56), 30764.16)

    def test_falling_object_negative(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object(-1)


class TestSumIntegers(unittest.TestCase):
    score = Score(8, 20, 'TestSumIntegers')
    points_worth = 0

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)
        print(self.score.write_json())

    def test_normal_case_1(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([10, 10]), 20)

    def test_normal_case_2(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([90, 10, 45, 25]), 170)

    def test_zero(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([0, 0]), 0)

    def test_negative(self):
        self.points_worth = 2
        with self.assertRaises(Exception): sum_integers([1, 20, -1])

if __name__ == '__main__':
    unittest.main()
