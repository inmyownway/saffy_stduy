#test_case = int(input())
def mul(x,y):

    if y==0:
        return 1
    return x*mul(x,y-1)
for tc in range(1, 11):
    n=int(input())
    x,y=map(int,input().split())

    answer=0

    answer=mul(x,y)
    print("#%d %d"%(tc,answer))

