print("\n<< Bilangan Prima dan Komposit >>")
print("-"*40)

minimal = int(input("min:           "))
maximal = int(input("max:           "))

prima = []
komposit = {}

for number in range(minimal, maximal + 1):
    if number > 1:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                komposit[number] = None  
                break
        if is_prime:
            prima.append(number)

print("-"*40)

print("Bilangan Prima:")
print(prima)

print("Bilangan Komposit:")
print(list(komposit.keys()))