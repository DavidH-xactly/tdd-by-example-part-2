from test_runner import TestSuite, TestCase, TestResult


def reverse_string(str):
    return str[::-1]


class TestReverseString(TestCase):
    def set_up(self):
        self.result = None

    def test_reverse_string(self):
        result = reverse_string('car')
        assert(result == 'rac')


suite = TestSuite()
suite.add(TestReverseString('test_reverse_string'))
result = TestResult()
suite.run(result)
print(result.summary())
