# Coding Guidelines

## Python
- In general use python version 3.6.9
- comply with the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/)
- the executable main file should be named `main.py`
  - Bonus: add a help message, which can be shown via `-h` or `--help` argument
- add a `README.md` to each python project, which describes what the purpose of the project is and how to use the project
  - recommended: some examples how to use it

## Git
- don't use capital letters in branch names, see https://stackoverflow.com/a/38494084/3866740
- four-eye principle for merging

---
Some code guidelines can be automatically enforced with an .editorconfig file (https://editorconfig.org/) if the used editor or IDE supports this.

## Encoding
The following command lists all `*.cpp`-files with non trivial encoding, i.e., they might contain some special characters:
```
/bin/find . -type f -name *.cpp -exec file --mime-encoding {} \; | grep -v us-ascii
```
All files should be in `utf-8` encoding but should only use ascii characters.

## Tabs vs. Spaces
No tab characters should be used. Instead we should use always 4 spaces.

## Brace Formatting
In C++ braces should always be like that:  
```cpp
int myFunction(const Vector2d& v) {
  return 2;
}
```

## Module Conventions
- parameter Class should be named `Parameter`
- the object of the parameter class should be called params
- The config file with the parameters should have the same name as the Module
- no leading and trailing underscores in header include guards. use `MY_MODULE_NAME` instead of `_MY_MODULE_NAME_`