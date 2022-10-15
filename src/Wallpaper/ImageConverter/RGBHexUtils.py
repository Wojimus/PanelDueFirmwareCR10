def clamp(x):
    return max(0, min(x, 255))


def convert888To565(rgb888):
    return ((rgb888[0] & 0xf8) << 8) + ((rgb888[1] & 0xfc) << 3) + (rgb888[2] >> 3)


def rgb888ToHex(rgb888):
    return "0x{0:02x}{1:02x}{2:02x}".format(clamp(rgb888[0]), clamp(rgb888[1]), clamp(rgb888[2]))


def rgb565ToHex(rgb565):
    return "0x{0:04x}".format(rgb565)