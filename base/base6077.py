#입력된 숫자에서 짝수인것만 합
n=int(input())
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i

print(s)