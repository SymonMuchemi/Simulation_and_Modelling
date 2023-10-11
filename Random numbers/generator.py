import random

random_number = random.randint(0, 9)
random_number2 = random.random()
uniformNumber = random.uniform(0, 9)
sample = random.sample(range(10, 20), 10)
rangeNumber = random.randrange(0, 9, 2)         

def myFunc(e):
    return (e)


print(random_number)
print(random_number2)
print(uniformNumber)
print(sample)
print(sample.sort(key=myFunc))
print(rangeNumber)
