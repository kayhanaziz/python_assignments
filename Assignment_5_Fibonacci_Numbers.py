fib_numbers = []

for x in range(-2, 8) :

    if x < 0 :

        fib_numbers.append(1)

    else:

        fib_numbers.append(fib_numbers[x] + fib_numbers[x + 1])

print(fib_numbers)
