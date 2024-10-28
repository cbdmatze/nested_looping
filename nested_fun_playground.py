def print_triangle(n):
    """
    Prints a triangle pattern with numbers based on the input odd integer n.
    
    Args:
        n (int): An odd integer which determines the height of the triangle.
    """
    if n % 2 == 0:
        print("Please provide an odd number.")
        return

    # Print the upper part of the triangle (including the middle line)
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)))

    # Print the lower part of the triangle
    for i in range(n - 1, 0, -1):
        print(' '.join(str(j) for j in range(1, i + 1)))


print_triangle(5)
print_triangle(3)





def print_triangle(n):
    """
    Prints a triangle pattern with numbers based on the input odd integer n.
    
    Args: n (int): An odd integer which determines the height of the triangle.
    """
    if n % 2 == 0:
        print("Please provide an odd number.")
        return
   
    # Upper part of the triangle
    for i in range(1, (n // 2) + 2):
        for j in range (1, i + 1):
            print(j, end="")
        print()
    
    # Lower part of the triangle
    for i in range(n // 2, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
            print()

print_triangle(5)
print_triangle(3)



def print_multiplication_table(n):
    """
    Pringts a multiplication table for numbers from 1 to n.
    
    Args:
        n (int): The size of the multiplicastion table.
    """
    # Print the header row (top row with numbers 1 to n)
    print(" ", end="") # Leave space for the first column
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
    print() # Move to the next line after the header

    # Print each row of the multiplication table
    for i in range (1, n + 1):
        print(f"{i:2}", end="") # print the row number (left column)
        for j in range (1, n + 1):
            print(f"{i * j:2}", end=" ") # Print the product
        print() # Move to the next line after each row

print_multiplication_table(5)
