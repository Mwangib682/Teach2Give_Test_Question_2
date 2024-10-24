"""
QUESTION 2: Write a Python function that checks whether a word or phrase is palindrome or
not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase nurses run.
"""

#import the re module, which provides support for regular expressions in Python.
import re

#defining a new function named is_palindrome
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Check if the cleaned string is the same as its reverse
    return cleaned_str == cleaned_str[::-1]


# Test examples
print("The word 'madam' is a palindrome: ",is_palindrome("madam"))  # True
print("The word 'assignment' is a palindrome: ",is_palindrome("assignment"))  # False
print("The word 'kayak' is a palindrome: ",is_palindrome("kayak"))  # True
print("The word 'racecar' is a palindrome: ",is_palindrome("racecar"))  # True
print("The word 'python' is a palindrome: ",is_palindrome("python"))  # False
print("The word 'nurses run' is a palindrome: ",is_palindrome("nurses run"))  # True
print("The word 'hello' is a palindrome: ",is_palindrome("hello"))  # False
print("The statement 'A man, a plan, a canal, Panama!' is a palindrome: ",is_palindrome("A man, a plan, a canal, Panama!"))  # True


"""
My Pycharm results for the above written code are as follows:
C:\Users\hp\PycharmProjects\pythonProject2\.venv\Scripts\python.exe "C:\Users\hp\PycharmProjects\pythonProject2\QUESTION 2.py" 
The word 'madam' is a palindrome:  True
The word 'assignment' is a palindrome:  False
The word 'kayak' is a palindrome:  True
The word 'racecar' is a palindrome:  True
The word 'python' is a palindrome:  False
The word 'nurses run' is a palindrome:  True
The word 'hello' is a palindrome:  False
The statement 'A man, a plan, a canal, Panama!' is a palindrome:  True

Process finished with exit code 0
"""