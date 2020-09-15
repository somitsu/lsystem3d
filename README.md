# lsystem3d
3D Lsystem Addon for Blender

<img src="/images/hilburt3d.png" alt="hilburt3d" width="384" height="216"/><img src="/images/sierpenskiArrowhead.png" alt="sierpenskiArrowhead" width="384" height="216"/>

This addon allows users to add mesh through Lindenmayer System (L-system).

**L-system** is an iterative (or recursive depending on implementation) string manipulation system that can be used to derive complex geometric structures like those of fractals.
By user defining set of chars **"variables (V)"**, initial **"axiom (W)"**, and set of string **"production rules (P)"**, L-system replaces varibles in string according to the production rules for provided number of iterations.


Resulting string will then be passed to a turtule graphics like draw system which interprets the string as series of draw commands to provide the end result.
Below are the list of chars and draw command interpretations.
* F: Move forward and draw line
* +: Yaw (turn) left by angle theta
* -: Yaw (turn) right by angle theta
* &: Pitch down by angle theta
* ^: Pitch up by angle theta
* \\: Roll left by angle theta
* /: Roll right by angle theta
* |: Turn around
* \[: Save state and push to stack
* ]: Pop stack and load state


**Example: Koch Square**
* Variables: \['F']
* Axiom: "F"
* Rules: {'F': "F+F-F-F+F"}
* Theta: 90

*<ins>Iteration 0:</ins>
"F"*

<img src="/images/level0.png" alt="level0" width="96" height="54"/>


*<ins>Iteration 1:</ins>
"F" -> "F+F-F-F+F"*

(the character 'F' is replaced by "F+F-F-F+F" through production rule)

<img src="/images/level1.png" alt="level1" width="96" height="54"/>

*<ins>Iteration 2:</ins>
"F+F-F-F+F" -> "F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F"*

(each character 'F' in the string are replaced by "F+F-F-F+F", '+' and '-" are unchanged since they are not variables)

<img src="/images/level2.png" alt="level2" width="96" height="54"/>



