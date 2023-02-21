import random
import time
from random_words import RandomWords

#створюэмо списки
int_list = [random.randint(0, 1000) for i in range(5000)]
float_list = [random.uniform(0.1, 100.0) for i in range(5000)]
rw = RandomWords()
str_list = rw.random_words(count=5000)

#створюжмо функцію сортування (сортування вставками)
def insertion_sort(list):
    #count = 0
    for i in range(1, len(list)):
        for j in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
                #count +=1
            else:
                break
    return list

#створюємо функцію, яка буде розраховувати середній час сортування
def insertion_sorting_time(func, list, iterations):
    total_time = 0
    for i in range(iterations):
        start_time = time.time()
        func(list)
        end_time = time.time()
        total_time +=(end_time - start_time)
    average_time = total_time / iterations
    return average_time

int_sorting_time = insertion_sorting_time(insertion_sort, int_list, 10)
float_sorting_time = insertion_sorting_time(insertion_sort, float_list, 10)
str_sorting_time = insertion_sorting_time(insertion_sort, str_list, 10)

print(f'Середній час сортування float-списку: {float_sorting_time:.10f}')
print(f'Середній час сортування int-списку: {int_sorting_time:.10f}')
print(f'Середній час сортування str-списку: {str_sorting_time:.10f}')

#print(insertion_sort(int_list))
#print(insertion_sort(float_list))
#print(insertion_sort(str_list))

