- input=ac
- blockbegin=a
- blockend=c
- block="a"
- replacement=\*   // a is replaced by \*
- result=\*c

# Video
![[test-1.mp4]]

![[test-1-b.mp4]]

## Test1.ohm
```
test1 {
main = rulea
rulea = "a"
}
```
## Test1.glue
```
main [rulea] = [[*]]
rulea [c] = [[${c}]]
```
## Command
```
prep 'a' 'c' test1.ohm test1.glue --input=test1
```
## Reading
![reading](tests-test 1.svg)
Matching:
rule `main` calls rule `rulea`
- `rulea` matches a single "a"

Formatting:
- after matching by test1.ohm, test1.glue is invoked
- `main` walks the resulting match-tree and fetches the sub-tree from `rulea`
- `rulea` matches one character of the input and returns it verbatim (in this case "a")
- `main` receives the result from `rulea` in the parameter called `rulea` then replaces the result from `rulea` by a `*` and returns that result