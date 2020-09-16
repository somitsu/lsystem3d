import bpy
op = bpy.context.active_operator

op.iteration = 10
op.theta = 90
op.variables = "['X', 'Y']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "FX"
op.rules = "{'X': 'X+YF+', 'Y': '-FX-Y'}"
op.forwards = "['F']"
op.stochastic = False
