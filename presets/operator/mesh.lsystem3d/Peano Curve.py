import bpy
op = bpy.context.active_operator

op.iteration = 3
op.theta = 90
op.variables = "['X', 'Y']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "X"
op.rules = "{'X': 'XFYFX+F+YFXFY-F-XFYFX', 'Y': 'YFXFY-F-XFYFX+F+YFXFY'}"
op.forwards = "['F']"
op.stochastic = False
