def print_all_friends(g, start):
    qu = []
    done = []
    qu.append((start,0))
    done.append(start)

    while qu:
        (p, c) = qu.pop(0)
        print(p, c)

        for i in g[p]:
            if i not in done:
                qu.append((i, c + 1))
                done.append(i)


fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')
