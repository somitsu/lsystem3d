import bpy
op = bpy.context.active_operator

op.iteration = 4
op.theta = 45
op.variables = "['F']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "F"
op.rules = "{'F': '-F++F-'}"
op.forwards = "['F']"
op.stochastic = False
