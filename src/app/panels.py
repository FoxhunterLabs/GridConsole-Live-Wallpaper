import random
from dataclasses import dataclass
from .logs import HEADERS, SUBHEADS, rand_log_line

@dataclass
class Panel:
    gx: int
    gy: int
    gw: int
    gh: int
    header: str
    subhead: str
    lines: list[str]
    scroll_speed: float
    pulse: float

def generate_panels(grid_cols: int, grid_rows: int, count_min=14, count_max=20) -> list[Panel]:
    occupied = [[False] * grid_rows for _ in range(grid_cols)]
    panels: list[Panel] = []

    def can_place(x, y, w, h):
        if x + w > grid_cols or y + h > grid_rows:
            return False
        for ix in range(x, x + w):
            for iy in range(y, y + h):
                if occupied[ix][iy]:
                    return False
        return True

    def mark(x, y, w, h):
        for ix in range(x, x + w):
            for iy in range(y, y + h):
                occupied[ix][iy] = True

    target = random.randint(count_min, count_max)

    for _ in range(target):
        for _try in range(60):
            w = random.choice([1, 1, 2, 2, 3])
            h = random.choice([1, 2, 2, 3, 4])
            x = random.randint(0, grid_cols - 1)
            y = random.randint(0, grid_rows - 1)

            if can_place(x, y, w, h):
                mark(x, y, w, h)
                panels.append(
                    Panel(
                        gx=x,
                        gy=y,
                        gw=w,
                        gh=h,
                        header=random.choice(HEADERS),
                        subhead=random.choice(SUBHEADS),
                        lines=[rand_log_line() for _ in range(random.randint(10, 22))],
                        scroll_speed=random.uniform(10, 22),
                        pulse=0.0,
                    )
                )
                break

    return panels
