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

void WallpaperTile::Init() {
    filename.Clear();
    state = WallpaperTileState::WPInit;
    parseErr = 0;
    err = 0;
    dataSize = 0;
    offset = 0;
    next = 0;
}

void WallpaperTileInit(struct WallpaperTile &wpTile)
{
    wpTile.width = 0;
    wpTile.height = 0;
    wpTile.pixel_count = 0;
}

void DrawWallpaperData(struct WallpaperTile &wpTile, UTFT &lcd) {
    //Decode From Base64
    dbg("Buffer Size: %d", sizeof(wpTile.data));
    dbg("Encoded Wallpaper Length: %d", wpTile.dataSize);
    uint16_t bitmap[40][24];
    for (int x = 0; x < 40; x++) {
        for (int y = 0; y < 24; y++) {
            int dataIndex = x*y*2;
            bitmap[x][y] = ((wpTile.data[dataIndex] << 8) + wpTile.data[dataIndex+1]);
            //bitmap[x][y] = wpTile.data[dataIndex] | wpTile.data[dataIndex + 1] << 8;
            //bitmap[x][y] = ((uint16_t)wpTile.data[dataIndex] << 16) + (uint16_t)wpTile.data[dataIndex + 1];
        }
    }
    //int decodedLength = base64_decode((const char *)wpTile.data, wpTile.dataSize, wpTile.data);
    //dbg("Decoded Wallpaper Length: %d", decodedLength);
    lcd.drawBitmap16(0, 0, 40, 24, reinterpret_cast<const uint16_t *>(bitmap), 10);
}