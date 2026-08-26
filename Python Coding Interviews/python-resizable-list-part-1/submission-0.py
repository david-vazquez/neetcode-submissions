from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    out = arr1.copy()
    for num in arr2:
        out.append(num)
    return out


def pop_n(arr: List[int], n: int) -> List[int]:
    if n>=len(arr):
        return []
    out = arr.copy()
    for i in range(n):
        out.pop()
    return out

def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    out = arr.copy()
    if 0 <= index < len(arr):
        out.insert(index, element)
    else:
        out.append(element)
    return out


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
