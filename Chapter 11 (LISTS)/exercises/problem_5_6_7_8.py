import sys

def add_vectors(u, v):
    result = u[:]
    for (idx, elem) in enumerate(v):
        result[idx] += elem
    return result

def scalar_mult(s, v):
    result = v[:]
    for i in range(len(result)):
        result[i] *= s
    return result

def dot_product(u, v):
    result = 0
    for i in range(len(u)):
        result += u[i] * v[i]
    return result

def cross_product(u, v):  # for vector of length 3
    result = []
    dim = len(u)
    for i in range(dim):
        a = u[(i + 1) % dim]
        b = v[(i + 1) % dim]
        c = u[(i + 2) % dim]
        d = v[(i + 2) % dim]
        result.append(a*d - b*c)
    return result


def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

# test(add_vectors([1, 1], [1, 1]) == [2, 2])
# test(add_vectors([1, 2], [1, 4]) == [2, 6])
# test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

# test(scalar_mult(5, [1, 2]) == [5, 10])
# test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
# test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

# test(dot_product([1, 1], [1, 1]) == 2)
# test(dot_product([1, 2], [1, 4]) == 9)
# test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

test(cross_product([1, 2, 1], [1, 4, 3]) == [2, -2, 2])
test(cross_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
test(cross_product([10, 5, 11], [9, 14, 3]) == [-139, 69, 95])
test(cross_product([-10, -5, 11], [9, 14, -3]) == [-139, 69, -95])