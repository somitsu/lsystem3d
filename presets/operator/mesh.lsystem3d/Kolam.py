import bpy
op = bpy.context.active_operator

op.iteration = 3
op.theta = 45
op.variables = "['A', 'B', 'C', 'D']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "-D--D"
op.rules = "{'A': 'F++FFFF--F--FFFF++F++FFFF--F', 'B': 'F--FFFF++F++FFFF--F--FFFF++F', 'C': 'BFA--BFA', 'D': 'CFC--CFC'}"
op.forwards = "['F']"
op.stochastic = False
