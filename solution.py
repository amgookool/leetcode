import enum
from multiprocessing import cpu_count
from operator import ne


def romanToInt(s: str) -> int:
    cnt = 0
    roman_map = {
        "I": lambda count: count + 1,
        "V": lambda count: count + 5,
        "X": lambda count: count + 10,
        "L": lambda count: count + 50,
        "C": lambda count: count + 100,
        "D": lambda count: count + 500,
        "M": lambda count: count + 1000,
        "IV": lambda count: count + 4,
        "IX": lambda count: count + 9,
        "XL": lambda count: count + 40,
        "XC": lambda count: count + 90,
        "CD": lambda count: count + 400,
        "CM": lambda count: count + 900
    }
    solve = list()
    for index in range(len(s)):
        if index == 0:
            cur = s[index]
            nex = s[index+1]
            if cur+nex in roman_map.keys():
                solve.append(cur+nex)
            else:
                solve.append(cur)
        elif index == len(s) - 1 :
            cur = s[index]
            prev = s[index-1]
            if prev+cur in roman_map.keys() and (prev+cur) not in solve:
                solve.append(prev+cur)
            else:
                solve.append(cur)
        if index != 0 and index <= (len(s)-2):
            cur = s[index]
            prev = s[index-1]
            nex = s[index+1]
            if (prev+cur) in roman_map.keys() and (prev+cur) not in solve:
                solve.append(prev+cur)
            elif (prev+cur) not in roman_map.keys() and (cur+nex) not in roman_map:
                solve.append(cur)

    for i in solve:
        cnt = roman_map.get(i)(cnt)
    print(cnt)
    return cnt


if __name__ == "__main__":
    test1 = "III"
    test2 = "LVIII"
    test3 = "MCMXCIV"
    test4 = "MMMCDXC"
    test5 = "IV"
    romanToInt(test5)
