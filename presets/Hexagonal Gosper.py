import bpy
op = bpy.context.active_operator

op.iteration = 4
op.theta = 60
op.variables = "['X', 'Y']"
op.constants = r"['F','+','-','[',']','&','^','\\','/','|']"
op.axiom = "XF"
op.rules = "{'X': 'X+YF++YF-FX--FXFX-YF+', 'Y': '-FX+YFYF++YF+FX--FX-Y'}"
op.forwards = "['F']"
op.stochastic = False
