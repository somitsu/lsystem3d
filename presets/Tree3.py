import bpy
op = bpy.context.active_operator

op.iteration = 6
op.edgeLength = 1
op.theta = 20
op.variables = "['V','W','X','Y','Z']"
op.constants = "['F','+','-','[',']','&','^','%','$','|']"
op.axiom = "VZFFF"
op.rules = "{'V': '[+++W][---W]YV','W': '+X[-W]Z','X': '-W[+X]Z','Y': 'YZ','Z': '[-FFF][+FFF]F'}"
op.forwards = "['F']"
op.stochastic = False
