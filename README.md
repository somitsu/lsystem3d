# lsystem3d
3D Lsystem Addon for Blender

This addon allows users to add mesh through Lindenmayer System (L-system).

**L-system** is an iterative (or recursive depending on implementation) string manipulation system that can be used to derive complex geometric structures like those of fractals.
By user defining set of chars **"variables (V)"**, initial **"axiom (W)"**, and set of string **"production rules (P)"**, L-system replaces varibles in string according to the production rules for provided number of iterations.


Resulting string will then be passed to a turtule graphics like draw system which interprets the string as series of draw commands to provide the end result.
Below are the list of chars and draw command interpretations.
* F: Move forward
* +: Yaw (turn) left by theta
* -: Yaw (turn) right by theta
* &: Pitch down by theta
* ^: Pitch up by theta
* \\: Roll left by theta
* /: Roll right by theta
* |: Turn around
* [: Save state and push to stack
* ]: Pop stack and load state


**Example: Koch Square**
* Variables: ['F']
* Axiom: "F"
* Rules: {'F': "F+F-F-F+F"}

*Iteration 0: "F"*


*Iteration 1:
"F" -> "F+F-F-F+F"*

(the character 'F' is replaced by "F+F-F-F+F" through production rule)

*Iteration 2:
"F+F-F-F+F" -> "F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F"*

(each character 'F' in the string is replaced by "F+F-F-F+F", '+' and '-" are unchanged since they are not variables)






