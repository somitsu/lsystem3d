import bpy
op = bpy.context.active_operator

op.iteration = 4
op.theta = 45
op.variables = "['X']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "-X--X"
op.rules = "{'X': 'XFX--XFX'}"
op.forwards = "['F']"
op.stochastic = False
