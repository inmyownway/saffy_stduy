for test in range(1,11):
    n=int(input())
    bu = list(map(int,input().split()))

    count=0


    for b in range(2,len(bu)-2):
        #print(bu[b])
        if bu[b]>bu[b-1] and bu[b]>bu[b-2]\
                and bu[b]>bu[b+1] and bu[b]>bu[b+2]: # 가장 큰 빌딩이면
            view=bu[b]-max(bu[b-1],bu[b-2],bu[b+1],bu[b+2]) # 두번째로 큰 빌딩의 높이를 빼줌
            
            count+=view


    print("#{} {}".format(test,count))



