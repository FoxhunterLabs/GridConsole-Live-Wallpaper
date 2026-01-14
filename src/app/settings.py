from dataclasses import dataclass

@dataclass
class Settings:
    fps: int = 30
    grid_cols: int = 6
    grid_rows: int = 14
    layout_refresh_seconds: int = 25
    max_lines_per_panel: int = 90

DEFAULT_SETTINGS = Settings()
