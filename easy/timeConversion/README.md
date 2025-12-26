
# Time Conversion - HackerRank.com


## Problem Short Description
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


##  Example

```bash

Input:
s = 12:01:00PM

Output:
12:01:00
```


## 💡 Solution Idea

The input time is parsed from a 12-hour format (AM/PM) into a datetime object using strptime, then converted to a 24-hour format using strftime.

## ⏱ Time & Space Complexity
- Time Complexity: O(1)
- Space Complexity: O(1)


## Problem Link

[HackerRank – Time Conversion](https://www.hackerrank.com/challenges/time-conversion/)



## How to run

```bash
python solution.py
```
## Authors

- [@ZeyadGabr1](https://www.github.com/ZeyadGabr1)

