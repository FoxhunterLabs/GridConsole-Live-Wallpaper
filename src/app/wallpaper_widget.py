import random
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.widget import Widget

from .settings import DEFAULT_SETTINGS
from .themes import DEFAULT_THEME
from .panels import generate_panels, Panel
from .logs import rand_log_line, HEADERS

FONT_NAME = "monospace"  # ✅ standard system monospace

class HudWallpaper(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = DEFAULT_SETTINGS
        self.theme = DEFAULT_THEME

        self.t = 0.0
        self.last_layout = 0.0

        self.panels: list[Panel] = generate_panels(self.settings.grid_cols, self.settings.grid_rows)
        Clock.schedule_interval(self.update, 1 / self.settings.fps)

    def on_touch_down(self, touch):
        W, H = self.width, self.height
        if W <= 1 or H <= 1:
            return True

        cell_w = W / self.settings.grid_cols
        cell_h = H / self.settings.grid_rows
        gx = int(touch.x // cell_w)
        gy = int(touch.y // cell_h)

        for p in self.panels:
            if p.gx <= gx < p.gx + p.gw and p.gy <= gy < p.gy + p.gh:
                p.pulse = 1.0
                if random.random() < 0.6:
                    p.header = random.choice(HEADERS)
                for _ in range(random.randint(2, 6)):
                    p.lines.append(rand_log_line())
                p.lines = p.lines[-self.settings.max_lines_per_panel:]
                break
        return True

    def update(self, dt):
        self.t += dt

        # slow evolution (no chaos)
        if self.t - self.last_layout > self.settings.layout_refresh_seconds and random.random() < 0.04:
            self.last_layout = self.t
            self.panels = generate_panels(self.settings.grid_cols, self.settings.grid_rows)

        for p in self.panels:
            if random.random() < 0.10:
                p.lines.append(rand_log_line())
                p.lines = p.lines[-self.settings.max_lines_per_panel:]
            p.pulse = max(0.0, p.pulse - dt * 1.5)

        self.canvas.clear()
        with self.canvas:
            self._draw()

    def _label(self, text, x, y, size, alpha):
        lab = CoreLabel(text=text, font_size=size, font_name=FONT_NAME)
        lab.refresh()
        Color(1, 1, 1, alpha)
        Rectangle(texture=lab.texture, pos=(x, y), size=lab.texture.size)

    def _draw(self):
        W, H = self.width, self.height
        if W < 2 or H < 2:
            return

        # background
        Color(*self.theme.background_rgb, 1)
        Rectangle(pos=self.pos, size=(W, H))

        # faint global grid (background)
        Color(1, 1, 1, self.theme.grid_alpha)
        cols = 10
        rows = 18
        for i in range(1, cols):
            x = W * i / cols
            Line(points=[x, 0, x, H], width=1)
        for j in range(1, rows):
            y = H * j / rows
            Line(points=[0, y, W, y], width=1)

        # panels
        cell_w = W / self.settings.grid_cols
        cell_h = H / self.settings.grid_rows

        for p in self.panels:
            x = p.gx * cell_w
            y = p.gy * cell_h
            w = p.gw * cell_w
            h = p.gh * cell_h

            inset = 6

            # border pulse
            border_alpha = self.theme.border_alpha + self.theme.border_alpha_pulse_boost * p.pulse
            Color(1, 1, 1, border_alpha)
            Line(rectangle=(x + inset, y + inset, w - 2 * inset, h - 2 * inset), width=1)

            # header separator
            Color(1, 1, 1, 0.15)
            Line(points=[x + inset + 6, y + h - 32, x + w - inset - 6, y + h - 32], width=1)

            # header text
            self._label(p.header, x + inset + 10, y + h - 26, self.theme.header_font_size, self.theme.header_alpha)

            # subhead
            self._label(p.subhead, x + inset + 10, y + h - 44, self.theme.subhead_font_size, self.theme.subhead_alpha)

            # body text
            font_size = self.theme.body_font_size
            line_h = font_size + 2
            max_lines = max(1, int((h - 60) / line_h))
            visible = p.lines[-max_lines:]

            start_y = y + inset + 10
            for i, line in enumerate(reversed(visible)):
                yy = start_y + i * line_h
                if yy > y + h - 60:
                    break
                self._label(line[:90], x + inset + 10, yy, font_size, self.theme.body_alpha)
