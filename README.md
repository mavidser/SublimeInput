#SublimeInput
SublimeInput is a Sublime Text plugin which gives stdin input through comments to a program. It's in active development and will not work with all platforms and languages.

##Usage
Insert a multi-line comment in the top of program in the given format:

_Python:_
```python
'''input
2
foo
bar
'''
a=input()
for i in xrange(a):
    a=raw_input()
    print a
```
_C/C++_
```cpp
/*input
2
foo
bar
*/
#include <stdio.h>
int main() {
  int n,i;
  char s[10];
  scanf("%d",&n);
  for(i=0;i<n;i++) {
    scanf("%s",s);
    printf("%s\n",s);
} }
```

The opening comment symbols should immediately be followed by the `input` keyword.
Both the programs will print the following output:
```
foo
bar
```
##Current Status
The plugin is in active development and right now supports only Python/C/C++ on Linux/OSX.

