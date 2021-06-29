import random

def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
        Generate a list containing num random ints between
        lower_bound and upper_bound. upper_bound is an open bound.
        The result list cannot contain duplicates.
    """

    result = []
    rng = random.Random()

    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)