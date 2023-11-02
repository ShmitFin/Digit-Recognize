import Interface
import glob
import random
arr = []
def Book():
    c = Interface.interface(random.choice(glob.glob("datasets\\zeros\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\ones\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\twos\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\tres\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\fours\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\fives\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\six\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\seven\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\eight\\*.png")))
    arr.append(c.conv(c.ar))
    c = Interface.interface(random.choice(glob.glob("datasets\\nine\\*.png")))
    arr.append(c.conv(c.ar))
    return arr

#print(c.img()[0][0])
#print(Book())
'''colors={
    "[237  28  36]":"red",
    "[255 242   0]":"yellow",
    "[ 34 177  76]":"green"
}
print(colors[str(c.img()[0][0])])'''