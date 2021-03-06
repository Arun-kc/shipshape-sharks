import asyncio
from typing import Any

from asciimatics.effects import Cycle, Stars
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def update_screen(end_time: Any, loop: Any, screen: Any) -> None:
    """Upadates Screen"""
    screen.draw_next_frame()
    if loop.time() < end_time:
        loop.call_later(0.05, update_screen, end_time, loop, screen)
    else:
        loop.stop()


# Define the scene that you'd like to play.
screen = Screen.open()
effects = [
    Cycle(
        screen,
        FigletText("Box", font='big'),
        screen.height // 2 - 8),
    Cycle(
        screen,
        FigletText("RPG!", font='big'),
        screen.height // 2 + 3),
    Stars(screen, (screen.width + screen.height) // 2)
]
screen.set_scenes([Scene(effects, 500)])

# Schedule the first call to display_date()
try:
    loop = asyncio.get_event_loop()
    end_time = loop.time() + 5.0
    loop.call_soon(update_screen, end_time, loop, screen)

    # Blocking call interrupted by loop.stop()
    loop.run_forever()
    screen.close()
except ResizeScreenError:
    pass
