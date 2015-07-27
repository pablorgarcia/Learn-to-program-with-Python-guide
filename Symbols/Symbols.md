# Symbols

Some rules
-------
A function only makes one output.
Function name can't start with a number.
"Methods" are functions in a class
"Attributes" are variables in a class
2D list [[1,2,3],[4,5,6]]
Help - type in Powershell -m pydoc xxx
ordinal numbers
cardinal numbers


Keywords (excludes easy ones)
-------

from        Use when importing: from sys import argv
while       Loop while logical operator is True
for         Loop over the defined range
break       in for or while loop (not nested within function in loop). Terminates loop skipping else. In Try() will execute Finally before exiting loop.
try         Error handling. Catch in try blocks.
except      Error handling. Handled in except blocks. E.g. except IOError: print …
finally     Error handling. Executed regardless whether an exception occurs.
continue    continue next cycle in loop
as 
in 
is 
def         define a new function
class       group of functions / variables. Tell python to make a new tyrp of thing.
yield       include in function definition to make it a "generator function" (iteration)
lambda      create anonymous functions. 
pass        placeholder when writing that does nothing – e.g. def function(arg): pass
global      declaration that holds for all code. Assign a global variable.
with 
Del         Delete
assert      test that statement that should be True is True. Use for debugging.
import      make a module available to subsequent code
print       write out on the screen. add , to avoid \n at end of line.
exec        statement. Compiles and evaluates a statement in a string.
raise ??? 
return      output returned by a function
self        inside functions of a class, self is a variable for the instance/object being accessed
is-a        something inherits from another, e.g. a salmon is a fish
has-a       something is composed of other things or has a trait e.g. a salmon has a mouth
dict        dictionary { }. Also called hashes.
raw_input('>')  user enters data at prompt > 
int(x)       returns x as a number
seek
range
.get
.decode
.append
.rstrip
.compile
.flush
.split      
.pop        remove the last entry and return it
:           creates branch in code. Expect indented code after this.
==          test if a = b
open(x, r)  r is read mode, w is write mode. Can open multiple copies.
.read()
.close()    close the file
.next()     the next value
readline()  next line from file
truncate()  
write(stuff)  
from x import exists    TRUE if file does exist, FALSE otherwise


Exit types
-------
exit(0)     "Good" exit
exit


Error types
-------
NameError
ImportError


Data Types (excludes easy ones)
-------
None 
numbers 
lists       collection of items in an order that’s accessed by number


String escape sequences
-------
\\          \
\’          ‘
\"          "
\a          BELL = buzzer
\b          Backspace
\f          Formfeed (new page in printing)
\n          New line (enter key)
\r          Carriage return (go back to start of line)
\t          Tab
\v          Tab vertically


String formats
-------
%d          Integer decimal
%i          Integer decimal
%o          octal value
%u          -- Obsolete (same as d) --
%x          hexadecimal (lower case)
%X          hexadecimal (upper case)
%e          floating point exponential format (lower case)
%E          floating point exponential format (upper case)
%f          floating point decimal format
%F          floating point decimal format
%g          floating point format. %e if < -4. %f otherwise.
%G          floating point format. %E if < -4. %F otherwise.
%c          single character (integer or string)
%r          Raw python
%s          String
%%          No argument. Results in % character.


Operators (excludes easy ones)
-------
*           multiply. Also use to unpack a tuple. s = sum(*values)
**          to the power of. Also use to unpack a dictionary. s = sum(**values)
//          truncating division (e.g. "4.0 // 1.5" gives 2.0)
( )         Brackets for variables etc.
[ ]         Brackets for Lists
{ }         Brackets for Dictionaries
@           class/function/method decorators. Dynamically alter them without adjusting source code
, 
. 
:           After this is indented code for function/loop/etc.
;   
+=          "x = x + 2" is the same as "x += 2"
-=          "x = x - 2" is the same as "x -= 2"
*=          "x = x * 2" is the same as "x *= 2"
/=          "x = x / 2" is the same as "x /= 2"
**=         "x = x ** 2" is the same as "x **= 2"
//=         "x = x // 2" is the same as "x //= 2"
%=          "x = x % 2" is the same as "x %= 2"