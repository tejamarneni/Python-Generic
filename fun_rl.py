import random

val = 0
neg = 0
pos = 0
learning_rate = 1

direction = ['E','W','N','S']

while val <= 10:
    ch = random.choice(direction)
    print(ch)
    if ch in ('E','N'):
        val += learning_rate
        pos += 2
    else:
        val -= learning_rate
        neg -= 1

print("pos:",pos)
print("neg:",neg)
