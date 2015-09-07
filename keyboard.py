import scadGenerator as SCAD

SW = 18 #Standard key size
TAB_SIZE = 22 + 6
CAPS_SIZE = 26 + 6
BACKSPACE_SIZE = 26 + 6
BACKSLASH_SIZE = 22 + 6
CTRL_SIZE = 22 + 6
PADDING = 1;
ENTER_SIZE = 22 + 6

layout = [
            [SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW],
            [SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, BACKSPACE_SIZE],
            [TAB_SIZE, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, BACKSLASH_SIZE],
            [CAPS_SIZE, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, SW, ENTER_SIZE],
            [],
            []
        ];

mainModule = SCAD.Element()

currentX = 0;
currentY = 0;

for row in layout:
    for key in row:
        pos = (currentX,currentY,-1)

        translate = SCAD.Translate(pos);
        translate.addChild(SCAD.Module("children", "0"))
        mainModule.addChild(translate);

        currentX += key;

    currentX = 0;
    currentY += SW;
        

print(mainModule.generateCode());
