def RLECompressHexString(hexString, bitNumber, multiplierBitAmount):
    # Hex String Format
    hexFormatString = "{0:0" + str(multiplierBitAmount) + "x}"

    # Compress String
    print("Compressing Hex String With RLE")
    compressedHexString = ""
    previousHex = hexString[0:bitNumber]
    repeatCount = 1
    for i in range(bitNumber, len(hexString), bitNumber):
        if repeatCount >= pow(16, multiplierBitAmount) - 1:
            compressedHexString += "{}{}".format(hexFormatString.format(repeatCount), previousHex)
            repeatCount = 1
        else:
            hexValue = hexString[i:i+bitNumber]
            if hexValue != previousHex:
                compressedHexString += "{}{}".format(hexFormatString.format(repeatCount), previousHex)
                repeatCount = 1
                previousHex = hexValue
            else:
                repeatCount += 1
    compressedHexString += "{}{}".format(hexFormatString.format(repeatCount), previousHex) # Get Last pattern

    # Debug Output
    compressionRatio = len(hexString) / len(compressedHexString) * 100
    print("Compressed Hex String With A Compression Ratio Of {:.2f}%".format(compressionRatio))
    print("Original Length: {}, Compressed Length: {}".format(len(hexString), len(compressedHexString)))

    # Verify Decompressed Hex String Matches Original Hex String
    print("\nVerifying Hex String")
    decompressedHexString = RLEDecompressHexString(compressedHexString, bitNumber, multiplierBitAmount)
    if decompressedHexString == hexString:
        print("Verification Successful")
    else:
        print("Verification Failed: Hex Strings Do Not Match")

    return compressedHexString


def RLEDecompressHexString(hexString, bitNumber, multiplierBitAmount):
    decompressedHexString = ""
    for i in range(0, len(hexString), bitNumber + multiplierBitAmount):
        multiplier = int(hexString[i:i+multiplierBitAmount], 16)
        value = hexString[i+multiplierBitAmount:i+multiplierBitAmount+bitNumber]
        for i in range(0, multiplier):
            decompressedHexString += value
    return decompressedHexString
