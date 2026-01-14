from dataclasses import dataclass

@dataclass
class Theme:
    background_rgb: tuple[float, float, float] = (0, 0, 0)
    grid_alpha: float = 0.05

    border_alpha: float = 0.38
    border_alpha_pulse_boost: float = 0.35

    header_alpha: float = 0.95
    subhead_alpha: float = 0.55
    body_alpha: float = 0.82

    header_font_size: int = 14
    subhead_font_size: int = 10
    body_font_size: int = 11

DEFAULT_THEME = Theme()
