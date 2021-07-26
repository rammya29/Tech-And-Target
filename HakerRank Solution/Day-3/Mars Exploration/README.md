# Mars Exploration

## Description

A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic radiation during transmission. 
Given the signal received by Earth as a string, s, determine how many letters of the SOS message have been changed by radiation.

Example

S = 'SOSTOT

The original message was SOSSOS. Two of the message's characters were changed in transit.

## Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

string s: the string as received on Earth

**Returns**

int: the number of letters changed during transmission

**Input Format**

There is one line of input: a single string, .

**Constraints**

1 < length of s < 99

length of s modulo 3 = 0

 s will contain only uppercase English letters, ascii[A-Z].
 
## Sample Input 0

SOSSPSSQSSOR

## Sample Output 0

3

## Explanation 0

 = SOSSPSSQSSOR, and signal length . They sent  SOS messages (i.e.: ).

Expected signal: SOSSOSSOSSOS

Recieved signal: SOSSPSSQSSOR

Difference:          X  X   X

## Soluton

[Mars Exploraation](https://github.com/rammya29/Tech-And-Target/blob/main/HakerRank%20Solution/Day-3/Mars%20Exploration/solution.py)
