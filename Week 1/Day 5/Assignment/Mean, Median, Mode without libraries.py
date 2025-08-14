# Mean, Median, Mode without libraries

scores = [85, 90, 75, 85, 92, 88, 75, 90, 90, 100]

# Mean
mean = sum(scores) / len(scores)

# Median
sorted_scores = sorted(scores)
n = len(sorted_scores)
if n % 2 == 1:
    median = sorted_scores[n // 2]
else:
    median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

# Mode
freq = {}
for num in scores:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.values())
mode = [num for num, count in freq.items() if count == max_freq]

# Output
print(f"Scores: {scores}")
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Mode: {mode}")
