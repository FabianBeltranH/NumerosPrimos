primeNumbersList = [2] #For this solution we have a list storing our prime numbers, we start with the number 2 in it
primeNumbersFound = 1 #Counter for prime numbers found, starts at 1 since we are including the number 2 from the start
currentNumber = 2 #The number we start testing with, at the beginning of the first loop it'll increment to 3


while primeNumbersFound < (10001): #We keep the loop until we find the 10001st prime number

    currentNumber = currentNumber + 1 #We begin checking if 3 is prime, then 4, etc.
    primeNumber = True #We assume all numbers are prime in first instance

    for i in (primeNumbersList): #We are going to compare the numbers with only the prime numbers in our list

        if ((currentNumber % i) == 0):  #If any of the numbers in the counter is a multiple of our current number, it means it isn't a prime number
            primeNumber = False
            break #We skip the remaining of the loop

    if (primeNumber): #If it's a prime number, we add it to our list of prime numbers and increment the prime numbers counter
        primeNumbersList.append(currentNumber)
        primeNumbersFound = primeNumbersFound + 1

print('The 10001st prime number is: ' + str(currentNumber) + '.') #Once we finish we print the value of the 10001st prime number
