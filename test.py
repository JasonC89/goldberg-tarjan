from goldbergtarjan import max_flow

# Test cases

expected = [6, 5]
outputs = []

c = {(0, 1): 3, (0, 2): 15, (1, 3): 8, (3, 2): 9, (3, 4): 8, (2, 4): 11,
     (4, 5): 3, (5, 6): 7, (3, 6): 10}
sum, res = max_flow(c, 0, 6)
outputs.append(sum)

c = {(0, 1): 3, (0, 2): 3, (1, 2): 2, (1, 3): 3, (2, 4): 2, (3, 4): 4,
     (3, 5): 2, (4, 5): 3}
sum, res = max_flow(c, 0, 5)
outputs.append(sum)

for i in range(min([len(outputs), len(expected)])):
    if outputs[i] == expected[i]:
        print("Y")
    else:
        print("F")
