def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2) - 1 #change the symbol to - so its centered correctly
    a[mid], a[n-1] = a[n-1], a[mid]
    # this do the following
    # sort => 1 2 3 4 5 6 7
    # then get the middle and replace
    # 1 2 3 7 5 6 4
    
    st = mid + 1  # this is the middle of the arr + 1 which is idx 4 -> a[4] = 5
    ed = n - 2  # change this from - 1 to -2 since a[5] = 6 and a[6] = 4
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]  # here we flip places of a[4] with a[5]
        st = st + 1
        ed = ed - 1  # and change +1 to -1 so it only runs once
    
    # so we are left with  1 2 3 7 6 5 4 => result

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


