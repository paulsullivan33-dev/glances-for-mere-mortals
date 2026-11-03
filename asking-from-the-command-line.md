# Asking from the Command Line

Outcome: any number Glances knows,
printed as plain text a script can read
— no screen, no scraping. This is the
mode that turns Glances from something
you watch into something your other
tools can ask.

## The idea: name the fields

`--stdout` takes a comma-separated list
of **fields**, each written
`plugin.field` (or just a plugin name,
for everything it holds), and prints one
value per line per refresh:

```bash
glances --stdout cpu.total,cpu.user,cpu.system,mem.percent,mem.used,mem.total,load.min1,load.min5,uptime --time 3
```

```text
cpu.total: 26.6
cpu.user: 17.8
cpu.system: 7.3
mem.percent: 94.4
mem.used: 7850135552
mem.total: 8319905792
load.min1: 2.7470703125
load.min5: 1.13818359375
uptime: {'seconds': 2897}
```

(Transcript
`glances-lab/transcripts/t01-stdout-mode.txt`.)
Read the output honestly: byte counts
arrive as raw bytes (7850135552, not
7.85G — the screen's human units are a
courtesy of the screen), load averages
arrive unrounded, and some fields are
small structures (`uptime` prints a
dictionary). Text mode is for quick
checks and for feeding simple tools.

Two behaviours to know before a script
depends on them. Glances in this mode
**runs until stopped** — it is a monitor
printing repeatedly, so a script uses
`timeout` or reads the first block and
closes the pipe. And the **first block's
processor rates are the warm-up zeros**
of chapter 5; a careful reader discards
the first block or asks twice.

## CSV and JSON shapes

`--stdout-csv` takes the same field list
and prints a header row once, then one
comma row per refresh — ready for a
spreadsheet or a plotting script:

```text
cpu.total,mem.percent,load.min1
9.7,94.6,2.28515625
```

`--stdout-json` takes **plugin names**
(not fields) and prints one JSON object
per refresh:

```bash
glances --stdout-json cpu,mem --time 3
```

```json
{"cpu": {"total": 37.9, "user": 24.6, "nice": 0.0, "system": 19.9,
"idle": 32.5, "iowait": 18.6, "irq": 0.0, "steal": 0.9, ...},
"mem": {"total": 8319905792, "available": 404746240, "percent": 95.1, ...}}
```

(Both shapes in transcript t02.) The
JSON form is the one to build on: pipe
it to `jq` (the jq guide in this series
is the natural companion) and a question
like "tell me only the memory percent"
becomes `jq '.mem.percent'` — a number
with the structure still attached, so a
field that moves house in a future
version breaks loudly instead of lying
quietly.

## Choosing fields without guessing

Field names are the plugin's own keys,
and the reliable way to learn them is to
ask for the whole plugin once —
`--stdout-json cpu` shows every key the
`cpu` plugin holds — then narrow to the
fields you need. Guessing has a cost
this lab measured: **an unknown field is
silently ignored**. Transcript t09 asked
for `cpu.total,nonsense.field` and got
`cpu.total`, four times, exit code
untroubled, no warning anywhere on the
output. A typo'd field in a monitoring
script therefore fails as *missing
data*, not as an error — verify a new
field list by eyeballing one full block
before trusting it.

Plugins can also be switched off for a
run —

```bash
glances --disable-plugin network,fs,diskio --stdout cpu.total,mem.percent --time 2
```

— which the lab verified prints the same
values with the named panels dark
(transcript t09). On a machine where a
plugin is slow or its subject is
irrelevant, this is the tidy way to slim
a run.

## The check

```bash
timeout 10 glances --stdout-csv cpu.total,mem.percent --time 3
```

Two or three rows under one header,
values moving between rows, is success.
If the rows are identical to the last
decimal every time, suspect that you are
reading a cached or first sample in a
loop of your own making — Glances's own
repeats, as transcript t01 shows, agree
in story and differ in detail, because
the machine underneath it refuses to sit
still.
