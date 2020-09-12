import bpy
op = bpy.context.active_operator

op.iteration = 3
op.edgeLength = 1
op.theta = 60.0
op.variables = "['F']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "F++F++F"
op.rules = "{'F': 'F-F++F-F'}"
op.forwards = "['F']"
op.stochastic = False
