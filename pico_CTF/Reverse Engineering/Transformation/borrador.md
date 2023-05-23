## Challenge name: Transformation

## Category: Reverse Engineering

## description
https://play.picoctf.org/practice/challenge/104?page=1
I wonder what this really is... enc ```''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])```

## solution
Solution...

## flag
```
flag{}
```