import numpy as np

data = np.loadtxt('input.txt', dtype=int)
column1 = data[:, 0].tolist()
column2 = data[:, 1].tolist()

#Part 1 - 1941353
print("Part 1 -", np.sum(np.abs(np.array(sorted(column1)) - np.array(sorted(column2)))))

#Part 2 - 22539317
print("Part 2 -", sum([column1.count(num) * column2.count(num) * num for num in set(column1)]))