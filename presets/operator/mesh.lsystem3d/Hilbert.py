import bpy
op = bpy.context.active_operator

op.iteration = 3
op.edgeLength = 1
op.theta = 90.0
op.variables = "['X', 'Y']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "X"
op.rules = "{'X': '-YF+XFX+FY-', 'Y': '+XF-YFY-FX+'}"
op.forwards = "['F']"
op.stochastic = False
