import bpy
op = bpy.context.active_operator

op.iteration = 3
op.theta = 90
op.variables = "['F']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "FF+FF+FF+FF"
op.rules = "{'F': 'F+F-F-F+F'}"
op.forwards = "['F']"
op.stochastic = False
