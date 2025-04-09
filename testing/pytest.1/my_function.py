import sys

def add(x, y):
  """Add two numbers and return the result.
     Any exception will be thrown to the caller"""
  return int(x) + int(y)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python add.py <number1> <number2>")
  else:
    result = add(sys.argv[1], sys.argv[2])
    print(f"SUM is {result}")
