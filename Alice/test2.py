def knapsack(w, v, k):
    dict = {}
    for i in range(len(v)):
        dict[v[i]] = w[i]

    K = sorted(dict.keys() , reverse=True)
    sum_w  = 0
    sum_v  = 0
    can = k
    for i in K:
        if dict[i] <= k :
            k -= dict[i]
            sum_v += i
    print(sum_v)

    return sum_v




w = [10, 20, 30]
v = [60, 100, 120]
k = 50


knapsack(w, v, k)
