# Class vs. Instance

## Problem Statement
Write a Person class with an instance variable, `age` , and a constructor that takes an integer, _initialAge_, as a parameter. The constructor must assign _initialAge_ to `age` after confirming the argument passed as _initialAge_ is not negative; if a negative argument is passed as _initialAge_, the constructor should set `age` to 0 and print **Age is not valid, setting age to 0.**. In addition, you must write the following instance methods:

1. yearPasses() should increase the `age` instance variable by 1.
2. amIOld() should perform the following conditional actions:
    - If `age` < 13, print **You are young.**.
    - If `age` >= 13 and `age` < 18, print **You are a teenager.**.
    - Otherwise, print **You are old.**.

**Sample Input**:
```
4
-1
10
16
18
```

**Sample Output**:
```
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
```
