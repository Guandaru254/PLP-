// Dart program demonstrating data types

void main() {
  // Example of int data type
  int age = 25;
  print('Age: $age');

  // Example of double data type
  double height = 5.9;
  print('Height: $height');

  // Example of String data type
  String name = 'John Doe';
  print('Name: $name');

  // Example of List data type
  List<int> numbers = [1, 2, 3, 4, 5];
  print('Numbers: $numbers');

  // Example of accessing elements in a List
  print('First number: ${numbers[0]}');
  print('Last number: ${numbers[numbers.length - 1]}');

  // Example of Map data type
  Map<String, dynamic> person = {
    'name': 'Alice',
    'age': 30,
    'isEmployed': true
  };
  print('Person: $person');

  // Example of accessing values in a Map
  print('Name: ${person['name']}');
  print('Age: ${person['age']}');
  print('Is Employed? ${person['isEmployed']}');
}