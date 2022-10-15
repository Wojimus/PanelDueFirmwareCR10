//
// Created by wojci on 07/10/2022.
//

#ifndef PANELDUE_WALLPAPER_HPP
#define PANELDUE_WALLPAPER_HPP

#include <cstdint>
#include <cstddef>
#include "General/String.h"
#include "Configuration.hpp"
#include "Hardware/UTFT.hpp"

//static bool WallpaperTilePending;

enum WallpaperTileState {
    WPInit = 0,
    WPHeader,
    WPDataRequest,
    WPDataWait,
    WPData
};

struct WallpaperTile
{
    uint16_t width;
    uint16_t height;
    uint32_t pixel_count;

    String<MaxFilnameLength> filename;
    uint32_t dataSize;
    unsigned char data[3840];
    uint32_t offset;
    uint32_t next;

    enum WallpaperTileState state;

    int16_t parseErr;
    int32_t err;


    void Init();
};

void WallpaperTileInit(struct WallpaperTile &wpTile);
void DrawWallpaperData(struct WallpaperTile &wpTile, UTFT &lcd);

#endif //PANELDUE_WALLPAPER_HPP