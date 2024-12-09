import random

list_ = []
for i in range(random.randint(5, 10)):
    list_.append(random.randint(0, 10))
print(list_)

selected_num = random.randint(1, 6)
print(selected_num)

def find_sum(target, li):
    for i in li:
       for j in li:
           if i + j == target:
               return (i, j)
# С‡Р°СЃ = O(n^2)
# РїСЂРѕСЃС‚С–СЂ O(1)
print(find_sum(selected_num, list_))


def find_sum_fast(target, li):
    li.sort()
    zauvi = set()

    for num in li:
        riz = target - num
        if riz in zauvi:
            return (num, riz)
        zauvi.add(num)

    return None
# С‡Р°СЃ = O(nlogn)
# РїСЂРѕСЃС‚С–СЂ O(n)

print(find_sum(selected_num, list_))