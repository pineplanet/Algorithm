from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    Max = len(prices)
    while prices:
        item = prices.popleft();

        a = 0;
        for i in prices:
            if item > i:
                a = a+1
                break
            else:
                a =a+1
        answer.append(a)

    return answer



prices = [1,2,3,2,3]
print( solution(prices))