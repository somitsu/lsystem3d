import bpy
op = bpy.context.active_operator

op.iteration = 3
op.theta = 45
op.variables = "['X', 'Y']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "X+X+X+X+X+X+X+X"
op.rules = "{'X': 'X+YF++YF-FX--FXFX-YF+X', 'Y': '-FX+YFYF++YF+FX--FX-YF'}"
op.forwards = "['F']"
op.stochastic = False
