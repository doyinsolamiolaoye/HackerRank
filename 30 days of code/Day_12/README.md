# Inheritance

## Problem Statement
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

- A Student class constructor, which has `A` parameters:
    1. A string, `firstName`.
    2. A string, `lastName`.
    3. An integer, `id` .
    4. An integer array (or vector) of test scores, `scores`.
- A char `calculate()` method that calculates a Student object's average and returns the grade character representative of their calculated average:


**Input Format**

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains `firstName`, `lastName`, and `id`, respectively. The second line contains the number of test scores. The third line of space-separated integers describes `scores`.

**Sample Input**
```
Heraldo Memelli 8135627
2
100 80
```

**Sample Output**
```
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
```
