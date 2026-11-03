# Glossary

**Alert plugin / event** — the part of
Glances that keeps the event history.
When a value sits past its warning or
critical line, an event opens, records
its extremes and duration, and closes
when the value falls back.

**AMPS** — Application Monitoring
Process support: a plugin that watches
named processes against counts you set
in the config file (the defaults watch
for Dropbox, Python, Nginx and friends,
and report counts of zero, harmlessly,
on machines without them).

**Bind address** — the network address
a server listens on. `127.0.0.1` means
"this machine only" (loopback);
anything wider is a decision to be
reachable.

**Careful / warning / critical** — the
three threshold lines per value in the
config file. Careful colours a panel;
warning and critical also open events.

**Collector** — the layer that gathers
the raw numbers. In Glances that is
psutil; everything drawn is drawn from
its readings.

**Curses** — the terminal graphics
library behind Glances's default
screen: panels and bars drawn in a text
terminal, refreshed in place.

**Exporter** — a module that writes each
refresh somewhere durable: the csv and
json file exporters, and a long list
aimed at databases, queues and
Prometheus.

**Field** — one named value of a plugin,
written `plugin.field` (as in
`mem.percent`) when asking from the
command line, and flattened to the same
dotted name in exports.

**History** — the samples Glances keeps
in memory (1200 by default) for its
graphs and events. It ends when Glances
does; exports are the durable form.

**iowait** — processor time spent idle
while waiting for a disk to answer.
High iowait is a storage story wearing
a processor costume.

**Load average** — the average number
of processes running or waiting to run,
over 1, 5 and 15 minutes. Read against
the core count; Glances's load
thresholds are fractions of that count.

**Loopback** — the machine talking to
itself at 127.0.0.1. Servers bound to
loopback cannot be reached from the
network at all.

**Plugin** — one module owning one
panel and one subject: `cpu`, `mem`,
`fs`, `processlist` and thirty-one
more in this guide's build.

**psutil** — the cross-platform Python
library Glances collects through. Its
version is reported beside Glances's
own, because it is half the story.

**Quicklook** — the summary plugin:
processor, memory, swap and load in one
bar across the top of the screen.

**Rate** — a value computed between two
samples, like a percentage of an
interval. Rates read 0.0 on the first
sample, which has no predecessor.

**Refresh** — the interval between
samples, set by `--time` or the config
file's `refresh`; two seconds is the
floor and the default.

**Resident memory (RES)** — the memory
a process actually holds in RAM. The
process list's believable memory
column; VIRT is merely its address
space claim.

**REST API** — the web server's JSON
door: `/api/4/<plugin>` and
`/api/4/<plugin>/<field>` over HTTP,
for programs to ask with.

**Swap** — disk space used as overflow
memory. A swap panel in steady use, not
a high memory percentage, is the honest
sign of a machine short of memory.

**XML-RPC server** — the service behind
server mode (`glances -s`): a Glances
client draws its screen from it. A
different protocol from the REST API,
which serves browsers and scripts.
