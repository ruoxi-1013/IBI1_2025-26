# What does this piece of code do?
# Answer: Generate 11 random numbers between 1 and 10, then calculate their sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
# Initialise a variable to store the sum of all random numbers
total_rand = 0
# Initialise a counter variable to track the number of generated random numbers
progress=0
#Loop until the counter reaches 10 (run 11 times in total)
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n
#Print the final sum of all random numbers
print(total_rand)

