import bpy
op = bpy.context.active_operator

op.iteration = 3
op.edgeLength = 1
op.theta = 60.0
op.variables = "['X', 'Y']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "YF"
op.rules = "{'X': 'YF+XF+Y', 'Y': 'XF-YF-X'}"
op.forwards = "['F']"
op.stochastic = False
