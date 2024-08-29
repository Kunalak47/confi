def print_pattern(rows):
  """Prints a number pattern in the shape of a pyramid.

  Args:
    rows: The number of rows in the pyramid.
  """
  for i in range(1, rows + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(rows)