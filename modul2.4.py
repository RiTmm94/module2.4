numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue # тут если 1 то просто возвращаемся и берем следуюшее число
    is_prime = True # тут как я понимаю что если условие не равно 1 выполнено то is_prime = True
    for i in range(2, number): # тут как я понимаю идет ранжирование переменной i [2 до текущего числа]
        if number % i == 0: # условие если число делится целочисленно на переменные , допустим если number = 4, то i = 2,3
            is_prime = False # и деление будет 4/2, 4/3 но оба варианта при делении не равны 0, получается условие не выолняется..?
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)