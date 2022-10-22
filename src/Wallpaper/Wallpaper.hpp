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

static bool WallpaperPending;

enum WallpaperState {
    WPInit = 0,
    WPHeader,
    WPDataRequest,
    WPDataWait,
    WPData
};

struct Wallpaper
{
    enum WallpaperState state;

    uint16_t width;
    uint16_t x;
    uint16_t height;
    uint16_t y;

    String<MaxFilenameLength> filename;
    uint16_t dataSize;
    unsigned char data[2048];
    uint32_t next;
    uint16_t multiplierBitAmount;

    void Init();
};

void DrawWallpaperData(struct Wallpaper &wallpaper, UTFT &lcd);

#endif //PANELDUE_WALLPAPER_HPP