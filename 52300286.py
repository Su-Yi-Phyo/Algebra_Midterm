import numpy as np

A = np.random.randint(1,101, size = (10,10))
B = np.random.randint(1,21, size = (2,10))
C = np.random.randint(1,21, size = (10,2))

def ex1a(A, B, C):
    A_transpose = np.transpose(A)
    B_transpose = np.transpose(B)
    C_transpose = np.transpose(C)

    result = A + A_transpose + (np.dot(C,B)) + (np.dot(B_transpose, C_transpose))
    return result

def ex1b(A):
  result = 0
  for i in range(10, 20):
    result += (A / i)**(i - 9)

  return result

def ex1c(A):
  odd_rows = []

  # Iterate over the rows of A and save odd rows
  for i in range(1, A.shape[0], 2):   #start, stop(represents no of rows), step
   odd_rows.append(A[i])

  # Convert the list of odd rows into a numpy array
  odd_rows_matrix = np.array(odd_rows) 
  return  odd_rows_matrix

def ex1d(A):
  flattened_A = A.flatten()
  odd_integer_vector = flattened_A[flattened_A % 2 != 0]
  return odd_integer_vector

def is_prime(num):
  if num == 1:
    return False
  elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           return False
   else:
       return True
       
  # if input number is less than
  # or equal to 1, it is not prime
  else:
   return False

def ex1e(A):
  prime_numbers = []

  # Iterate through each element of matrix A and check for prime numbers
  for row in A:
    for element in row:
        if is_prime(element):
            prime_numbers.append(element)
  return prime_numbers

def ex1f(C,B):
  D = np.dot(C,B)
  print("Original Matrix D \n", D, "\n")
  for i in range(1, D.shape[0], 2):
    D[i] = D[i, ::-1]

  return D

def ex1g(A):
  max_prime_count = 0
  max_prime_rows = []

  for row in A:
    prime_count = 0
    for num in row:
      if is_prime(num):
        prime_count += 1

    
    if prime_count > max_prime_count:
        max_prime_count = prime_count
        max_prime_rows = [row]
    elif prime_count == max_prime_count:
        max_prime_rows.append(row)

  # Print matrix A
  print("Matrix A:")
  print(A)

  # Print rows with maximum count of prime numbers
  print("\nRows with maximum count of prime numbers:")
  for row in max_prime_rows:
    print(row)
    

# Function to find longest contiguous sequence of odd numbers
def longest_contiguous_odd_sequence(row):
    max_length = 0
    current_length = 0
    for num in row:
        if num % 2 == 1:  # Check if the number is odd
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 0
    return max_length

def ex1h(A):
  # Find rows with the longest contiguous sequence of odd numbers
  max_odd_sequence_length = 0
  rows_with_max_sequence = []

  for row in A:
    sequence_length = longest_contiguous_odd_sequence(row)
    if sequence_length > max_odd_sequence_length:
        max_odd_sequence_length = sequence_length
        rows_with_max_sequence = [row]
    elif sequence_length == max_odd_sequence_length:
        rows_with_max_sequence.append(row)

  # Print the rows with the longest contiguous sequence of odd numbers
  print("Rows with the longest contiguous sequence of odd numbers:")
  for row in rows_with_max_sequence:
    print(row)

#main

print("Ex1a: \n")
print(ex1a(A,B,C), "\n")

print("Ex1b: \n")
print(ex1b(A), "\n")

print("Ex1c: \n")
print(ex1c(A), "\n")

print("Ex1d: \n")
print(ex1d(A), "\n")

print("Ex1e: \n")
print(ex1e(A), "\n")

print("Ex1f: \n")
print(ex1f(C,B), "\n")

print("Ex1g: \n")
ex1g(A)

print("\nEx1h: \n")
ex1h(A)