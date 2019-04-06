from lib.operations import ImperativeOperations


class TestMultipleOperation1(ImperativeOperations):

    def execute(self):
        print 'TestMultipleOperation1'


class TestMultipleOperation2(ImperativeOperations):

    def execute(self):
        print 'TestMultipleOperation2'


class TestMultipleOperation3(ImperativeOperations):

    def execute(self):
        print 'TestMultipleOperation3'
