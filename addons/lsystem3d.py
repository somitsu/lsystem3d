bl_info = {
    "name" : "3D L-System",
    "author" : "Shoji Omitsu",
    "version" : (1, 0),
    "blender" : (2, 83, 0),
    "category" : "Mesh",
    "location" : "Operator Search",
    "description" : "3D L-System with Turtle graphic type draw", 
    "warning" : "",
    "doc_url" : "",
    "tracker_url" : "",
}

import bpy, math, mathutils, bmesh, random, logging
from math import radians, pi

class MESH_OT_lsystem3d(bpy.types.Operator):
    bl_idname = "mesh.lsystem3d";
    bl_label = "3D L-System";
    bl_options = {'REGISTER', 'UNDO', 'PRESET'};

    iteration : bpy.props.IntProperty(
        name = 'Iteration',
        description = 'Number of string manipulation iterations',
        default = 3,
        min = 0, soft_max = 5,);
    edgeLength : bpy.props.FloatProperty(
        name = 'Edge Length',
        description = 'Length of edge created by forward movement',
        default = 1.0,
        min = 0, soft_max = 10,
    );
    theta : bpy.props.FloatProperty(
        name = 'Theta',
        description = 'Angle of turning at each turn command',
        default = 90,
        min = 0, max = 360,);
    variables : bpy.props.StringProperty(
        name = 'Variables',
        description = 'List of Char variables to be used',
        default = "['F']",);
    constants : bpy.props.StringProperty(
        name = 'Constants',
        description = 'List of Char constants to be used',
        default = "['F','+','-','[',']','&','^','%','$','|']",);
    axiom : bpy.props.StringProperty(
        name = 'Axiom',
        description = 'Axiom (Initial condition) of L-System',
        default = "['F']",);
    rules : bpy.props.StringProperty(
        name = 'Rules',
        description = 'String replacement rules to be used in Python dict format',
        default = "{'F': 'F+F-F-F+F'}",);
    forwards : bpy.props.StringProperty(
        name = 'Forwards',
        description = 'List of characters representing Forward motion',
        default = "['F']",);
    stochastic : bpy.props.BoolProperty(
        name = 'Stochastic',
        description = '',
        default = False,);

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D';

    def execute(self, context):
        lsysStr = self.buildLsysStr();
        # print(lsysStr);

        cursorPos = bpy.context.scene.cursor.location;

        bm = bmesh.new();
        mymesh = bpy.data.meshes.new('lsystem3d');
        myobj = bpy.data.objects.new('lsystem3d', mymesh);
        bm.from_mesh(mymesh);

        bpy.context.scene.collection.objects.link(myobj);

        myTurtle = turtle3d(position = cursorPos);
        self.drawLsystem(myTurtle, bm, lsysStr, self.edgeLength);

        bm.to_mesh(mymesh);
        bm.free();

        return {'FINISHED'};


    def buildLsysStr(self):
        lsysStr = self.axiom;
        for _ in range(self.iteration):
            lsysStr = self.processString(lsysStr, eval(self.variables), eval(self.constants), eval(self.rules), self.stochastic);
        return lsysStr;
    
    def processString(self, oldStr, var, const, rule, stochastic):
        newStr = ''
        ep = 0.00001;

        for char in oldStr:
            if char in var:
                if stochastic:
                    index = int(math.floor((random.random()- ep)*len(rule[char])))
                    newStr += rule[char][index]
                    #print(index)
                else:
                    newStr += rule[char]
            elif char in const:
                newStr += char
            else:
                print(f'something wrong {char}')
        return newStr

    def drawLsystem(self, turtle, bm, lsysStr, distance):
        vertStack = [];
        currVert = bm.verts.new(turtle.position);

        for char in lsysStr:
            # print(f'char:{char}');
            if char in eval(self.forwards):
                turtle.forward(distance);
                newVert = bm.verts.new(turtle.position);
                newEdge = bm.edges.new((currVert, newVert));
                currVert = newVert;
            elif char == 'B':
                pass;
            elif char == '+':
                turtle.yaw(self.theta);
            elif char == '-':
                turtle.yaw(-self.theta);
            elif char == '&':
                turtle.pitch(-self.theta);
            elif char == '^':
                turtle.pitch(self.theta);
            elif char == '\\':
                turtle.roll(self.theta);
            elif char == '/': 
                turtle.roll(-self.theta);
            elif char == '|':
                turtle.turn();
            elif char == '[':
                turtle.save();
                vertStack.append(currVert);
            elif char == ']':
                turtle.load();
                currVert = vertStack.pop();                
            



class turtle3d:
    def __init__(self, position = (0,0,0), heading = (1,0,0), up = (0,0,1)):
        self.position = mathutils.Vector(position);
        self.heading = mathutils.Vector(heading);
        self.quat = mathutils.Quaternion(heading, radians(0));
        self.stack = [];

        
    def forward(self, distance):
        self.position += self.quat @ mathutils.Vector((1,0,0)) *distance;
        # print(f'forward:{self.position},\n{self.quat}');
    
    def backward(self, distance):
        self.position -= self.quat @ mathutils.Vector((1,0,0)) *distance;

    def yaw(self, angle):
        self.quat = self.quat @ mathutils.Quaternion((0,0,1), radians(angle));
        # print(f'yaw:{self.position},\n{self.quat}');
        
    def pitch(self, angle):
        self.quat = self.quat @ mathutils.Quaternion((0,1,0), radians(angle));
        # print(f'pitch:{self.position},\n{self.quat}');
    
    def roll(self, angle):
        self.quat = self.quat @ mathutils.Quaternion((1,0,0), radians(angle));
        # print(f'roll:{self.position},\n{self.quat}');
    
    def turn(self):
        self.quat = self.quat @ mathutils.Quaternion((0,0,1), radians(180));
        # print(f'turn:{self.position},\n{self.quat}');


    def save(self):
        self.stack.append((self.position.copy(), self.quat.copy()));
        
    def load(self):
        self.position, self.quat = self.stack.pop()
        
    def debug(self):
        return((self.position, self.quat))

def mesh_add_menu_draw(self, context):
    self.layout.operator('mesh.lsystem3d',
                            icon = 'FREEZE');

blender_classes = (
    MESH_OT_lsystem3d,
)

def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class);
    bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw);
    
def unregister():
    for blender_class in reversed(blender_classes):
        bpy.utils.unregister_class(blender_class);
    bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw);