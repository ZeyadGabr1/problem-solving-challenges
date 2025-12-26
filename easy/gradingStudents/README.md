
# Grading Students - HackerRank.com


## Problem Short Description
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

##  Example

```bash

Input:
4
38
39
67
84

Output:
[40, 40, 67, 85]
```


## 💡 Solution Idea

The solution iterates through the list of grades and checks which grades are eligible for rounding.  
For each grade that is at least 38, the difference to the next multiple of 5 is calculated.  
If this difference is less than 3, the grade is rounded up by adding the difference

## ⏱ Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)


## Problem Link

[HackerRank – Grading Students](https://www.hackerrank.com/challenges/grading)



## How to run

```bash
python solution.py
```
## Authors

- [@ZeyadGabr1](https://www.github.com/ZeyadGabr1)

