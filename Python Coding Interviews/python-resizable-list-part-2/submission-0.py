from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    out = arr1.copy()
    out.extend(arr2)
    return out
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    out = arr1
    for num in arr2:
        if num in out:
            out.remove(num)
    return out


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
