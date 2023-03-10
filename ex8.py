import time
import os

t_start = time.perf_counter()

def memory_usage_psutil():
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

f = open("input.txt")
n = int(f.readline())
a = list(map(int, f.readline().split()))
mf = open("output.txt", "w+")

min_index = 0

for first_index in range(n):
    for i in range(first_index, n):
        if a[i] < a[min_index]:
            min_index = i
    a[first_index], a[min_index] = a[min_index], a[first_index]
    mf.write(f"Swap elements at indices {first_index + 1} and {min_index + 1}\n")

mf.write("No more swaps needed.")
f.close()

print("Время:", time.perf_counter() - t_start)
print("Память:", memory_usage_psutil(), "мб")

mf.close()
