// Task 1: Function to add two numbers
double addTwo(double num1, double num2) {
  return num1 + num2;
}

// Task 2: Function to subtract two numbers
double subtractTwo(double num1, double num2) {
  return num1 - num2;
}

// Task 3: Function to multiply two numbers
double multiplyTwo(double num1, double num2) {
  return num1 * num2;
}

// Task 4: Function to divide two numbers
double divideTwo(double num1, double num2) {
  if (num2 != 0) {
    return num1 / num2;
  } else {
    print('Error: Division by zero');
    return double.infinity; // Return infinity for division by zero
  }
}

// Task 5: Function to get the length of a string
int stringLength(String str) {
  return str.length;
}

// Task 6: Function to get the first element of a list
dynamic getFirstElement(List<dynamic> list) {
  if (list.isNotEmpty) {
    return list[0];
  } else {
    return null; // Return null if the list is empty
  }
}

void main() {
  // Testing the functions
  print('Sum of 5 and 3: ${addTwo(5, 3)}');
  print('Difference of 5 and 3: ${subtractTwo(5, 3)}');
  print('Product of 5 and 3: ${multiplyTwo(5, 3)}');
  print('Quotient of 5 and 3: ${divideTwo(5, 3)}');
  print('Length of "Hello": ${stringLength("Hello")}');
  print('First element of [1, 2, 3]: ${getFirstElement([1, 2, 3])}');
}