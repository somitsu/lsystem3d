import bpy
op = bpy.context.active_operator

op.iteration = 3
op.edgeLength = 1
op.theta = 90
op.variables = "['X','Y']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "-YF"
op.rules = "{'X': 'XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-','Y': '+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY'}"
op.forwards = "['F']"
op.stochastic = False
