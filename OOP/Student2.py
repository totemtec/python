class Student(object):
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student("Bart Simpson", 59)

bart.print_score()

print(bart.name)