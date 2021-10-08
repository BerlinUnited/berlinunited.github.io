# Coding Guidelines

## Git
- Don't use capital letters in branch names, see https://stackoverflow.com/a/38494084/3866740
- We use a four-eye principle for merging. Create a merge request in gitlab and ask another developer to approve the changes.
- The pipeline for your merge request must run wthout any error
- Try to keep the lifetime of your branch as short as possible. We don't want branches to exists for years.
- Ideally a branch addresses on feature or bug. This makes it easier to test and review.
- The merge request should explain the changes and link to an issue where applicable.

## Python
- In general use python version 3.6.9
- comply with the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/)
- the executable main file should be named `main.py`
  - Bonus: add a help message, which can be shown via `-h` or `--help` argument
- add a `README.md` to each python project, which describes what the purpose of the project is and how to use the project
  - recommended: some examples how to use it

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
- We use include guards for all header files:
  - no leading and trailing underscores in header include guards. use `MY_MODULE_NAME_H` instead of `_MY_MODULE_NAME_H_`
  - We don't use pragma once. We had a lot of discussions about it and decided to stick with the include guards. 
    Links from the last discussion:
    - [https://luckyresistor.me/2019/07/13/why-its-time-to-use-pragma-once/](https://luckyresistor.me/2019/07/13/why-its-time-to-use-pragma-once/)
    - [https://stackoverflow.com/questions/1143936/pragma-once-vs-include-guards/34884735#34884735](https://stackoverflow.com/questions/1143936/pragma-once-vs-include-guards/34884735#34884735)