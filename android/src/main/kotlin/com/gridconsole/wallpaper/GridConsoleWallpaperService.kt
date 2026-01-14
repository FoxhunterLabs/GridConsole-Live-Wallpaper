package com.gridconsole.wallpaper

import android.content.Intent
import android.service.wallpaper.WallpaperService
import android.view.SurfaceHolder

class GridConsoleWallpaperService : WallpaperService() {

    override fun onCreateEngine(): Engine {
        return GridConsoleEngine()
    }

    inner class GridConsoleEngine : Engine() {

        override fun onVisibilityChanged(visible: Boolean) {
            super.onVisibilityChanged(visible)

            if (visible) {
                val intent = Intent(applicationContext, GridConsoleOverlayActivity::class.java)
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                startActivity(intent)
            } else {
                val stopIntent = Intent(applicationContext, GridConsoleOverlayActivity::class.java)
                stopIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                stopIntent.putExtra("finish", true)
                startActivity(stopIntent)
            }
        }

        override fun onCreate(surfaceHolder: SurfaceHolder) {
            super.onCreate(surfaceHolder)
        }
    }
}
