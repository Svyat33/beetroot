"""
Task 3

Write a function called `choose_func` which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list
and return the result of it. Otherwise, return the result of the second one


def choose_func(nums: list, func1, func2):

    pass



# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]



def square_nums(nums):

    return [num ** 2 for num in nums]



def remove_negatives(nums):

    return [num for num in nums if num > 0]



assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""
nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):

    return [num ** 2 for num in nums]


def remove_negatives(nums):

    return [num for num in nums if num > 0]


def choose_func(numbers, func1, func2):
    processed = list(filter(lambda x: x < 0, numbers))
    if len(processed) == 0:
        return func1(numbers)
    else:
        return func2(numbers)


if __name__ == "__main__":
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))
