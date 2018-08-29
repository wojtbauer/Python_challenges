#Question - Problem 1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = list(range(2000,3200))
res = []
for num in numbers:
    if (num % 7 == 0) and (num % 5 != 0):
        res.append(str(num))
s = ', '
#print(res) #tabel form version
print(s.join(res)) #string version
