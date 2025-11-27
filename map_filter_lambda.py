# =========================
# 1️⃣ List Comprehension Exercises
# =========================

# 1. Cubes of numbers 1–5
cubes = [x**3 for x in range(1,6)]
print("Cubes 1-5:", cubes)

# 2. Numbers divisible by 10
nums = [10,15,20,25,30]
div_10 = [x for x in nums if x % 10 == 0]
print("Divisible by 10:", div_10)

# 3. Flatten 2D list
matrix = [[1,2], [3,4], [5,6]]
flat = [j for i in matrix for j in i]
print("Flattened list:", flat)

# 4. Words ending with 'e'
words = ["apple", "cat", "elephant", "orange", "dog"]
words_e = [w for w in words if w.endswith("e")]
print("Words ending with 'e':", words_e)

# 5. Tuples (x, x*x) for numbers 1–4
tuples = [(x, x*x) for x in range(1,5)]
print("Tuples (x, x*x):", tuples)


# =========================
# 2️⃣ Lambda + sorted Exercises
# =========================

# 6. Sort list of tuples by first element
tuples_list = [(3,5), (1,2), (4,1)]
sorted_by_first = sorted(tuples_list, key=lambda x: x[0])
print("Sorted by first element:", sorted_by_first)

# 7. Sort list of strings by length
strings = ["app", "banana", "hi", "computer"]
sorted_by_len = sorted(strings, key=lambda x: len(x))
print("Sorted by length:", sorted_by_len)


# =========================
# 3️⃣ map + filter Exercises
# =========================

# 8. Convert all strings to uppercase
words_lower = ["hello", "hi"]
uppercase = list(map(lambda x: x.upper(), words_lower))
print("Uppercase:", uppercase)

# 9. Keep numbers greater than 50
numbers = [10, 60, 30, 80]
greater_50 = list(filter(lambda x: x > 50, numbers))
print("Numbers > 50:", greater_50)

# 10. Increase each number by 2, keep only even results
nums = [1,2,3,4,5]
even_after_add = list(filter(lambda x: x % 2 == 0, map(lambda x: x + 2, nums)))
print("Even numbers after adding 2:", even_after_add)
