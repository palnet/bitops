from type_check import *


@type_check
def bitcat(nums: [int], bits: [int]) -> int:
    if len(nums) != len(bits):
        raise ValueError("Lists must be same length")
    for i in range(len(nums)):
        if nums[i] >= 2**bits[i]:
            raise ValueError("Value is greater than " + str(bits[i]) + " bit(s) at index " + str(i))

    r = nums[-1]
    for i in range(len(nums) - 1):
        r += nums[i] << sum(bits[i + 1:])
    return r


@type_check
def bitsplit(num: int, bits: [int]) -> [int]:
    r = []
    for i in range(len(bits)):
        r.append(num >> sum(bits[i + 1:]) & (2**bits[i] - 1))
    return r
