import math as m


def GetInBinary(size, num):
    ret = ""
    while ( size > 0):
        if num - m.pow(2, size - 1) >= 0:
            num -= m.pow(2, size - 1)
            ret += '1'
        else:
            ret += '0'
        size -= 1
    return ret


def GetNegativeFromBinary(num):
    ret = ""
    for digit in num:
        if digit == '1':
            ret += '0'
        else:
            ret += '1'
    return AddOne(ret)


def AddOne(num):
    if len(num) == 0:
        return '1'
    if num[-1] == '0':
        return num[:-1] + '1'
    else:
        return AddOne(num[:-1]) + '0'


size = int(input('enter the size of the number in bits: ->'))
num = int(input('enter the number: ->'))
numInBin = GetInBinary(size, num)
negBin = GetNegativeFromBinary(numInBin)

print(f'{num} in binary is: {numInBin}, -{num} in binary is: {negBin}')
