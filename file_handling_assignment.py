try:
    # File Creation
    with open("my_file.txt", "w") as f:
        f.write("This is line 1\n")
        f.write("Line 2: 12345\n")
        f.write("Another line with text\n")

    # File Reading and Display
    with open("my_file.txt", "r") as f:
        print("Contents of my_file.txt:")
        print(f.read())

    # File Appending
    with open("my_file.txt", "a") as f:
        f.write("Appended line 1\n")
        f.write("Line 6: 67890\n")
        f.write("Final appended line\n")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("File handling completed.")