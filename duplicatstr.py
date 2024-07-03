def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def main():
    input_string = input("Enter a string: ")
    result = remove_duplicates(input_string)
    print("String after removing duplicates:", result)

if __name__ == "__main__":
    main()
