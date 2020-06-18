class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def set_up(self):
        self.was_run = None
        self.log = "set_up "

    def test_method(self):
        self.set_up()
        self.was_run = 1
        self.log += 'test_method '


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun('test_method')

        test.run()
        assert(test.log == 'set_up test_method ')


TestCaseTest('test_running')
TestCaseTest('test_set_up')
