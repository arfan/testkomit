import time
from tqdm import tqdm

total = 0
for i in tqdm(range(1, 10)):
	x = i * i
	total = total + x
	time.sleep(1)

print("total", total)

