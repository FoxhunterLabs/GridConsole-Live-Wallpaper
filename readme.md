# GridConsole Live Wallpaper

<img width="1916" height="1016" alt="image" src="https://github.com/user-attachments/assets/2693543d-a18f-432c-a798-29dfbaa9ead1" />


GridConsole is a generative Android live wallpaper that looks like a monochrome “AI console” grid:
- crisp white HUD panels
- subtle background grid lines
- scrolling terminal-style logs
- layouts evolve over time
- tap panels to pulse + refresh content

It’s meant to match that clean “terminal tiles / HUD mosaic” vibe — sharp, minimal, and alive.

---

## What’s in this repo

✅ Python (Kivy) renderer  
✅ Android Live Wallpaper service (Kotlin)  
✅ Shows up in the system Live Wallpaper picker  
✅ Generative panel packing + scrolling content  
✅ Tap interactivity

---

## Why Kotlin exists at all (real talk)

Android **requires** live wallpapers to be exposed through a `WallpaperService`.  
That part can’t be pure Python.

So Kotlin handles the wallpaper lifecycle, and Python handles *everything visual*.

---

## Run on desktop (best way to tune the look)

```bash
pip install -r requirements.txt
python src/main.py
________________________________________
Build Android APK (debug)
Buildozer works best on Linux.
pip install buildozer
buildozer -v android debug
Your APK will land in:
bin/
________________________________________
Install + set as Live Wallpaper
1.	Install the APK on your Android device
2.	Open:
o	Settings → Wallpaper & style
3.	Choose:
o	Live wallpapers
4.	Select:
o	GridConsole Live Wallpaper
________________________________________
Customize the visuals
Density / layout
Edit:
•	src/app/settings.py
o	grid_cols, grid_rows
o	layout_refresh_seconds
o	fps
Borders / text / alpha
Edit:
•	src/app/themes.py
o	border intensity
o	grid intensity
o	font sizes
o	text brightness
Log style + labels
Edit:
•	src/app/logs.py
o	headers
o	subheads
o	terminal log generator
Panel generation rules
Edit:
•	src/app/panels.py
o	how panels pack into the grid
o	panel size distribution
o	number of panels
________________________________________
License
MIT
