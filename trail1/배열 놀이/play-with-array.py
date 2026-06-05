N, Q = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(Q):
    Query = list(map(int, input().split()))
    if len(Query) == 2:
        if Query[0] == 1:
            print(nums[Query[1]-1])
        else:
            if Query[1] in nums:
                print(nums.index(Query[1])+1)
            else:
                print(0)
    else:
        s, e = Query[1], Query[2]
        print(*nums[s-1:e])
