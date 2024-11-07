# Applicable

## Problem 1
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
[-0.  3.  9.  7.  8. 12. 15.]
Vogel’s approximation method:
[-0. -5. -2. -1.  0.  1.  2.]
Russell’s approximation method:
[-0. -4. -2. -0.  0.  1.  4.]
```

## Problem 2
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
[ -0.  -0. -30.  19.  30.  40. -10.]
Vogel’s approximation method:
[ -0. -50. -10.  19.  -2. -10.  10.]
Russell’s approximation method:
[-0. -0. 22. 19. 30. 40. 42.]
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

```
140 180 160
2 3 4 2 
8 4 1 4 
9 7 3 7 
100 120 160 100
```
Answer: `The method is not applicable!`
