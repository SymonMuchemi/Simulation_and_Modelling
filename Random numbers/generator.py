import random

random_number = random.randint(0, 9)
random_number2 = random.random()
uniformNumber = random.uniform(0, 9)
sample = random.sample(range(0, 90), 12)
rangeNumber = random.randrange(0, 9, 2)         


print(random_number)
print(random_number2)
print(uniformNumber)
print(sample)
print(sample.sort())
print(rangeNumber)
