
my_list = [int(n) for n in input().split()]

x=1

for n in my_list:
    x= n * x
print(x)