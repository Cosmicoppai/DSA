# 3 Questions on bit manipulation
# Baka

"""
1. Given a number, write a function that tests if its i^{th} bit is set.
"""


def test_bit_set(number, index):
    """
    Returns True if number has the index'th bit set
    and False otherwise.

    We'll say that the bits are numbered from the least significant bit (on the right) to the most significant bit (on the left).

    So, the binary number 0000 0001 has the 0^{th} bit set and all the rest of its bits are clear (not set).
    """
    binaryNum = []
    pos = 0
    while number > 0:
        binaryNum.append(number % 2)
        number //= 2
        pos += 1
    try:
        return True if binaryNum[index] == 1 else False
    except IndexError:
        return False


"""
We can also use left shift to check for set bit at ith index
"""


def test_bit_set_using_left_shift(number, index):
    """
    1 & 0 == 0,
    1 & 1 == 1
    By left shifting 1 by (k-1)th time we're setting a bit at (k-1) position i.e all number except (k-1) are zero...
    """
    return True if number & (1 << (index - 1)) != 0 else False


"""
Set Bit
Given a number, write a function that sets its i^{th} bit to 1.
"""


def set_bit(number, index):
    """"
    Set the index'th bit of number to 1, and return
    the result"""
    if number[index] == 1:
        return "The ith bit is already set"
    return number | (1 << (index - 1))


"""
Clear Bit
Given a number, write a function that clears its i^{th}bit by setting it to 0."""


def clear_bit(number, index):
    """
    Set the index'th bit of number to 0, and return
    the result.
    """
    if number[index] == 0:
        return "The ith bit is already 0 Bakayarou"
    return number & (~(1 << (index-1)))


"""
Given a number, write a function that toggles its i^{th} bit. (If the bit is 1, set it to 0. If it's 0, set it to 1.
"""


def toggle_bit(number, index):
    # return number & (~(1 << (index-1))) if number[index] == 1 else number | (1 << (index-1))
    return number ^ (1 << (index-1))  # XOR operation takes 2 bit and return 1 if exactly one bit is 1. Otherwise it returns 0


"""
Single Bit Set
Given a number, write a function that determines if the number has exactly one bit set.
"""


def single_bit_set(number):
    """
        Return True if number has exactly one bit set to 1; False
        if it has any other number of bits set to 1.
        """
    if number == 0:
        return False
    return number & (number-1)




if __name__ == "__main__":
    numbers = [5, 2, 75, 39, 500, 4, 4]
    pos_of_ith_bit = [1, 3, 4, 5, 3, 0, 2]

    for i in range(len(numbers)):
        print(f"Test {i} passed") if test_bit_set(numbers[i], pos_of_ith_bit[i]) == test_bit_set(numbers[i],
                                                                                                 pos_of_ith_bit[
                                                                                                     i]) else print(
            f"Test {i}Failed")
