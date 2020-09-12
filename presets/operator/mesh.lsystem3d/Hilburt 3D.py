import bpy
op = bpy.context.active_operator

op.iteration = 2
op.theta = 90
op.variables = "['A','B','C','D']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "A"
op.rules = "{'A': 'B-F+CFC+F-D&F^D-F+&&CFC+F+B//','B': 'A&F^CFB^F^D^^-F-D^|F^B|FC^F^A//','C': '|D^|F^B-F+C^F^A&&FA&F^C+F+B^F^D//','D': '|CFB-F+B|FA&F^A&&FB-F+B|FC//'}"
op.forwards = "['F']"
op.stochastic = False
