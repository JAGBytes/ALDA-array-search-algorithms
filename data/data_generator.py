import random
from data import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(random.randint(0, limit))
    return answer


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)