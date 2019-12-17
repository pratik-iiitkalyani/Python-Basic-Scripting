# this module is used to interect with my os

import os

print(os.getcwd())  # get current working directory

# os.chdir('C:\Users\ts-pratik.kumar\Music\New folder')  # change the working directory

# os.mkdir("C:\\Users\\ts-pratik.kumar\\Desktop\\python_scripting\\subprocess_module")  # new directory

# os.rmdir("C:\\Users\\ts-pratik.kumar\\Desktop\\python_scripting\\subprocess_module")    # remove directory

# os.remove("path") - remove the  file

# join the two path
# print(os.path.join("C:\\Users\\ts-pratik.kumar\\Desktop\\python_scripting", "C:\\Users\\ts-pratik.kumar\\Desktop\\python_scripting\\os_module"))

# split into directory name and file
print(os.path.split("C:\\Users\\ts-pratik.kumar\\Desktop\\python_scripting\\os_module\\os_module"))

# check file is exits or not -  return true or not
print(os.path.exists("C:\\Users\\ts-pratik.kumar\\Desktop\\python_scripting\\os_module\\os_module.py"))