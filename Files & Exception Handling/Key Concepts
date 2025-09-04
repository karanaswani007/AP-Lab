**I. File Handling Concepts**

1.  **File Modes:**

    *   **`'r'` (Read Mode):** Opens a file for reading. The file pointer is placed at the beginning of the file. If the file does not exist, it raises a `FileNotFoundError`.
    *   **`'w'` (Write Mode):** Opens a file for writing. If the file exists, its contents are truncated (deleted). If the file does not exist, a new file is created.
    *   **`'a'` (Append Mode):** Opens a file for appending. The file pointer is placed at the end of the file. If the file exists, new data is added to the end. If the file does not exist, a new file is created.
    *   **`'x'` (Exclusive Creation Mode):** Creates a new file for writing. If the file already exists, it raises a `FileExistsError`.
    *   **`'b'` (Binary Mode):** Used in conjunction with other modes (e.g., `'rb'`, `'wb'`) to open a file in binary mode. This is important for handling non-text files like images or audio.
    *   **`'t'` (Text Mode):** The default mode. Used to open a file as a text file.
    *   **`'+'` (Updating Mode):** Used in conjunction with other modes (e.g., `'r+'`, `'w+'`, `'a+'`) to open a file for both reading and writing/appending.

2.  **Opening and Closing Files:**

    *   **`open(filename, mode)`:** The built-in function used to open a file. It returns a file object.
    *   **`file.close()`:**  Closes the file. It's crucial to close files to release system resources and ensure that any buffered data is written to disk.
    *   **`with open(filename, mode) as file:`:**  The preferred way to open files. The `with` statement automatically closes the file when the block of code is finished, even if exceptions occur. This ensures proper resource management.

3.  **Reading File Contents:**

    *   **`file.read()`:** Reads the entire contents of the file as a single string.
    *   **`file.readline()`:** Reads a single line from the file, including the newline character (`\n`).
    *   **`file.readlines()`:** Reads all lines from the file and returns them as a list of strings.
    *   **Iterating through a file:**  You can iterate through a file object directly using a `for` loop, which reads the file line by line: `for line in file:`.

4.  **Writing to Files:**

    *   **`file.write(string)`:** Writes a string to the file.  It does *not* automatically add a newline character.
    *   **`file.writelines(list_of_strings)`:** Writes a list of strings to the file.  It does *not* automatically add newline characters.

5.  **File Pointers:**

    *   The file pointer indicates the current position in the file where the next read or write operation will occur.
    *   **`file.seek(offset, whence)`:**  Moves the file pointer to a specific position. `offset` is the number of bytes to move, and `whence` specifies the reference point (0: beginning of file, 1: current position, 2: end of file).
    *   **`file.tell()`:** Returns the current position of the file pointer.

6.  **File Paths:**

    *   **Relative Paths:**  Paths relative to the current working directory (e.g., `"my_file.txt"`, `"data/input.txt"`).
    *   **Absolute Paths:**  Full paths that specify the exact location of the file on the file system (e.g., `"/home/user/documents/my_file.txt"` on Linux/macOS, `"C:\\Users\\User\\Documents\\my_file.txt"` on Windows).
    *   **`os.path` module:**  Provides functions for manipulating file paths in a platform-independent way (e.g., `os.path.join()`, `os.path.abspath()`, `os.path.exists()`).

7.  **CSV File Handling (using the `csv` module):**

    *   **`csv.reader(file)`:** Creates a reader object that allows you to iterate over rows in a CSV file.
    *   **`csv.writer(file)`:** Creates a writer object that allows you to write data to a CSV file.
    *   **`csv.DictReader(file)`:** Creates a reader object that treats each row as a dictionary, using the first row as the header (keys).
    *   **`csv.DictWriter(file, fieldnames)`:** Creates a writer object that writes dictionaries to a CSV file, using `fieldnames` as the header row.
    *   **`reader.writerow(row)`:** Writes a single row to the CSV file.
    *   **`reader.writerows(rows)`:** Writes multiple rows to the CSV file.
    *   **`newline=''`:**  Important when opening a CSV file for writing to prevent extra blank rows from being inserted (especially on Windows).

