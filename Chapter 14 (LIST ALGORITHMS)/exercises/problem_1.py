# operations on lists, not sets (duplicate elements allowed)

from unit_tester import *

def merge_intersection(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:

        if xi >= len(xs) or yi >= len(ys):          # If either list is finished,
            return result          # And we're done.
        
        # Both lists still have items, if the items are same only then append.
        if xs[xi] < ys[yi]:
            xi += 1

        elif xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1

        else:
            yi += 1

def merge_first_only(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        
        if xi >= len(xs):          # If xs is finished,
            return result          # And we're done.
        
        if yi >= len(ys):          # If ys is finished,
            result.extend(xs[xi:]) # Add remaining items from xs
            return result

        # Both lists still have items, if the items are present in the first only, only then append.
        if xs[xi] < ys[yi]:
            result.append(xs[xi]) 
            xi += 1

        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        else:
            yi += 1

def merge_second_only(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        
        if yi >= len(ys):          # If ys is finished,
            return result          # And we're done.
        
        if xi >= len(xs):          # If xs is finished,
            result.extend(ys[yi:]) # Add remaining items from xs
            return result

        # Both lists still have items, if the items are present in the second only, only then append.
        if xs[xi] < ys[yi]:
            xi += 1

        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        else:
            result.append(ys[yi]) 
            yi += 1

# elements present in both lists taken once, unless they are present more than once in either lists
def merge_union(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        
        if yi >= len(ys):
            result.extend(xs[xi:]) # If ys is finished,
            return result          # Add remaining items from xs
        
        if xi >= len(xs):          # If xs is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result

        # Both lists still have items, if the items are present in the either, append.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        elif xs[xi] == ys[yi]:
            result.append(ys[yi])
            xi += 1
            yi += 1

        else:
            result.append(ys[yi]) 
            yi += 1

def bagdiff(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(ys):
            result.extend(xs[xi:]) # If ys is finished,
            return result          # Add remaining items from xs
        
        if xi >= len(xs):          # If xs is finished,
            return result 

        # Both lists still have items, if the items are present in the either, append. But no repeats.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        else:
            yi += 1
        

xs = [1, 3, 3, 5, 6, 7, 9, 9, 11, 13, 15, 17, 19] # sorted list 1
ys = [0, 3, 3, 4, 6, 7, 8, 9, 12, 16, 17, 17, 18, 19, 20]  # sorted list 2

#Test 1_a
test(merge_intersection(xs, ys) == [3, 3, 6, 7, 9, 17, 19])
test(merge_intersection(xs, []) == [])
test(merge_intersection([], ys) == [])
test(merge_intersection([], []) == [])
test(merge_intersection([1, 2, 9], [3, 4]) == [])

#Test 1_b
test(merge_first_only(xs, ys) == [1, 5, 9, 11, 13, 15])    
test(merge_first_only(xs, []) == xs)
test(merge_first_only([], ys) == [])
test(merge_first_only([], []) == [])
test(merge_first_only([1, 2, 9], [3, 4]) == [1, 2, 9])

#Test 1_c
test(merge_second_only(xs, ys) == [0, 4, 8, 12, 16, 17, 18, 20]) 
test(merge_second_only(xs, []) == [])
test(merge_second_only([], ys) == ys)
test(merge_second_only([], []) == [])
test(merge_second_only([1, 2, 9], [3, 4]) == [3, 4])

#Test 1_d
test(merge_union(xs, ys) == [0, 1, 3, 3, 4, 5, 6, 7, 8, 9, 9, 11, 12, 13, 15, 16, 17, 17, 18, 19, 20]) # failed
test(merge_union(xs, []) == xs)
test(merge_union([], ys) == ys)
test(merge_union([], []) == [])
test(merge_union([1, 2, 9], [3, 4]) == [1, 2, 3, 4, 9])

#Test 1_e
test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])