#!/usr/bin/python
class Student(object):
    __slots__ = ('name', 'score')
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print 'name = %s\nscore = %s' % (self.name, self.score)
student1 = Student('tom', 90)
student1.print_score()

student1.high = 180
print student1.high
#print dir(Student)

