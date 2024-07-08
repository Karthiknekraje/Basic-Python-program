def linear_search(arr, target):
    """
    Perform a linear search for the target in the list arr.
    
    Args:
        arr (list): The list to search in.
        target (int/float/str): The element to search for.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def main():
    arr = [10, 23, 45, 70, 11, 15]
    target = int(input("Enter the number you want to search for: "))
    
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"The number {target} is at index {result}.")
    else:
        print(f"The number {target} is not in the list.")

if __name__ == "__main__":
    main()
