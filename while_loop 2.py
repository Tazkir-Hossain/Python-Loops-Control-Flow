# 01 Find sum of given numbers as input
num_of_number=int(input('Enter number of number'))
sum=0
count=0
while count<num_of_number:
    n=int(input('Enter a number'))
    sum=sum+n
    count+=1
print(sum)


# 02 Find sum of positive and negative numbers
num_of_number=int(input('Enter number of number'))
count=0
psum=0
nsum=0
while count<num_of_number:
    n=int(input('Enter a number'))
    if n>0:
        psum=psum+n
    else:
        nsum=nsum+n
    count+=1
print('The positive number is',psum)
print('The negetive number is',nsum)


# 03 Find maximum numbers from the given numbers
num_of_number=int(input('Enter number of number'))
count=0
max=0
while count<num_of_number:
    n=int(input('Enter number'))
    if n>max:
        max=n
    count+=1
print('The max number is ',max)


# 04 Convert a Decimal number to a Binary number
n=45674
binary=0
while n>0:
    r=n%2
    n=n//2
    binary=binary*10+r
# print(binary)
m=binary
reverse=0
while m>0:
    r=m%10
    m=m//10
    reverse=reverse*10+r
print(reverse)


