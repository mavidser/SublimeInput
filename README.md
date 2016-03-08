Sublime Input
=============

Sublime Input is a Sublime Text 2/3 plugin which gives STDIN input through comments to a program.

Installation
------------
**With the [Package Control plugin](https://packagecontrol.io/installation) (Recommended):**

1. Bring up the Command Palette (Cmd+Shift+P on OS X, Ctrl+Shift+P on Linux/Windows). 
2. Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select Sublime Input.
3. The advantage of using this method is that Package Control will automatically keep Sublime Input up to date with the latest version.

**Alternate Method:**

1. Go to Preferences | Browse Packages
2. Browse up a folder and then into the Installed Packages/ folder
3. [Downlad and Copy the `Sublime.Input.sublime-package` file](http://github.com/mavidser/SublimeInput/releases/download/3.0/Sublime.Input.sublime-package)
4. Restart Sublime Text

Usage
-----
Insert a multi-line comment at the top of program.

Examples, using the default format:

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

Both the programs will print the following output:
```
foo
bar
```

Configure
---------
Set the build schemas in Preferences: Package Settings > SublimeInput > Settings – User

Example schema :
```
{
  "build_schemas" : {
    "cpp" : {
      "shell_cmd" : "g++ \"${file}\" -o \"${file_path}/${file_base_name}\" && \"${file_path}/${file_base_name}\"",
      "input_start" : "/*input",
      "input_end" : "*/"
    }
  }
}
```

`build_schemas` contains key-value pairs, where the key's the filetype (`cpp` in this example), and a dictionary as its value.

`shell_cmd`  stores the command to execute on build.
> `{file}` - Complete address of the file

> `{file_path}` - The address of the directory the file is stored in

> `{file_base_name}` - Just the filename, without the extension

> `{file_extension}` - The extension of the file

`input_start` stores the start of the input comment block.

`input_end` stores the end of the input comment block.

The default schema can be found in Preferences: Package Settings > SublimeInput > Settings – Default

The following schemas have been included by default:
- C
- C++
- Python
- Java

Keyboard Shortcuts
------------------
- *Ctrl + Alt + B* - Build/Run program
- *Ctrl + Alt + C* - Cancel the running pogram

Current Status
--------------
The Plugin is in active development. Windows users may encounter some bugs.

