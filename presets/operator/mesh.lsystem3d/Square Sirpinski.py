import bpy
op = bpy.context.active_operator

op.iteration = 3
op.theta = 90
op.variables = "['X']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "F+XF+F+XF"
op.rules = "{'X': 'XF-F+F-XF+F+XF-F+F-X'}"
op.forwards = "['F']"
op.stochastic = False
