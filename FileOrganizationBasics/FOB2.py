with open("file.txt") as f:                 # No need of using f.close()
    print(f.read())

# Opens 'file.txt' to read its contents.
# Raises FileNotFoundError if 'file.txt' does not exist.
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# Creates 'file.txt' if it doesn't exist. 
# WARNING: If it exists, it completely overwrites/erases it.
with open("file.txt", "w") as f:
    f.write("This will replace all existing text.")

# Creates 'file.txt' if it doesn't exist.
# If it exists, it keeps the old text and adds new text to the end.
with open("file.txt", "a") as f:
    f.write("\nThis line is added at the end.")

# Creates a brand new 'file.txt' and opens it for writing.
# Throws FileExistsError if 'file.txt' already exists in the folder.
with open("file.txt", "x") as f:
    f.write("Fresh new file content.")



# Opens an EXISTING file. (Throws error if 'file.txt' is missing).
# Allows you to read first, then write, without erasing the entire file.
with open("file.txt", "r+") as f:
    content = f.read()   # Read current contents
    print(content)
    f.write("\nAdding text to the end.") # Write new content

# Overwrites/erases 'file.txt' immediately upon opening.
# Allows you to write data and then read it back immediately.
with open("file.txt", "w+") as f:
    f.write("New data stream.")
    
    f.seek(0)            # Move the pointer back to the beginning to read!
    print(f.read())

# Opens file for adding data at the very end without deleting anything.
# Allows you to read, but the initial pointer starts at the END of the file.
with open("file.txt", "a+") as f:
    f.write("\nAppending a new entry.")
    
    f.seek(0)            # Move pointer to the start so we can read the whole file
    print(f.read())