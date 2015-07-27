# Interactive applications, buttons and input fields.
Event handlers, local variables, global variables, SimpleGui module, buttons, input fields.

Event handlers — Event-driven programming
-------
Event handlers (also called callbacks) are functions registered to an event such as a button click, keyboard press or mouse click.
Event handlers react to the event by changing the state (collection of information) encoded in the program.

Local variables — Local vs. global variables
-------
Assignment to a variable inside a Python function creates a local variable.
The scope of variable (portion of the program where the value of the variable can be accessed) is the body of function.

Global variables — Local vs. global variables
-------
Variables defined outside functions are global variables. Their values may be accessed inside functions without declaration.
To modify to a global variable inside a function, the variable must be declared inside the function using the keyword global.
Global variables are a convenient (but dangerous) way for event handlers to share information in event-driven programming.

SimpleGUI module — SimpleGUI
-------
The Docs button links to documentation for SimpleGUI.
SimpleGUI allows creations of frames and timers as well as loading sounds and images.
Frames include a control panel (with buttons and input fields), a status area (for monitoring keyboard and mouse events) and a canvas (with simple 2D drawing operations).

Buttons — Buttons
-------
Buttons may be created (and their event handlers registered) via add_button.
Buttons are positioned linearly (top/down) in the control panel in their order of creation.

Input fields — Input fields
-------
Input fields may be created (and their event handlers registered) via add_input.
Input fields are positioned linearly (top/down) in the control panel in their order of creation.
The event handlers for the input field take a single parameter that is the text string entered.
