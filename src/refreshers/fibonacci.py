def iterative_fibonacci(n):
  if n < 0:  # reject negative numbers
    return "Invalid input. Please enter a non-negative integer."
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  
  a, b = 0, 1
  for _ in range(2, n + 1):  # iterate from 1 to n + 1
    a, b = b, a + b
  
  return b


def showcase_iterative_fib(n):
  print(f"Checking fib program for n={n}:")
  print(iterative_fibonacci(n))


if __name__ == '__main__':
  showcase_iterative_fib(0)
  showcase_iterative_fib(1)
  showcase_iterative_fib(2)
  showcase_iterative_fib(3)
  showcase_iterative_fib(4)
  showcase_iterative_fib(7)
  showcase_iterative_fib(11)
