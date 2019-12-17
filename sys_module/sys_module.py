import sys

print(sys.version)
print(sys.argv)      # command line argument passed to a script

# stderr - stores is your error message
# stdin - accept the input from user
# stdout - print to the screen
# exit() - tells interpreter to quit or direct way to end python script
print(sys.executable)   # path and name of the file for python executable
# print(sys.path)   # Contains the search pyth, where Python is looking for modules.

# Name of the platform on which Python is running, e.g. "linux2" for Linux and "win32" for Windows
print(sys.platform)

# Similar information than sys.version, but the output is a tuple
#  containing the five components of the version number: major, minor, micro, release-level, and serial.
#  The values of this tuple are integers except the value for the release level, which is one of the following:
#  'alpha', 'beta', 'candidate', or 'final'.
print(sys.version_info)


# getrecursionlimit() - returns the current value of the recursion limit, the maximum depth of the Python interpreter stack.
#  This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.

# setrecursionlimit(limit) sets the maximum depth of the Python interpreter stack to the value of "limit"

print(sys.getrecursionlimit())