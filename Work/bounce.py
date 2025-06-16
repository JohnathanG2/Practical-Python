# bounce.py

ball_height = 100.0

for i in range(10):
    ball_height *= 3/5
    print(i + 1, "Current ball height is", round(ball_height, 4))
    