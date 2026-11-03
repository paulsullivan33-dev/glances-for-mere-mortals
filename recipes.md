# Recipes

Outcome: four complete jobs done with
the parts the earlier chapters proved.
Each recipe names the chapters it
stands on, and none introduces a new
mechanism.

## 1. A one-line health answer for a script

*Stands on chapters 6 and 5.* Another
program — a status page, a cron job, a
shell prompt — wants one number, not a
screen:

```bash
timeout 12 glances --stdout-json mem --time 3 \
  | tail -1 | jq -r '.mem.percent'
```

The `tail -1` is the honest detail: the
first JSON block can carry warm-up
values, so the script reads the *last*
block of a short run rather than the
first block of a long one. For
processor, apply chapter 5's rule and
discard the first block the same way —
a rate read once is a rate not yet
measured.

## 2. The quiet overnight history

*Stands on chapter 10.* A machine
misbehaves at 3 a.m. and is innocent by
9. Leave a witness:

```bash
glances --export csv --export-csv-file ~/glances-night.csv \
  --export-csv-overwrite --time 10
```

started in the evening (under `tmux` or
`nohup` so it survives your logout) and
stopped in the morning. Ten seconds is
the refresh for a history: fine enough
to catch a ten-minute storm, coarse
enough that the file stays a size a
spreadsheet will open. In the morning,
the columns that answer "what, and
when" are `timestamp` beside
`cpu.total`, `mem.percent`,
`load.min1` and the busy disk's
`diskio` rates — and chapter 10's
warning applies: the file writes
everything, so bring a column-cutting
tool and no expectations of smallness.

## 3. A web page for a headless box

*Stands on chapters 8 and 3.* On the
box itself:

```bash
glances -w --bind 127.0.0.1 --port 18083 --time 3
```

—and reach it through an SSH tunnel from
your desk (`ssh -L 18083:127.0.0.1:18083 box`),
so the bind stays loopback, the traffic
travels inside SSH, and no Glances port
faces the network at all. This is the
arrangement the lab's rules point at:
the web page's convenience with the
server mode's warning answered by never
exposing the port. Where a tunnel is
impossible and the port must face a
network, chapter 8's password stops
being optional.

## 4. Thresholds tuned to a small machine

*Stands on chapter 7.* A little server
that normally idles at 55–65% memory
(cache doing its job) earns a permanent
ongoing event under the default warning
of 70 the first warm week it has. Its
honest config moves the *memory* lines,
not the machinery:

```ini
[mem]
careful=60
warning=80
critical=92
```

— warning now means "above anything
this machine does on a normal day",
which is the only definition of warning
worth paging a human for. Leave the
processor lines at their defaults until
you have a week's screen-watching to
argue with them; chapter 7's experiment
is the method (lower a line on purpose,
watch an event be born, learn what the
line means) and a production config is
where its lessons get spent, one line
at a time.
