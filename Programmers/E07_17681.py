def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result1 = bin(arr1[i] | arr2[i])
        result2 = result1[2:].rjust(n,'0').replace("1", "#").replace("0"," ")
        answer.append(result2)
    print(answer)
    return answer


arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
solution(6, arr1, arr2)
["######", "### #", "## ##", " #### ", " #####", "### # "]