8.  **JSON File Handling (using the `json` module):**

    *   **`json.load(file)`:** Reads a JSON file and parses it into a Python object (usually a dictionary or list).
    *   **`json.dump(data, file)`:** Writes a Python object to a JSON file.
    *   **`json.dumps(data)`:** Converts a Python object to a JSON string.
    *   **`json.loads(json_string)`:** Parses a JSON string into a Python object.

**II. Exception Handling Concepts**

1.  **`try-except` Blocks:**

    *   The `try` block contains the code that might raise an exception.
    *   The `except` block(s) contain the code that handles specific exceptions.
    *   You can have multiple `except` blocks to handle different exception types.
    *   If an exception occurs in the `try` block, Python looks for a matching `except` block. If a match is found, the code in that `except` block is executed. If no match is found, the exception propagates up the call stack.

2.  **Specific Exception Types:**

    *   **`FileNotFoundError`:** Raised when a file cannot be found.
    *   **`IOError`:** A general exception for input/output errors.  Can be more specific like `BlockingIOError`, `TimeoutError`, etc.
    *   **`ValueError`:** Raised when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert `"abc"` to an integer).
    *   **`ZeroDivisionError`:** Raised when you try to divide by zero.
    *   **`IndexError`:** Raised when you try to access an element in a list or tuple using an invalid index.
    *   **`TypeError`:** Raised when an operation or function is applied to an object of inappropriate type.
    *   **`KeyError`:** Raised when you try to access a dictionary key that does not exist.
    *   **`ImportError`:** Raised when an import statement fails to find the module definition.
    *   **`OSError`:** Raised for operating system-related errors.
    *   **`json.JSONDecodeError`:** Raised when there is an error decoding a JSON string or file.

3.  **`finally` Block:**

    *   The `finally` block is executed *always*, regardless of whether an exception occurred in the `try` block or not.
    *   It's typically used to clean up resources (e.g., closing files, releasing locks).

4.  **`else` Block:**

    *   The `else` block is executed only if *no* exceptions occurred in the `try` block.
    *   It's useful for code that should only run if the `try` block completed successfully.

5.  **Raising Exceptions:**

    *   **`raise Exception("Error message")`:**  Raises a specific exception. You can create your own exception classes or use built-in exception types.
    *   You can re-raise an exception in an `except` block to propagate it up the call stack: `raise`.

6.  **Custom Exceptions:**

    *   You can create your own exception classes by inheriting from the built-in `Exception` class or one of its subclasses.
    *   This allows you to define specific error conditions that are relevant to your application.

7.  **Handling Multiple Exceptions:**

    *   You can handle multiple exception types in a single `except` block by specifying them as a tuple: `except (FileNotFoundError, IOError) as e:`.

8.  **Exception Objects:**

    *   When an exception is raised, an exception object is created.
    *   You can access the exception object in the `except` block using the `as` keyword: `except ValueError as e:`.
    *   The exception object contains information about the error, such as the error message.

9.  **`try...except...else...finally` Structure:**

    ```python
    try:
        # Code that might raise an exception
    except ExceptionType1 as e1:
        # Handle ExceptionType1
    except ExceptionType2 as e2:
        # Handle ExceptionType2
    else:
        # Code to execute if no exceptions occurred in the try block
    finally:
        # Code to execute regardless of whether an exception occurred
    ```

**III. General Programming Concepts**

*   **Input Validation:**  Checking user input to ensure that it's valid before processing it.
*   **String Manipulation:**  Using string methods like `strip()`, `upper()`, `split()`.
*   **Data Structures:**  Working with lists, dictionaries, and other data structures.
*   **Loops:**  Using `for` and `while` loops to iterate over data.
*   **Functions:**  Defining and calling functions to organize code.
*   **Modules:**  Importing and using modules like `csv`, `json`, and `os`.
