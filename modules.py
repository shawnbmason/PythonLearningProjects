# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1, 100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

# ---------------------------------------------------------------------------------------------

import codecademylib3_seaborn
import random
# Add your code below:
from matplotlib import pyplot as plt

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

# outputs [489, 446, 104, 49, 654, 953, 691, 748, 532, 971, 482, 479]
print(numbers_b)

plt.plot(numbers_a, numbers_b)
# outputs [854, 680, 521, 966, 959, 719, 841, 278, 402, 806, 835, 654]
# plot these number sets against each other using plt

plt.show()
# shows a graph of random numbers. 
# You’ve used two Python modules to accomplish this (random and matplotlib).

# ----------------------------------------------------------------------------------------

from decimal import Decimal

two_decimal_points = Decimal("0.10") + Decimal("0.35")
# Returns 0.45 instead of 0.44999999999999996
print(two_decimal_points)