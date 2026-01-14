package com.gridconsole.wallpaper

import android.content.Intent
import android.os.Bundle
import org.kivy.android.PythonActivity

/**
 * Runs the Kivy renderer in a transparent overlay activity.
 * This is started/stopped by the wallpaper service visibility changes.
 */
class GridConsoleOverlayActivity : PythonActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        // Finish request from wallpaper engine
        if (intent?.getBooleanExtra("finish", false) == true) {
            finish()
            return
        }

        // Start service_main.py instead of main.py
        this.intent = Intent(this, GridConsoleOverlayActivity::class.java).apply {
            putExtra("androidPrivate", filesDir.toString())
            putExtra("androidArgument", "service_main.py")
            putExtra("service", "1")
        }

        super.onCreate(savedInstanceState)
    }
}
