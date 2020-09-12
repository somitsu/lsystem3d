import bpy
op = bpy.context.active_operator

op.iteration = 3
op.edgeLength = 1
op.theta = 22.5
op.variables = "['F']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "F"
op.rules = "{'F': 'FF+[+F-F-F]-[-F+F+F]'}"
op.forwards = "['F']"
op.stochastic = False
