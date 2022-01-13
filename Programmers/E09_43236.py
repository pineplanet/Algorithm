def solution(distance, rocks, n):
    answer = []

    lt = 1
    rt = distance
    res = 0

    def cal(a):
        a.insert(0, 0)
        a.append(distance)
        r = []
        for i in range(1, len(a)):
            r.append(a[i] - a[i - 1])

        return r

    def count(l):
        cnt = 0
        ep = 0
        d = []
        for i in range(0, len(rocks)):

            if rocks[i] - ep < l:
                cnt += 1
                d.append(rocks[i])
            else:
                ep = rocks[i]
        return d

    while lt <= rt:
        mid = (lt + rt) // 2
        if len(count(mid)) > n:
            # mid 가 줄어들어야함
            rt = mid - 1
        elif len(count(mid)) <= n:
            lt = mid + 1
            answer = list(set(rocks) - set(count(mid)))
            answer.sort()

    r2 = cal(answer)
    answer = min(r2)

    return answer


d = 25
rocks = [2, 14, 11, 21, 17]
rocks.sort()
n = 2
print(solution(d, rocks, n))
