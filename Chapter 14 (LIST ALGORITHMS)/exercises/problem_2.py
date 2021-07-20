from unit_tester import *
import time

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

# test(not share_diagonal(5,2,2,0))
# test(share_diagonal(5,2,3,0))
# test(share_diagonal(5,2,4,3))
# test(share_diagonal(5,2,4,1))

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


# # Solutions cases that should not have any clashes
# test(not col_clashes([6,4,2,0,5], 4))
# test(not col_clashes([6,4,2,0,5,7,1,3], 7))

# # More test cases that should mostly clash
# test(col_clashes([0,1], 1))
# test(col_clashes([5,6], 1))
# test(col_clashes([6,5], 1))
# test(col_clashes([0,6,4,3], 3))
# test(col_clashes([5,0,7], 2))
# test(not col_clashes([2,0,1,3], 1))
# test(col_clashes([2,0,1,3], 2))

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

# test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
# test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
# test(has_clashes([0,1,2,3]))             # Try small 4x4 board
# test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case

def solve_n_queens(n):
    import random
    rng = random.Random()   # Instantiate a generator
    bd = list(range(n))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 1:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

# solve_n_queens(4)
# solve_n_queens(12)

# t0 = time.time()
# solve_n_queens(14)
# t1 = time.time()
# print("Solving 14 queens took {0:.4f} seconds.".format(t1-t0)) #5.8446 seconds

# t0 = time.time()
# solve_n_queens(16)
# t1 = time.time()
# print("Solving 16 queens took {0:.4f} seconds.".format(t1-t0)) #49.6144 seconds

t0 = time.time()
solve_n_queens(17)
t1 = time.time()
print("Solving 17 queens took {0:.4f} seconds.".format(t1-t0)) #71.4941 seconds, 48.1055 seconds.

# maximum size that can be solved under a minute is 17 queens (considering randomness might decrease the time).

# t0 = time.time()
# solve_n_queens(18)
# t1 = time.time()
# print("Solving 18 queens took {0:.4f} seconds.".format(t1-t0)) #167.4585 seconds.