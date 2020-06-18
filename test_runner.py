class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.fail_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.fail_count += 1

    def summary(self):
        return "%d run, %d failed" % (self.run_count, self.fail_count)


class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = ''

    def set_up(self):
        self.log += "set_up "

    def test_method(self):
        self.log += 'test_method '

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log += 'tear_down'


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun('test_method')

    def test_template_method(self):
        result = TestResult()
        self.test.run(result)

        assert(self.test.log == 'set_up test_method tear_down')

    def test_success_result(self):
        result = TestResult()
        self.test.run(result)

        assert(result.summary() == "1 run, 0 failed")

    def test_failed_result(self):
        result = TestResult()
        self.test.run(result)
        # print(result.summary())
        assert(result.summary() == "1 run, 1 failed")

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()

        assert(result.summary() == "1 run, 1 failed")

    # def test_set_up_fail_tear_down_called(self):
    #     self.test.run()
    #     print(self.test.log)
    #     assert(self.test.log == 'set_up tear_down')

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        result = TestResult()

        suite.run(result)
        assert(result.summary() == "2 run, 1 failed")

    def tear_down(self):
        pass


# suite = TestSuite()
# suite.add(TestCaseTest('test_template_method'))
# suite.add(TestCaseTest('test_success_result'))
# suite.add(TestCaseTest('test_failed_result'))
# suite.add(TestCaseTest('test_failed_result_formatting'))
# suite.add(TestCaseTest('test_suite'))
# result = TestResult()
# suite.run(result)
# print(result.summary())
