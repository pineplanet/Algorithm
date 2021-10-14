def solution(answers):
    answer = []
    p1Pattern = [1, 2, 3, 4, 5]
    p2Pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    p3Pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    sheet = []
    answersLength = len(answers)
    for i in [p1Pattern, p2Pattern, p3Pattern]:
        if answersLength > len(i):
            mul = round(len(answers) / len(i)) + 1
            sheet.append(i * mul)
        else:
            sheet.append(i)

    count = {0: 0, 1: 0, 2: 0}
    for i in range(answersLength):
        for j in range(len(sheet)):
            if sheet[j][i] == answers[i]:
                count[j] += 1

    Max = (max(count.values()))

    for i in count.keys():

        if count[i] == Max:
            answer.append(i+1)
    print (answer)
    return answer


solution([1,3,2,4,2])
