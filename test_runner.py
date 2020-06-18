class TestResult:
    def summary(self):
        return "1 run, 0 failed"


class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return result


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = ''

    def set_up(self):
        self.log += "set_up "

    def test_method(self):
        self.log += 'test_method '

    def tear_down(self):
        self.log += 'tear_down'


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun('test_method')

    def test_template_method(self):
        self.test.run()

        assert(self.test.log == 'set_up test_method tear_down')

    def test_result(self):
        result = self.test.run()

        assert(result.summary() == "1 run, 0 failed")

    def tear_down(self):
        pass


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
