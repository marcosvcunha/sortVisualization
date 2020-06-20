import random
def randomList(listSize, max):
    return [random.randint(0, max) for _ in range(listSize)]