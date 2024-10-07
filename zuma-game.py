import random
import time

colors = ['R', 'G', 'B', 'Y']
queue = []

for i in range(10):
    queue.append(random.choice(colors))

shooter = random.choice(colors)
pit = False

while not pit:
    print("Queue: ", ' '.join(queue))
    print("shooter: ", shooter)

    position = int(input(f'Enter position to shoot (0 to {len(queue)}): '))
    queue.insert(position, shooter)
    shooter = random.choice(colors)

    i = 0
    while i < len(queue) - 2:
        if queue[i] == queue[i+1] == queue[i+2]:
            del queue[i:i+3]
        else:
            i += 1

    if len(queue) > 0:
        queue.pop(0)
    if len(queue) == 2:
        pit = True


    time.sleep(1)

print("Game Over! Balls reached the pit.")

