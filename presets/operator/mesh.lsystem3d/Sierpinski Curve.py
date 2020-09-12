import bpy
op = bpy.context.active_operator

op.iteration = 4
op.theta = 45
op.variables = "['X']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "F--XF--F--XF"
op.rules = "{'X': 'XF+F+XF--F--XF+F+X'}"
op.forwards = "['F']"
op.stochastic = False
