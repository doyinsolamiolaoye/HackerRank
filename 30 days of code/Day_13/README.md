# Abstract Classes

## Problem Statement
Given a Book class and a Solution class, write a MyBook class that does the following:

- Inherits from Book
- Has a parameterized constructor taking these  parameters:
    1. string 
    2. string 
    3. int 
- Implements the Book class' abstract display() method so it prints these  lines:
    1. `Title`, a space, and then the current instance's `title` .
    2. `Author:` , a space, and then the current instance's `author`.
    3. `Price:`, a space, and then the current instance's .
Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: `public`) when declaring MyBook or your code will not execute.

**Input Format**

You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments). It then calls the display method on the Book object.
**Sample Input**
```
The Alchemist
Paulo Coelho
248
```

**Sample Output**
```
Title: The Alchemist
Author: Paulo Coelho
Price: 248
```
