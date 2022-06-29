# standard libraries
import sys
import asyncio
import functools

# dependencies
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import qasync

# local modules
from window import Window


async def main():
    '''
    required by qasync
    '''
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = qasync.QApplication.instance()
    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(functools.partial(close_future, future, loop))

    window = Window()
    window.show()

    await future
    return True



if __name__ == '__main__':
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)