# Question 1: Write a Python program to open a file named "my_file.txt" in read mode and print its contents to the console. Handle the FileNotFoundError exception if the file does not exist.

try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")


# Question 2: Write a Python program to write the string "Hello, world!" to a file named "output.txt".

try:
    with open("output.txt", "w") as file:
        file.write("Hello, world!")
    print("Successfully wrote to output.txt")
except Exception as e:
    print(f"An error occurred: {e}")


# Question 3: Write a Python program to append the string "This is a new line." to the end of the file "output.txt".

try:
    with open("output.txt", "a") as file:
        file.write("\nThis is a new line.")
    print("Successfully appended to output.txt")
except Exception as e:
    print(f"An error occurred: {e}")


# Question 4: Write a Python program to read a file line by line and print each line to the console. Handle potential IOError exceptions.

try:
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())  # Remove leading/trailing whitespace
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 5: Write a Python program to read a file and count the number of words in it.

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"The file contains {word_count} words.")
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 6: Write a Python program to copy the contents of one file ("source.txt") to another file ("destination.txt"). Handle FileNotFoundError and IOError exceptions.

try:
    with open("source.txt", "r") as source_file, open("destination.txt", "w") as dest_file:
        for line in source_file:
            dest_file.write(line)
    print("File copied successfully.")
except FileNotFoundError as e:
    print(f"Error: One or both files not found: {e}")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 7: Write a Python program to read a CSV file ("data.csv") and print each row as a list. Assume the CSV file is comma-separated. Handle FileNotFoundError and IOError exceptions.

import csv

try:
    with open("data.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("Error: The file 'data.csv' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 8: Write a Python program to write a list of dictionaries to a CSV file ("output.csv"). The keys of the dictionaries should be the header row.

import csv

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]

try:
    with open("output.csv", "w", newline="") as file:
        fieldnames = data[0].keys()  # Get keys from the first dictionary
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("CSV file written successfully.")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 9: Write a Python program that takes user input for a number and attempts to convert it to an integer. Handle the ValueError exception if the input is not a valid integer.

try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# Question 10: Write a Python program that divides two numbers entered by the user. Handle the ZeroDivisionError exception if the second number is zero.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")


# Question 11: Write a Python program that attempts to access an element at a specific index in a list. Handle the IndexError exception if the index is out of bounds.

my_list = [1, 2, 3, 4, 5]
try:
    index = int(input("Enter an index: "))
    value = my_list[index]
    print(f"The value at index {index} is: {value}")
except IndexError:
    print("Error: Index out of bounds.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer index.")


# Question 12: Write a Python program that attempts to open a file and read its contents. Use a finally block to ensure that the file is closed, regardless of whether an exception occurs.

file = None  # Initialize file to None
try:
    file = open("my_file.txt", "r")
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
finally:
    if file:
        file.close()
        print("File closed.")


# Question 13: Write a Python program that raises a custom exception called InvalidAgeError if the user enters an age less than 0.

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    print(f"Your age is: {age}")
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer age.")


# Question 14: Write a Python program that reads a file and handles multiple exceptions (e.g., FileNotFoundError, IOError) using a single except block with a tuple of exception types.

try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except (FileNotFoundError, IOError) as e:
    print(f"An error occurred: {e}")


# Question 15: Write a Python program that uses the else block in a try-except statement. The else block should execute only if no exceptions occur in the try block. The program should read a number from the user and print its square.

try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    square = num ** 2
    print(f"The square of {num} is: {square}")


# Question 16: Write a Python program that reads a file and prints the first 10 characters. Handle FileNotFoundError and IndexError (if the file is shorter than 10 characters).

try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents[:10])  # Print the first 10 characters
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except IndexError:
    print("Error: The file is shorter than 10 characters.")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 17: Write a Python program that reads a file and converts each line to uppercase before printing it. Handle FileNotFoundError and IOError.

try:
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip().upper())
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")


# Question 18: Write a Python program that reads a file containing numbers (one number per line) and calculates their sum. Handle FileNotFoundError, IOError, and ValueError (if a line is not a valid number).

total = 0
try:
    with open("numbers.txt", "r") as file:
        for lince in file:
            try:
                number = float(line.strip())
                total += number
            except ValueError:
                print(f"Warning: Invalid number found in line: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
finally:
    print(f"The sum of the valid numbers is: {total}")


# Question 19: Write a Python program that prompts the user for a filename, opens the file, and prints its contents. Use a while loop to repeatedly prompt the user until a valid filename is entered. Handle FileNotFoundError

while True:
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            conteaqnts = file.read()
            print(contents)
        break  # Exit the loop if the file is opened successfully
    except FileNotFoundError:
        print("Error: File not found. Please try again.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        break # Exit the loop if there is an I/O error



# Question 20: Write a Python program that reads a JSON file ("data.json") and prints the data. Handle FileNotFoundError, IOError, and json.JSONDecodeError.

import json

try:
    with open("data.json", "r") as file:
        data = json.qaload(file)
        print(data)
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
