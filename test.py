from goldbergtarjan import max_flow

# Test cases

expected = [6, 5, 15, 14, 120]
outputs = []

c = {(0, 1): 3, (0, 2): 15, (1, 3): 8, (3, 2): 9, (3, 4): 8, (2, 4): 11,
     (4, 5): 3, (5, 6): 7, (3, 6): 10}
sum, res = max_flow(c, 0, 6)
outputs.append(sum)

c = {(0, 1): 3, (0, 2): 3, (1, 2): 2, (1, 3): 3, (2, 4): 2, (3, 4): 4,
     (3, 5): 2, (4, 5): 3}
sum, res = max_flow(c, 0, 5)
outputs.append(sum)

c = {(0, 1): 10, (0, 2): 5, (1, 2): 15, (1, 3): 5, (2, 3): 10}
sum, res = max_flow(c, 0, 3)
outputs.append(sum)

c = {(0, 1): 4, (0, 2): 6, (0, 3): 5, (1, 2): 1, (2, 1): 1, (2, 3): 2,
     (3, 2): 2, (3, 5): 5, (2, 5): 4, (2, 4): 5, (1, 4): 7,
     (4, 5): 1, (5, 4): 1, (4, 6): 6, (5, 6): 8}
sum, res = max_flow(c, 0, 6)
outputs.append(sum)

c = {(0, 1): 90, (0, 3): 110, (1, 2): 60, (3, 1): 10, (1, 4): 30, (3, 4): 30,
     (2, 4): 40, (2, 5): 50, (4, 5): 100}
sum, res = max_flow(c, 0, 5)
outputs.append(sum)

for i in range(min([len(outputs), len(expected)])):
    if outputs[i] == expected[i]:
        print("Y")
    else:
        print("F")
