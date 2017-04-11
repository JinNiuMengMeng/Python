#!/usr/bin/python
class Student(object):
    score = 0
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interge!')
        if value < 0 or value > 100:
            raise ValueError('score must be in 0 - 100')
        self._score = value

Tom = Student()
Tom.set_score(999)
print Tom.get_score()
