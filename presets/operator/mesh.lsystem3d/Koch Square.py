import bpy
op = bpy.context.active_operator

op.iteration = 5
op.edgeLength = 1
op.theta = 90.0
op.variables = "['F']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "F"
op.rules = "{'F': 'F+F-F-F+F'}"
op.forwards = "['F']"
op.stochastic = False
