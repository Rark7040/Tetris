import asyncio

from test.src.hard.main_display.MainDisplay import MainDisplay

display = MainDisplay()
display.display(
    [
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,

        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
    ]
)
asyncio.get_event_loop().run_until_complete(display.async_loop())
