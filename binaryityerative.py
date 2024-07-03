def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main_iterative():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input("Enter the target value: "))
    result = binary_search_iterative(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")

if __name__ == "__main__":
    main_iterative()
