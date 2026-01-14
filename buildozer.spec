[app]
title = GridConsole Live Wallpaper
package.name = gridconsole
package.domain = com.gridconsole.wallpaper

source.dir = .
source.include_exts = py,kv,xml,kt,png,jpg

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions =
android.api = 34
android.minapi = 24
android.ndk = 25b

# Include Kotlin source folder
android.add_src = android/src/main/kotlin

log_level = 2

[buildozer]
warn_on_root = 1
