import matplotlib.pyplot as plt
from die import Die


# Create a couple of dice
d1 = Die()
d2 = Die()

results = list()
for roll in range(5000):
    results.append(d1.roll_die() + d2.roll_die())

frequencies = list()
max_result = d1.num_sides + d2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = [x for x in range(2, max_result + 1)]

fig, ax = plt.subplots()
ax.barh(x_values, frequencies)

ax.set_title("Frequency a number is rolled from a pair of D6 dice.")
ax.set_xlabel("Frequency", fontsize=14)
ax.set_ylabel("Dice number", fontsize=14)
ax.tick_params(axis="both", labelsize=14)
plt.show()