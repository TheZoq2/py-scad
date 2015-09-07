
class Element:
    def __init__(self):
        self.children = []

    def generateCode(self):
        code = ""

        for child in self.children:
            code += child.generateCode();
            code += "\n"

        return code

    def addChild(self, child):
        self.children.append(child)

    

class Translate(Element):
    def __init__(self, pos):
        super(Element, self).__init__()
        self.pos = pos;
        self.children = []

        if len(pos) != 3:
            raise ValueError("Transform takes exactly 1 parameter");

    def generateCode(self):
        code = "translate([{},{},{}])\n".format(self.pos[0], self.pos[1], self.pos[2]);
        code += "{\n"
        
        for child in self.children:

            code += str(child.generateCode());
            code += "\n";
        
        code += "}"

        return code;

class Module(Element):
    def __init__(self, name, parameters):
        Element()
        self.name = name;
        self.parameters = parameters

    def generateCode(self):
        code = "{}(".format(self.name);

        for i in range(0, len(self.parameters)):
            code += "{}".format(self.parameters[i]);
            
            if(i != len(self.parameters) - 1):
                code += ","

        code += ");"

        return code






