# __name__ guard
if __name__ == '__main__':
  raise EnvironmentError('Cannot run termadd.py; File is a library.')

ALLOWED_SYSTEMS_ = [
  'linux',   # Linux kernel
  'linux2',  # Linux kernel
  'darwin'   # Mac OS X
]

import sys
from secrets import randbits as random

# system check
if sys.platform not in ALLOWED_SYSTEMS_:
  raise OSError('Cannot use termadd.py on a non Linux/Unix system.')

# termadd class
class termadd:
  def __init__(self):
    self.uuid = hex(random(256))[2:]
    self._echo = True

  def noecho(self):
    self._echo = False
  
  def getch(self):
    import tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if self._echo: sys.stdout.write(ch or '')
    return ch
