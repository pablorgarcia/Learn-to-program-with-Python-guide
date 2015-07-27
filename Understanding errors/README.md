# Understanding errors

This is an attempt to translate Python errors into English. It is by no means complete or comprehensive, but we've added it here as a resource.

So what do all these errors mean?

SyntaxError: "I don't recognize what you just wrote as Python code."
-------
'Syntax' refers to the rules that dictate how you're allowed to write down a coding language. For example, the rule that states that youmay not begin a variable name with a digit is part of the syntax of Python. A SyntaxError will pop up if you violate any of Python's syntax rules. This could be forgetting to close a parenthesis or quote, mistakes in indentation, forgetting colons after function headers, etc. Note that syntax errors can be tricky - sometimes the real error is actually before or after the line that the error is reported on. When you go hunting for syntax errors, try looking at the entire block of code that surrounds the line where the error appears.

NameError: "What in the world is X?"
-------
A NameError is triggered when doesn't recognize the variable, function name, etc. that you're referring to. A NameError is the way of saying "I've never heard of that before!" Common causes of this are misspellings or forgetting to declare variables entirely.

TypeError: "You're trying to use some of those things in a way that wasn't intended."
-------
This error can come up when you're trying to do perform an operation on something, but the operation and the thing just don't go together. One example is trying to multiply a dictionary and an integer - it just won't work. A helpful tool in debugging type errors is the Python type() function. Adding print statements like "print type(my_variable)" will help you figure out what's going wrong.

AttributeError: "That object doesn't know how do to what you asked it to do"
-------
In OOP, objects have "attributes" - things that they're aware of, and/or know how to do. In terms of Python, attributes are an objects properties and the methods defined by its class. An AttributeError will be thrown when you ask an object to do something or access something that isn't in its class definition.

IndexError: "That list/dictionary/tuple (etc.) doesn't have that many items in it."
-------
An IndexError happens when you try to access an index that doesn't actually exist. It's like telling someone to take 13 eggs out of a 12-egg carton - it won't work, because there are only 12 spaces. Printing out your index values, along with  len(the_list_in_question) will help you in debugging these errors. Important to note: negative indices *are* possible in Python! See the video lecture on lists for more information.

TokenError: "You probably forgot to close a bracket." *
-------
Very simply, tokens are things that stand for other things - sort of like variables, except they're used at a more structural level. Some examples of tokens are EOF (End Of File) and  EOL (End Of Line). These are the two most common ones you will come across in Python, but they are used everywhere in programming. The TokenErrors that you will see in this course are usually solved by remembering to close your brackets. See the example for a more in-depth explanation of why this is.

*Not actually what it means - but a more detailed explanation is more appropriate for other courses, and this is the most common cause of TokenErrors in this class.

ValueError: "There's something wrong with the value of one of those arguments (but the type is ok)."
-------
A ValueError is raised when a function receives an argument that looks ok on the surface (e.g., it receives a character, and it was looking for a character), but the value of that argument is unexpected (e.g., the function was only built to handle digits, and it received a letter 'a'). This type of error can be solved by checking the documentation for whatever function you're trying to use,  
and making sure that whatever you put inside the parentheses, the function was built to handle it.

IndentationError: "Your code blocks aren't all indented to the proper levels."

This is a type of Syntax Error. See Syntax Errors, 'Indendation Error: unindent does not match any outer indentation'

Miscellaneous section - these errors are either self-explanatory or not common in the level of programming done in IIPP
-------
OverflowError - caused by trying to store, for example, a long inside an int. A long has too many bytes to fit inside the int data type 
ZeroDivisionError - you guessed it - you're trying to divide by zero somewhere
ImportError - caused by trying to import a module that doesn't exist. Check your spelling.

JavaScript section - these are not Python errors. They are related to your browser, not your code.