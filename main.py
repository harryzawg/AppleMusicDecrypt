import asyncio
import sys

from src.cmd import NewInteractiveShell

if __name__ == '__main__':
    if sys.platform in ('win32', 'cygwin', 'cli'):
        try:
            import uvloop
            uvloop.install()
        except ImportError:
            print("uvloop not installed. Falling back to default asyncio.")
    else:
        import uvloop
        uvloop.install()
    
    loop = asyncio.get_event_loop()
    cmd = NewInteractiveShell(loop)
    try:
        loop.run_until_complete(cmd.start())
    except KeyboardInterrupt:
        loop.stop()
