n=int(input())
start=0
num=1
prod=1
while start<n:
    if num%2==0:
        prod*=num
        start+=1
    num+=1
print("The product of all even numbers up to",n,"is",prod,".")  