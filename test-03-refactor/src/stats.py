import statistics

# ---- DO NOT MODIFY THIS FILE BEFORE READING THE README ----
# This script is intentionally messy. It works correctly but is hard to read.
# Your job: refactor it into clean functions, then write tests.

data = [4, 8, 15, 16, 23, 42, 4, 8, 15, 4, 16, 23, 42, 8, 4]

s = 0
for x in data:
    s += x
mn = s / len(data)

sd = sorted(data)
n = len(sd)
if n % 2 == 1:
    med = sd[n // 2]
else:
    med = (sd[n // 2 - 1] + sd[n // 2]) / 2

freq = {}
for x in data:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
mx = max(freq.values())
md = [k for k, v in freq.items() if v == mx][0]

var = sum((x - mn) ** 2 for x in data) / len(data)

import math
std = math.sqrt(var)

print(f"Dataset : {data}")
print(f"Mean    : {mn:.2f}")
print(f"Median  : {med}")
print(f"Mode    : {md}")
print(f"Variance: {var:.2f}")
print(f"Std Dev : {std:.2f}")
