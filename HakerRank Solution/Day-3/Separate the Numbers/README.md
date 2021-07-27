# Seperate the  Numbers

## Description

A numeric string, , is beautiful if it can be split into a sequence of two or more positive integers, , satisfying the following conditions:

for any  (i.e., each element in the sequence is  more than the previous element).


No  contains a leading zero. For example, we can split  into the sequence , but it is not beautiful because  and  have leading zeroes.

The contents of the sequence cannot be rearranged. 
For example, we can split  into the sequence , but it is not beautiful because it breaks our first constraint (i.e., ).
The diagram below depicts some beautiful strings:

Perform  queries where each query consists of some integer string . F
or each query, print whether or not the string is beautiful on a new line. 
If it is beautiful, print YES x, where  is the first number of the increasing sequence. 
If there are multiple such values of , choose the smallest. Otherwise, print NO.

## Function Description

Complete the separateNumbers function in the editor below.

separateNumbers has the following parameter:

s: an integer value represented as a string

**Prints**

- string: Print a string as described above. Return nothing.

**Input Format**

The first line contains an integer q, the number of strings to evaluate.

Each of the next q lines contains an integer string s to query.

**Constraints**

1 < q <= 10

1 < |s| <= 32

s[i] E [0-9]

## Sample Input 0

7
1234
91011
99100
101103
010203
13
1

## Sample Output 0

YES 1
YES 9
YES 99
NO
NO
NO
NO

## Solution

[Seperate the numbers](https://github.com/rammya29/Tech-And-Target/blob/main/HakerRank%20Solution/Day-3/Separate%20the%20Numbers/solution.py)
