import math

hexits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def floatToHex256(x):
    h256  = min(x,255) # caps at #FF
    h256  = math.floor(256*x)
    hex16 = math.floor(h256/16)
    hex1  = h256 - (16*hex16)
    return hexits[hex16] + hexits[hex1]

def normTo256(x):
    return math.floor(min(x*255,255))

def normToHex256(x):
    return hex(normTo256(x))[2:]

def RGBToHexColor(a,b,c):
    hexstring = "#"
    for x in [a,b,c]:
        prepend = '0' if normTo256(x) < 16 else ''
        hexstring += prepend + normToHex256(x)
    return hexstring

def attributeToColor(val, min, max):
    norm = (val - min) / max
    return u_colors.RGBToHexColor(norm, 0.0, 1-norm)