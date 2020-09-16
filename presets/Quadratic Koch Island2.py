import bpy
op = bpy.context.active_operator

op.iteration = 3
op.theta = 90
op.variables = "['F']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "F+F+F+F"
op.rules = "{'F': 'F-FF+FF+F+F-F-FF+F+F-F-FF-FF+F'}"
op.forwards = "['F']"
op.stochastic = False
