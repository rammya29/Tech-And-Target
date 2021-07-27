# Cats and a Mouse
## Description
Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given  queries in the form of , , and  representing the respective positions for cats  and , and for mouse . Complete the function  to return the appropriate answer to each query, which will be printed on a new line.

If cat  catches the mouse first, print Cat A.
If cat  catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.
Example

x = 2,
y = 5
z = 4

The cats are at positions  (Cat A) and  (Cat B), and the mouse is at position . Cat B, at position  will arrive first since it is only  unit away while the other is  units away. Return 'Cat B'.

## Function Description

Complete the catAndMouse function in the editor below.

catAndMouse has the following parameter(s):

int x: Cat 's position
int y: Cat 's position
int z: Mouse 's position
Returns

string: Either 'Cat A', 'Cat B', or 'Mouse C'

**Input Format**

The first line contains a single integer, q, denoting the number of queries.
Each of the q subsequent lines contains three space-separated integers describing the respective values x of (cat A's location), y (cat B's location), and z (mouse C's location).

**Constraints**

1 < q <= 100

1 < x,y,z <=100

## Sample Input 0

2
1 2 3
1 3 2

## Sample Output 0

Cat B
Mouse C

## Solution

[Cats and a Mouse](https://github.com/rammya29/Tech-And-Target/blob/main/HakerRank%20Solution/Day-4/Cats%20and%20a%20Mouse/solution.py)
