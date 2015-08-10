== Basics of lists, keyboard control ==
-------
Canvas, event-driven drawing, drawing text, timers.

=== Lists — Lists ===

Lists can be constructed as a sequence of objects inside square brackets; e.g; <code>[2,4,6]</code>. The <code>list</code> function also converts other types of sequence data such as strings into lists.
Sequence operations such as indexing <code>l[i]</code>, concatenation <code>+</code>, length <code>len(l)</code> and slicing apply to lists.
As opposed to strings, an element of a list can be mutated via assignment <code>l[i] = x</code>.

=== Points and vectors — Motion ===

A point in 2D is represented by a pair of Cartesian coordinates.
A vector in 2D is represented by a pair of numbers (its horizontal and vertical components).
Taking the difference of two points (componentwise) yields a vector.
Vectors can be added and scaled (componentwise). Points should not be added or scaled.
Adding a point and a vector (componentwise) yields a new point. This operation can be used to animate moving points.

=== Distance computations — Collisions and reflections ===

The distance between two points <code>p0</code> and <code>p1</code> is 
<code>√(p0[0]-p1[0])<sup>2</sup>+(p0[1]-p1[1])<sup>2</sup></code> .
The distance between a point and a circle and the distance between two circles follows from this formula.
The set of points <code>[x,y]</code> that satisfy the equation <code>a*x + b*y + c == 0</code> is a line. The distance from this line to a point <code>p</code> is 
<code>(a*p[0] + b*p[1] + c)/ √a<sup>2</sup> + b<sup>2</sup></code>
The distance from a circle to a line is the distance from the center of the circle to the line minus the radius.

=== Reflections — Collisions and reflections ===

The direction of reflection for a ball bouncing off of a wall depends on the incoming velocity vector v and the normal vector to the wall at the point of contact.
The incoming velocity vector can be decomposed into <code>v = v<sub>p</sub> + v<sub>n</sub></code> where <code>v<sub>n</sub></code> is the component of v orthogonal to wall and <code>v<sub>p</sub></code> is the component parallel to to the wall.
In this model, the reflected vector is <code>v = v<sub>p</sub> - v<sub>n</sub></code>.
This model simplifies for horizontal and vertical walls. In particular, reflection simply negates one component of the velocity vector v.

=== Keyboard events — Keyboard input ===

SimpleGUI suppports two event handlers for keyboard events.
The key down event handler is registered via <code>set_keydown_handler</code>.
The key up event handler is registered via <code>set_keyup_handler</code>.
The variable passed to each of these handlers is a number that can be compared at the constants in <code>KEY_MAP</code> to determine which key has been pressed.

=== Positional control — Keyboard input ===

We can control the position of a point <code>p</code> directly using key board events.
The horizontal and vertical components of a point <code>p</code></code>'s position can be increment/decrement via <code>p[i] += c</code> in response to key presses.

=== Velocity control — Velocity control ===

Basic physics relates the position of a point <code>p</code> and its velocity <code>v</code> via the equation <code>p += dt * v</code> where <code>dt</code> is a small time step.
In this model, we can control the motion of <code>p</code> via keyup/keydown events that increment/decrement the two components of the velocity vector <code>v</code> via <code>v[i] += c</code>.

=== Mutable vs. immutable data — Programming tips #4 ===

Numbers, Booleans and strings are immutable and can not be modified. Only new copies of these kinds of data can be made.
On the other hand, parts of a list can be mutated via assignment to individual elements of the list.
Assignment of an entire list to a variable generates a reference that refers to the list. Subsequent assignment may generate multiple references to the same list.
Mutating a list with multiple references modifies all references to the list. This capability is very useful, but can generate subtle errors.


