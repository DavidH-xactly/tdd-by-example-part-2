from test_runner import TestSuite, TestCase, TestResult


def reverse_string(str):
    return str[::-1]


class TestReverseString(TestCase):
    def set_up(self):
        self.result = None

    def test_reverse_string_success(self):
        result = reverse_string('car')
        assert(result == 'rac')

    def test_reverse_string_failure(self):
        result = reverse_string('car')
        assert(result == 'racer')


suite = TestSuite()
suite.add(TestReverseString('test_reverse_string_success'))
suite.add(TestReverseString('test_reverse_string_failure'))
result = TestResult()
suite.run(result)
print(result.summary())
