
import itertools
import math
from itertools import product

def solution(numbers):
    answer = 0
    newNumber = []
    for i in range(len(numbers)):
        for j in itertools.permutations(numbers,i+1):
            if j[0] != '0':
                str_num = "".join(j)
                if str_num != '1':
                    newNumber.append(str_num)
    newNumber = list(set(newNumber))
    answers = []
    for n in newNumber:
        num = int(n)
        nSqrt = math.sqrt(num)
        x = 2
        cnt = 0
        while x <= nSqrt:
            if (num % x == 0):
                cnt += 1

            x += 1
        if num % nSqrt == 0:
            cnt += 1
        if cnt == 0:
            answers.append(num)


    answer = len(answers)
    print(answers)
    return answer
print(solution("17"))


