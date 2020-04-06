# Fibonacci Series
n = int(input("Enter no. of terms in series : "))
i0 = 0
i1 = 1
count = 0
if n <= 0:
    print("please enter a positive Number")
elif n == 1:
    print("Sequence :")
    print(i0)
else:
    while count < n:
        print(i0)
        i2 = i1 + i0
        i0 = i1
        i1 = i2
        count += 1
        
