from collections import Counter


def solution(participant, completion ):
    dic = {}
    answer= ""
    count_p = Counter(participant)
    count_c = Counter(completion)
    #print(count_p)
    #print(count_c)
    for i in count_p.keys():
        if count_c[i] < count_p[i]:
            answer=i
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))