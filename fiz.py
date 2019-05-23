#print (" new repo")

for n in range(100):
    if n % 15 == 0:       #number divisible by 15 (divisible by 3 & 5)
        print("FizzBuzz")
        continue
    elif n % 3 == 0:      #number divisible by 3 print fizz
        print("Fizz")
        continue
    elif n % 5 == 0:      #number divisible by 5 print buzz
        print("Buzz")
        continue
    print(n)
