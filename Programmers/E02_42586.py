import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    due = deque()
    progresses = deque(progresses)
    for i in range(len(progresses)):
        due.append(math.ceil((100 - progresses[i]) / speeds[i]))
    print(due)

    work = due.popleft()
    cnt = 1
    while due:
        if work >= due[0]:
            cnt = cnt + 1
            due.popleft()
        elif work < due[0]:
            answer.append(cnt)
            print(work, cnt)

            work = due.popleft()
            cnt = 1
    answer.append(cnt)
    print(work, cnt)
    return answer


# solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
