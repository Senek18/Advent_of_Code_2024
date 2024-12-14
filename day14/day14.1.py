import re
from PIL import Image
import numpy as np
from tqdm import tqdm

with open("day14/input.txt", "r") as f:
    data = f.read().splitlines()

wide, tall = 101, 103
matrix = [[0] * wide for _ in range(tall)]

def check_boundary(p):
    return p[0] % wide, p[1] % tall


memory_p = []
memory_v = []
for line in data:
    p, v = re.findall(r"-?\d+,-?\d+", line)
    p = list(map(int, p.split(",")))
    v = tuple(map(int, v.split(",")))
    memory_p.append(p)
    memory_v.append(v)


for sec in tqdm(range(10000)):
    im = np.zeros((tall, wide, 3), dtype=np.uint8)
    for idx, (key, value) in enumerate(zip(memory_v, memory_p)):
        value[0] += key[0]
        value[1] += key[1]
        value[0], value[1] = check_boundary(value)
        im[value[1], value[0]] = [255, 0, 0]
        memory_p[idx] = [value[0], value[1]]
    img = Image.fromarray(im, 'RGB')
    img.save(f'day14/seconds/{sec}.png')
