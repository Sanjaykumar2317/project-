start =int(input("Enter the Start range:"))
end =int(input("Enter the End range:"))
for num in range(start,end + 1):
    if num%2==0:
        print(num,end = ' ')