# Dictionaries and maps

## Problem Statement
Given `n` names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each `name` queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for `name`  is not found, print `Not found` instead.

**Input Format:**

The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

**Sample Input**:
```
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
```

**Sample Output**:
```
sam=99912222
Not found
harry=12299933
```
