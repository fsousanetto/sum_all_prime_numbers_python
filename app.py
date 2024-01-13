primeNumbers = []
limit = 1000

def sumAll ():
    sumArray = sum(primeNumbers)
    print(sumArray)

def main (limit):
    for num in range(2, limit + 1):
        prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                prime = False
                break
        if prime:
            primeNumbers.append(num)
    return sumAll()

main(limit)