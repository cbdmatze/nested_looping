def print_triangle(n):
    """
    Prints a triangle of numbers with size n (n should be odd).
   
    Args:
        n (int): The size of the triangle (must be an odd number).
    """
    for i in range(1, n + 1):
        print(" ".join(map(str, range(1, i + 1))))
    for i in range (n - 1, 0, -1):
        print(" ".join(map(str, range(1, i + 1))))


def print_multiplication_table(n):
    """
    Prints a multiplication table for numbers from 1 to n.
    
    Args:
        n (int): The size of the multiplication table.
    """
    # Print the header row (top row with numbers 1 to n)
    print("  ", end="")  # Leave space for the first column
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
    print()  # Move to the next line after the header
    
    # Print each row of the multiplication table
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")  # Print the row number (left column)
        for j in range(1, n + 1):
            print(f"{i * j:2}", end=" ")  # Print the product
        print()  # Move to the next line after each row


def main():
    # Ask the user for a number
    number = int(input("Please enter a number: "))

    # Ask the user for a command (triangle or mp)
    command = input("Please enter command (triangle/mp): ").strip().lower()

    # Execute the appropriate command
    if command == "triangle":
        print_triangle(number)
    elif command == "mp":
        print_multiplication_table(number)
    else:
        print("Invalid comman. Please enter 'triangle' or 'mp'.")


if __name__ == "__main__":
    main()