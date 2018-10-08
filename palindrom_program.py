#Write a program that returns the largest number-palindrome, which is the product of two prime five-digit numbers
# and returns the multipliers themselves.

prime_five_digits = []
for x in range(10001, 99999, 2):
    if x > 10000:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            prime_five_digits.append(x)

palindrome = {}
another = prime_five_digits[:]
for x in prime_five_digits:
    for y in another:
        z = x*y
        if str(z) == str(z)[::-1]:
            palindrome[z] = x, y

for key, value in palindrome.items():
    if key == max(palindrome):
        print(key, value)

