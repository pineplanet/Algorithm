import itertools
import math
from itertools import product


def solution(numbers):
    answer = 0
    answers = []
    nlist = list(numbers)
    # print(nlist)
    nlist2 = []
    for i in range(len(numbers)):
        # print(list(map(''.join, itertools.permutations(numbers,i+1))))
        nlist2.append(list(map(''.join, itertools.permutations(numbers, i + 1))))

    print(nlist2)

    for i in range(len(nlist2)):
        for j in range(len(nlist2[i])):
            if nlist2[i][j][0] != "0":

                num = int(nlist2[i][j])
                cnt = 0
                if num != 1:
                    sqrt_num = math.sqrt(num)
                    x = 2;

                    while x <= sqrt_num:
                        if (num % x == 0):
                            cnt += 1
                        # print(num, num%x)
                        x += 1
                    if num % sqrt_num == 0:
                        cnt += 1
                    if cnt == 0:
                        answers.append(num)

   #print(answers)
    answer_set = set(answers)
    print(answer_set,len(answer_set))
    answer = len(answer_set)

    # print(nlist2)
    return answer


solution("011")
