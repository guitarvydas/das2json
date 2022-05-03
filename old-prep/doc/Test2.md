- input=abc
- blockbegin=ab
- blockend=c
- block="a"
- replacement=\*   // a is replaced by \*
- result=\*c

# Video
![[test-2-a.mp4]]

![[test-2-b.mp4]]


## Test2 .ohm
```
test2 {
main = rulea
rulea = "ab"
}
```

## Test2.glue
```
main [rulea] = [[*]]
rulea [twoc] = [[${twoc}]]
```

## Command
```
prep 'ab' 'c' test2.ohm test2.glue --input=test2
```
### Reading
![[tests-test 2.svg]]
The pattern-matcher (test2.ohm) contains 2 rules:
- main - simply calls rulea
- rulea - matches an "a" followed by "b" 

The formatter (test2.glue) has 2 rules with exactly the same names as the rules in the .ohm file:
- main
- rulea

Matching:
- `main` gets input block "ab"
- `main` calls `rulea`
- `rulea` matches 2 characters, i.e. "a" followed by "b"

Formatting:
- `main` calls `rulea`
- `rulea` returns a 2-character string, i.e. "ab"
- `main` receive the string (in the parameter called "rulea") then ignores the string and returns a 1-character string `*`

A new string is formed by concatenating the formatted output of `main` with the tail, resulting in `*c`.

The new string is given as input to the pattern-matcher (again).

The new string `*c` doesn't match.

The process terminates and the final result is `*c`.