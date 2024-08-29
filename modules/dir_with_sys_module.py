import sys

# get attribute names using sys module
dir(sys)
['__displayhook__', '__doc__',
 'argv', 'builtin_module_names',
 'version', 'version_info']

# get attribute names for current module
dir()
['__builtins__', '__doc__',
 '__name__', '__package__', 'sys']

# create a new variable "a"
a = 5

dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# del/rm a name
del a

dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']