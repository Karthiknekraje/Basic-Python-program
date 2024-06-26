def complement_of_set(A, U):
    return U - A

# Example usage:
if __name__ == "__main__":
    # Define the universal set U and set A
    U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # Universal set
    A = {2, 4, 6, 8, 10}  # Set A

    # Calculate the complement of A in U
    complement = complement_of_set(A, U)

    # Print the result
    print("Universal Set U:", U)
    print("Set A:", A)
    print("Complement of A in U:", complement)
