# Printing "Goodbye" with a local message variable

def print_goodbye():
    message = 'Goodbye'
    print message

# Tests
message = "Hello"
print message
print_goodbye()
print message

message = "Ciao"
print message
print_goodbye()
print message

# Output
#Hello
#Goodbye
#Hello
#Ciao
#Goodbye
#Ciao