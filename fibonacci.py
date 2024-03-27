def fibonacci(n):
 if n <= 1:
     return n
 else:
     a, b = 0, 1
     for _ in range(2, n +1):
         c = a +b
         a, b = b, c
         return b 
     
    num_terms = input("Enter the number of terms: ")
    
    fibonacci_sequence = []
    for i in range(num_terms):
        fibonacci_sequence.append(fibonacci(i))