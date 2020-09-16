import bpy
op = bpy.context.active_operator

op.iteration = 3
op.edgeLength = 1
op.theta = 90.0
op.variables = "['F']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "F+F+F+F"
op.rules = "{'F': 'FF+F+F+F+FF'}"
op.forwards = "['F']"
op.stochastic = False
