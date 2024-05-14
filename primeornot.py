def Prime(n):  
    # Checking that n is more than 1  
    if n > 1:  
        # Iterating over the n  
        for i in range(2, int(n/2) + 1):  
            # If n is divisible or not  
            if (n % i) == 0:  
                print(n, "is not a prime number")  
                break  
        else:  
            print(n, "is a prime number")  
    # If n is 1  
    else:  
        print(n, "is not a prime number")  
        
# Taking an input from the user  
num = int(input("Enter an input number:"))
# Printing result  
Prime(num)