count=0
while count<10:
    print(count,'Hello')
    count+=1
# 01 Display Multiplication table for a given number
n=5
count=1
while count<=10:
    print(n,'x',count,'=',n*count)
    count+=1
# 02 Counting the number of digits in a number
n=12359
count=0
while n>0:
    n=n//10
    count += 1
print(count)

# 03 Find sum of digits in number
n=12345
sum=0
while n>0:
    r=n%10
    n=n//10
    sum=sum+r
print('The digit of sum is',sum)
# 04 Reversing a number
n=12345
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)
# 04 Check if a number is a Palindrome
n=int(input('Enter a number'))
m=n
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if rev==m:
    print('The number is a Palindrome')
else:
    print('The number is not a Palindrome')


