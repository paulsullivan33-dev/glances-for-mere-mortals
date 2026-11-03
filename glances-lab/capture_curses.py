#!/usr/bin/env python3
"""Run a curses program in a pseudo-terminal, render the final screen with pyte.

Usage: CAPTURE_OUT=file CAPTURE_SECONDS=10 capture_curses.py <cmd> [args...]
The rendered final screen (110x38) is written to CAPTURE_OUT.
"""
import os, pty, select, sys, time
import pyte

cmd = sys.argv[1:]
seconds = float(os.environ.get("CAPTURE_SECONDS", "10"))
out_path = os.environ["CAPTURE_OUT"]
COLS, ROWS = 110, 38

pid, fd = pty.fork()
import fcntl, struct, termios
if pid == 0:
    os.environ["TERM"] = "xterm-256color"
    os.execvp(cmd[0], cmd)

fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", ROWS, COLS, 0, 0))
screen = pyte.Screen(COLS, ROWS)
stream = pyte.ByteStream(screen)
end = time.time() + seconds
while time.time() < end:
    r, _, _ = select.select([fd], [], [], 0.5)
    if fd in r:
        try:
            data = os.read(fd, 65536)
        except OSError:
            break
        if not data:
            break
        stream.feed(data)
try:
    os.kill(pid, 15)
except ProcessLookupError:
    pass
try:
    os.waitpid(pid, 0)
except ChildProcessError:
    pass

lines = [ln.rstrip() for ln in screen.display]
while lines and not lines[-1]:
    lines.pop()
with open(out_path, "w") as fh:
    fh.write("\n".join(lines) + "\n")
print(f"rendered final screen: {len(lines)} lines -> {out_path}")
