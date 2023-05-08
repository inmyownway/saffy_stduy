from itertools import combinations
test_case=int(input())
for test in range(1,test_case+1):
    n=int(input())
    problems=list(map(int,input().split()))
    visit=[0]*(sum(problems)+1)
    visit[0]=1
    # 2 3 5
    # 0 2 3 5 7 8 10
    #
    for problem in problems:
        #print(problem)
       # print(visit)
        for i in range(len(visit)-1,-1,-1):


            if visit[i]==1:
                #print(problem,i," ",i+problem)
                visit[i+problem]=1
                #print(visit)

    print("#{} {}".format(test,sum(visit)))



