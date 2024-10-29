# Applicable

## Problem 1
Lab 7 problem 1 (NW)
```
140 180 160
2 3 4 2 
8 4 1 4 
9 7 3 7 
100 120 160 100
```
Answer: 
```
          B1    B2    B3    B4    Supply
------  ----  ----  ----  ----  --------
A1         2     3     4     2       140
A2         8     4     1     4       180
A3         9     7     3     7       160
Demand   100   120   160   100       480

North-West Corner method:
['100 * A1B1 (2)', '40 * A1B2 (3)', '80 * A2B2 (4)', '100 * A2B3 (1)', '60 * A3B3 (3)', '100 * A3B4 (7)']
Vogel’s approximation method:
['100 * A1B1 (2)', '160 * A3B3 (3)', '40 * A1B4 (2)', '120 * A2B2 (4)', '60 * A2B4 (4)']
Russell’s approximation method:
['100 * A1B1 (2)', '40 * A1B4 (2)', '120 * A2B2 (4)', '60 * A2B4 (4)', '160 * A3B3 (3)']
```

## Problem 2
Lab 7 problem 3 (Vogel)
```
160 140 170
7 8 1 2 
4 5 9 8 
9 2 3 6
120 50 190 110
```
Answer: 
```
          B1    B2    B3    B4    Supply
------  ----  ----  ----  ----  --------
A1         7     8     1     2       160
A2         4     5     9     8       140
A3         9     2     3     6       170
Demand   120    50   190   110       470

North-West Corner method:
['120 * A1B1 (7)', '40 * A1B2 (8)', '10 * A2B2 (5)', '130 * A2B3 (9)', '60 * A3B3 (3)', '110 * A3B4 (6)']
Vogel’s approximation method:
['110 * A1B4 (2)', '50 * A1B3 (1)', '140 * A3B3 (3)', '30 * A3B2 (2)', '120 * A2B1 (4)', '20 * A2B2 (5)']
Russell’s approximation method:
['160 * A1B3 (1)', '30 * A3B3 (3)', '120 * A2B1 (4)', '50 * A3B2 (2)', '20 * A2B4 (8)', '90 * A3B4 (6)']
```

## Problem 3
[Link](https://cbom.atozmath.com/example/CBOM/Transportation.aspx?q=ram) (Russel)
```
7   9   18
19	30	50	10	
70	30	40	60
40	8	70	20
5	8	7	14
```
Answer: 
```
          B1    B2    B3    B4    Supply
------  ----  ----  ----  ----  --------
A1        19    30    50    10         7
A2        70    30    40    60         9
A3        40     8    70    20        18
Demand     5     8     7    14        34

North-West Corner method:
['5 * A1B1 (19)', '2 * A1B2 (30)', '6 * A2B2 (30)', '3 * A2B3 (40)', '4 * A3B3 (70)', '14 * A3B4 (20)']
Vogel’s approximation method:
['8 * A3B2 (8)', '5 * A1B1 (19)', '10 * A3B4 (20)', '2 * A1B4 (10)', '7 * A2B3 (40)', '2 * A2B4 (60)']
Russell’s approximation method:
['14 * A3B4 (20)', '5 * A1B1 (19)', '4 * A3B2 (8)', '2 * A1B2 (30)', '2 * A2B2 (30)', '7 * A2B3 (40)']
```

# Not balanced
```
140 180 150
2 3 4 2 
8 4 1 4 
9 7 3 7 
70 120 130 100
```
Answer: `The problem is not balanced!`

# Not applicable
```
7   9   18
19	30	50	10	
70	30	40
40	8	70	20
5	8	7	14
```
Answer: `The method is not applicable!`
