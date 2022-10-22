//
// Created by wojci on 07/10/2022.
//

#include <string>
#include "Wallpaper.hpp"
extern "C"
{
#include "base64.h"
}

#define DEBUG	(3) // 0: off, 1: MessageLog, 2: Uart, 3: MessageLog Shortened
#include "Debug.hpp"
#include "Hardware/UTFT.hpp"

void Wallpaper::Init() {
    state = WallpaperState::WPInit;
    width = 0;
    x = 0;
    height = 0;
    y = 0;
    filename.copy("Wallpaper.gcode");
    dataSize = 0;
    next = 0;
    multiplierBitAmount = 0;
}

/**
 * hex2int
 * take a hex string and convert it to a 32bit number (max 8 hex digits)
 */
uint32_t hex2int(char *hex, int startChar, int charAmount) {
    uint32_t val = 0;
    int counter = 0;
    *hex += startChar;
    while (counter < charAmount) {
        // get current character then increment
        char byte = *hex++;
        counter++;
        // transform hex character to the 4bit equivalent number, using the ascii table indexes
        if (byte >= '0' && byte <= '9') byte = byte - '0';
        else if (byte >= 'a' && byte <='f') byte = byte - 'a' + 10;
        else if (byte >= 'A' && byte <='F') byte = byte - 'A' + 10;
        // shift 4 to make space for new digit, and add the 4 bits of the new digit
        val = (val << 4) | (byte & 0xF);
    }
    return val;
}

void DrawWallpaperData(struct Wallpaper &wallpaper, UTFT &lcd) {
    for (int i = 0; i < wallpaper.dataSize; i += 4) {
        uint16_t value = hex2int(reinterpret_cast<char *>(wallpaper.data), i + wallpaper.multiplierBitAmount, 4);
        lcd.setColor(value);
        if (wallpaper.x == wallpaper.width) {
            wallpaper.x = 0;
            wallpaper.y++;
        }
        lcd.drawPixel(wallpaper.x, wallpaper.y);
        wallpaper.x++;
    }

    /*
    //Decode From Base64
    dbg("Buffer Size: %d", sizeof(wallpaper.data));
    dbg("Encoded Wallpaper Length: %d", wallpaper.dataSize);
    uint16_t bitmap[40][24];
    for (int x = 0; x < 40; x++) {
        for (int y = 0; y < 24; y++) {
            int dataIndex = x*y*2;
            bitmap[x][y] = ((wallpaper.data[dataIndex] << 8) + wallpaper.data[dataIndex + 1]);
            //bitmap[x][y] = wpTile.data[dataIndex] | wpTile.data[dataIndex + 1] << 8;
            //bitmap[x][y] = ((uint16_t)wpTile.data[dataIndex] << 16) + (uint16_t)wpTile.data[dataIndex + 1];
        }
    }
    //int decodedLength = base64_decode((const char *)wpTile.data, wpTile.dataSize, wpTile.data);
    //dbg("Decoded Wallpaper Length: %d", decodedLength);
    */
    //lcd.drawBitmap16(0, 0, 80, 48, reinterpret_cast<const uint16_t *>(wallpaper.data), 10);
}