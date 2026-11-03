# Your First Look

Outcome: the terminal screen open, every
panel named, and one number on it
cross-checked against a second source —
so you know the picture is the machine
and not a screensaver. Run:

```bash
glances
```

Glances takes over the terminal and
redraws every two seconds by default
(`--time 3` slows the refresh to three;
the flag's name is the refresh interval
in seconds). Press `q` to leave. The
lab's screen, captured by driving a real
terminal and rendering its final frame
(the script is `glances-lab/capture_curses.py`,
the evidence is transcript
`glances-lab/transcripts/t03-curses-screen.txt`),
reads like this, trimmed to its bones:

```text
htch-runtime Ubuntu 24.04 64bit / Linux 7.0.0-39-generic   Uptime: 0:49:31
Frequency 1.50GHz   CPU      48.5%   MEM     94.3%   SWAP     0.0%   LOAD    4core
CPU  [bar  48.5%]   user     22.9%   total   7.75G   total       0   1 min    1.95
MEM  [bar  94.3%]   system   21.7%   used    7.30G   used        0   5 min    1.23
LOAD [bar  25.1%]   iowait   15.3%   free    179M    free        0   15 min   1.01

NETWORK  Rx/s Tx/s        TASKS  12 (52 thr), 1 run, 11 slp, 0 oth
DISK I/O R/s  W/s         CPU%  MEM%  VIRT  RES  PID USER  TIME+ ... Command
FILE SYS Used Total
...                       EVENTS history / High memory consumption
```

## Reading it in order

**The header line** names the machine,
its operating system and kernel, its
public address (chapter 14 explains the
`--hide-public-info` flag for screens you
share), and the uptime.

**The quicklook bar** — CPU, MEM, SWAP,
LOAD across the top — is the whole
machine in four numbers. Each has a bar
and a percentage, and each percentage
has a colour earned from the thresholds
of chapter 7. Under the bar sits the
detail block: the processor split into
user / system / iowait and friends on
the left, memory and swap totals in the
middle, and the three load averages on
the right.

**The left column** holds the slow
panels: NETWORK (bytes received and sent
per second, per interface), DISK I/O
(reads and writes per second, per
device) and FILE SYS (each filesystem's
used and total space). On a wide
terminal, sensors, ports and other
panels join them; on a narrow one,
Glances drops panels rather than
crushing them, which is why two readers'
screenshots of the same machine can
legitimately differ.

**The right side is the process list** —
the census and the suspects. Its header
counts the tasks and their states; its
rows are sorted automatically by
appetite, busiest first. In the lab's
capture the top row is the sandbox's own
daemon at 45.9% of a processor — the
screen naming the machine's real tenant,
which is exactly the job.

**The footer is the event history.**
The lab's capture ends with `High memory
consumption` and an ongoing MEM event:
the machine's memory sat above the
warning line, so the alert plugin
opened an event, named it, and will
close it when the number falls. Chapter
7 is about those lines and how to earn
(or avoid) them.

## The check

Pick the memory percentage from the
quicklook bar and compare it with a
second witness:

```bash
free -m
glances --stdout mem.percent --time 3
```

The two will not match to the decimal —
they sample different seconds — but they
must tell the same story (in the lab:
both said "about nine-tenths full").
If they disagree wildly, you are looking
at different machines, different
moments, or a Glances pointed somewhere
unexpected — chapter 9's client mode
makes that a real possibility worth
ruling out first.

## Keys worth knowing now

The screen is not read-only. The keys
this guide uses are `q` (quit), `h`
(help — the full key list, drawn by
Glances itself), `1` (per-processor view
on or off), `p` (sort processes by
name), `c` and `m` (sort by processor
and by memory), and `x` (clear the event
history). The rest are discoverable from
`h`, which is the honest way to learn
them: against the live screen, not a
table in a book.
