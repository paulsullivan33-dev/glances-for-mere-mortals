# Configuration and Thresholds

Outcome: a config file of your own that
Glances provably obeys — refresh rate,
and the careful / warning / critical
lines that give panels their colours and
the footer its events. The lab's proof
is an event that exists only because the
lab's thresholds said so.

## Where the file lives

Glances reads one config file, chosen in
this order: the path given with
`-C` / `--config`, or its standard
per-user location (on Linux,
`~/.config/glances/glances.conf`). A
complete, commented sample ships with
the package — in the lab's install it
sits at `share/doc/glances/glances.conf`
inside the virtual environment — and
copying that sample and editing it is
the sane way to start, because every
section and default is already written
down in it.

A fact the lab verified the awkward way:
**a missing config file is not an
error.** Pointing `-C` at a path that
does not exist ran Glances on defaults,
exit code untroubled (transcript t09).
When a config change "does nothing",
the first suspicion is therefore not the
file's contents but whether Glances is
reading the file at all — a wrong path
fails silently. Change something loud
(the refresh rate) and watch the screen
obey, before tuning anything subtle.

## The shape of the file

The file is INI: a `[global]` section,
then one section per plugin. The global
section carries the refresh rate
(`refresh=2`, the floor Glances allows),
whether it checks PyPI for a newer
version (`check_update`), and the
history size (1200 samples by default).
Each plugin section carries its lines,
named after the value they judge:

```ini
[cpu]
total_careful=65
user_careful=50
user_warning=70
user_critical=90

[mem]
careful=50
warning=70
critical=90

[load]
careful=0.7
warning=1.0
critical=5.0
```

(Extracted from the shipped sample;
transcript
`glances-lab/transcripts/t04a-default-thresholds-extract.txt`.)
Note the load lines are *fractions of
the core count*, as chapter 5 explained,
and that processor lines are per-field
(`user_`, `system_`, `total_` and
friends) while memory judges one
percentage. The filesystem section
(`[fs]`, 50 / 70 / 90 against used
percent) and swap (`[memswap]`) follow
the memory pattern.

Crossing **careful** colours a panel;
crossing **warning** and **critical**
also opens an **event** in the alert
plugin's history — the footer lines and
the API's `/api/4/alert` — which stays
open, marked *ongoing*, until the value
falls back, and records its minimum,
maximum, average and duration. An event
is Glances's memory of a bad patch, and
it is the difference between "the screen
was red when I looked" and "memory sat
above warning for eight minutes at
88.7%, and here is the receipt".

## The lab's low-threshold experiment

To prove the machinery end to end, the
lab wrote a config with lines no sane
operator would ship — processor warning
at 10, critical at 20 — and the shipped
sample's sober defaults nowhere in it:

```ini
[global]
refresh=2
check_update=false

[cpu]
user_careful=5
user_warning=10
user_critical=20
...
[mem]
careful=50
warning=70
critical=85
```

(The full file is `glances-lab/lab-glances.conf`.)
Within seconds the screen's footer
carried two events: the memory event the
busy sandbox had already earned, now
judged against the lab's lower critical
line, and a brand-new one —

```text
(0:00:08) - WARNING on CPU_USER
```

— an eight-second warning event for
processor user time crossing 10%, on a
machine doing nothing unusual at all.
(Transcript
`glances-lab/transcripts/t04-config-and-thresholds.txt`.)
Under the shipped defaults (warning at
70) that event could not exist. That is
the whole lesson in one line: **events
are opinions, and the config file is
where the opinions live.** Tune the
lines to your machine — a small server
idling at 60% memory forever wants its
warning above its normal, or its history
fills with one permanent ongoing event
and real excursions stop standing out.

## Actions, honestly labelled

The project's documentation describes
*actions*: commands Glances can run when
a value crosses a line (the classic
example is logging or notifying). The
lab did not run actions — wiring a
monitor to execute commands deserves its
own careful test, and the sandbox's
rules about background effects made it
the wrong place to improvise one — so
this guide names the feature as existing
and documented, and claims nothing about
its behaviour. If you adopt it, test it
with a harmless command first, the way
chapter 7's thresholds were tested with
harmless lines.

## The check

Copy the sample config, lower one line
absurdly (memory warning to 10 is
reliable on any real machine), start
Glances with `-C`, and watch the footer.
An event with your line's name on it is
proof the file is being read and the
machinery works. Put the line back
before you forget why the machine is
crying wolf.
