a=5.08e6
b=5.33e6
c=5.55e6
d=b-a
e=c-b
if d>e:
    trend="decelerating"
else:
    trend="accelerating"
# d=0.25e6, e=0.22e6. d is larger so population growth is decelerating.

X=True
Y=False
W=X or Y
# truth table for W=X or Y
#|X     |Y     |W     |
#|True  |True  |True  |
#|Ture  |False |True  |
#|False |True  |True  |
#|False |False |False |