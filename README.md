goldberg-tarjan
===============

boring one this time, goldberg-tarjan implementation for max flow problem in Python

Usage
-----

```python
from goldbergtarjan import max_flow
# Define all edges (implicit nodes) together with their maximum capacity
c = {(0, 1): 3, (0, 2): 15, (1, 3): 8, (3, 2): 9, (3, 4): 8, (2, 4): 11,
     (4, 5): 3, (5, 6): 7, (3, 6): 10}
flow, network = max_flow(c, 0, 6) # Calculate the max flow for the network
                                  # with source 0 and target 6
```

