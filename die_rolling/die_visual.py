from die import Die

# create D6
die = Die()

# make some rolls, store results in list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
