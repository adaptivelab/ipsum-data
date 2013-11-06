import random


class IntIncrementor(object):

    def increment(self, number, column_spec):
        maxStep = column_spec['maxStep']
        positive_weighting = column_spec['positiveWeighting']
        change = random.randint(0, maxStep)
        direction = 1

        if (random.random() > positive_weighting):
            direction = -1

        change = change * direction
        return number + change
