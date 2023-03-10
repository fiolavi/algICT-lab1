import time
import os
from math import log2

t_start = time.perf_counter()

def memory_usage_psutil():
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

f = open("input.txt")
n = int(f.readline())
people = list(map(float, f.readline().split()))
people_tuple = [(people[0], 1)]

for i in range(1, n):
    left, right = 0, len(people_tuple)

    if people[i] <= people_tuple[0][0]: #самый бедный
        people_tuple = [(people[i], i + 1)] + people_tuple
    elif people[i] >= people_tuple[-1][0]: #самый богатый
        people_tuple = people_tuple + [(people[i], i + 1)]
    else:
        for _ in range(int(log2(n)) + 1): #берем худший случай
            temp_index = (left + right) // 2 #среднее арифмитическое

            if people[i] > people_tuple[temp_index][0]: #сужение границ
                left = temp_index
            elif people[i] < people_tuple[temp_index][0]:
                right = temp_index
            else: #если число = числу
                left, right = temp_index, temp_index - 1
                break

        insert_index = (left + right + 1) // 2 #место куда надо вставить число
        people_tuple.insert(insert_index, (people[i], i + 1)) #впихиваем элемент и двигаем остальные вправо

mf = open("output.txt", "w+")
mf.write(str(people_tuple[0][1]) + ' ' + str(people_tuple[n // 2][1]) + ' ' + str(people_tuple[-1][1]))
mf.close()

print("Время:", time.perf_counter() - t_start)
print("Память:", memory_usage_psutil(), "мб")

f.close()
