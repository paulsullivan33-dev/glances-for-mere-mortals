# Glances for Mere Mortals

Your machine feels slow. Which part of it
is struggling — the processor, the memory,
a disk, the network, or one greedy
program? The classic tools each answer
one of those questions. **Glances**
answers all of them on one screen: one
program that watches the whole machine
and draws processor, memory, load, swap,
disks, network and the process list
together, refreshing every couple of
seconds, with colours that change when a
number crosses a line you set.

That one screen is only the first of its
shapes. The same numbers come out as
plain text lines for a script, as CSV and
JSON files that keep history, as a web
page you open in a browser, and as a
**REST API** — a way for other programs
to ask for the numbers over HTTP. One
Glances can also serve its screen to
another machine, so a small server in a
cupboard gets watched from your desk.
And it watches only the machine it runs
on, with no account and no cloud: the
numbers it collects describe your
hardware, and they stay yours unless you
choose to send them somewhere.

The lab behind this guide ran the real
thing: **Glances 4.5.8** (API version 4,
on psutil 7.2.2), installed from PyPI
into a Python virtual environment on a
small shared Linux machine. Against it
the lab read the terminal screen and
rendered it exactly as a terminal shows
it, asked for single numbers from the
command line in text, CSV and JSON,
wrote a config file with deliberately
low thresholds and watched the alert
machinery fire events that the defaults
would never have raised, ran the web
server on a loopback port and queried
its API endpoint by endpoint, connected
a client to a Glances server and read
the remote screen, and exported real
history to CSV and JSON files. It also
broke things on purpose: a web server
started twice on one port, a config file
that does not exist, a field name that
does not exist — and found that
Glances's failure style is often silence,
which this guide treats as a fact worth
knowing, not a detail worth hiding.

What the lab could not do, it did not
fake. The sandbox has no Docker, so the
containers plugin reported an honest
empty list; it has no hardware sensors,
so the temperature readings other
machines show are described, not
measured; and its long list of exporters
to databases and message queues was
tested only for the two file exporters
that need nothing else running. Where a
feature is taught from the project's
documentation rather than from a lab
run, the chapter says so, and
`criteria.md` keeps the full ledger.

One warning belongs up front, because the
lab's own server printed it: Glances's
server modes, left unguarded, will show
a detailed picture of your machine —
processes, addresses, filesystems — to
anyone who can reach the port. Chapters 8
and 9 show the password and
binding options, and this guide's own
lab never bound anything beyond
loopback.

## What this guide covers

- [**What Glances is**](what-glances-is.md) —
  the mental model: one collector, many
  windows onto the same numbers, and the
  difference between watching and
  recording
- [**The moving parts**](the-moving-parts.md) —
  the psutil collector underneath, the
  plugins that each own one panel, the
  thresholds, and the four output shapes
- [**Installing Glances**](installing-glances.md) —
  the pip install, the virtual
  environment, and the extra package the
  web server needs before it will start
- [**Your first look**](your-first-look.md) —
  the terminal screen read panel by
  panel, with the check that proves what
  you are looking at
- [**Reading the numbers**](reading-the-numbers.md) —
  processor percentages as rates, memory
  read honestly, load against core
  count, and the process list's verdict
- [**Asking from the command line**](asking-from-the-command-line.md) —
  single numbers as text, CSV or JSON for
  scripts, and the first-sample trap in
  every rate
- [**Configuration and thresholds**](configuration-and-thresholds.md) —
  the config file, the careful / warning
  / critical lines for each panel, and
  the events those lines produce
- [**The web server and the API**](web-server-and-api.md) —
  the browser page, the REST endpoints,
  and asking for exactly one field
- [**Watching other machines**](watching-other-machines.md) —
  server mode, a client reading a remote
  screen, and the password the log tells
  you to set
- [**Exporting history**](exporting-history.md) —
  CSV and JSON files that remember what
  the screen forgets, and the honest
  state of the other exporters
- [**Recipes**](recipes.md) — a one-line
  health check for a script, a quiet
  overnight history, a web page for a
  headless box, and thresholds tuned to
  a small machine
- [**The neighbours**](the-neighbours.md) —
  top and htop, btop, Cockpit, and the
  Prometheus world: what each does that
  Glances doesn't, and vice versa
- [**Limits**](limits.md) — rates that
  start at zero, panels that are empty
  without the hardware or the daemon
  behind them, silence as a failure
  style, and history that lives in
  memory only
- [**Troubleshooting**](troubleshooting.md) —
  the web server that will not start,
  the port already in use, the typo
  nobody reports, and the traps this
  guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Running Glances in a container, or
watching containers from inside one —
the lab had no container runtime, and
the chapter on limits says exactly what
that leaves unproven. Feeding its
numbers into a full monitoring stack
(Grafana dashboards, alert managers,
databases that keep years of history) is
pointed at, not taught: Glances is a
watcher and a witness, and chapter 11
explains where its memory ends and a
real time-series database's begins.
Windows and macOS installs are described
from the documentation; every procedure
in the lab ran on Linux.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before installing anything —
knowing that every panel is a plugin fed
by one collector turns later surprises
into named problems. Chapter 3 installs;
chapter 4 puts the screen in front of
you in the same sitting. Chapter 7 is
the one to read slowly: thresholds are
where Glances stops being a picture and
starts being an opinion, and the lab's
low-threshold experiment shows exactly
how an event is born. The lab's
transcripts live in
`glances-lab/transcripts/`; its screen
capture script is
`glances-lab/capture_curses.py` and its
threshold config is
`glances-lab/lab-glances.conf`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Watching Your System for Mere Mortals](https://paulsullivan33-dev.github.io/watching-your-system-for-mere-mortals/)
- [btop for Mere Mortals](https://paulsullivan33-dev.github.io/btop-for-mere-mortals/)
- [Cockpit for Mere Mortals](https://paulsullivan33-dev.github.io/cockpit-for-mere-mortals/)
- [Prometheus and Grafana for Mere Mortals](https://paulsullivan33-dev.github.io/prometheus-and-grafana-for-mere-mortals/)
- [Beszel for Mere Mortals](https://paulsullivan33-dev.github.io/beszel-for-mere-mortals/)
- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)
- [jq for Mere Mortals](https://paulsullivan33-dev.github.io/jq-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/glances-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/glances-for-mere-mortals/blob/main/LICENSE-CODE).
