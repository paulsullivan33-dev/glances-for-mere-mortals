# The Moving Parts

Glances looks like one program, and at
the command line it is one program.
Inside, the work is divided cleanly:
one collector underneath, a row of
plugins that each own one panel, a set
of thresholds that give the panels their
colours and opinions, and a row of
outputs that present the same numbers in
different shapes. Nearly every surprise
in this guide — including most of the
troubleshooting chapter — is one of
these parts behaving exactly as designed
while the reader expected another part's
behaviour. This chapter names them.

## The collector: psutil

Glances does not read the kernel's files
and counters itself. It asks **psutil**,
a cross-platform Python library for
process and system information, and
psutil does the grubby, operating-system
specific work: processor times, memory
counters, disk and network statistics,
the process census. This is why Glances
runs the same way on Linux, Windows and
macOS while the tools it replaces are
Unix-only — and why its version report
names two versions, its own and
psutil's:

```text
Glances version:	4.5.8
Glances API version:	4
PsUtil version:		7.2.2
```

(Transcript `glances-lab/transcripts/t00-version-and-help.txt`.)

One consequence follows from the
collector's design and runs through the
whole guide: a processor *percentage* is
not a reading, it is a **rate** — the
difference between two counter snapshots
divided by the time between them. The
first sample after any start has nothing
to subtract from, so the first processor
numbers are always zero. Chapter 6 and
chapter 9 both meet this fact in the
wild.

## The plugins: one panel each

Every panel on the screen is a
**plugin**: a small module that owns one
subject. The lab's build lists 35 of
them:

```text
Plugins list: alert, amps, cloud, connections, containers, core,
cpu, diskio, folders, fs, gpu, help, ip, irq, load, mem, memswap,
mpp, network, now, npu, percpu, ports, processcount, processlist,
programlist, psutilversion, quicklook, raid, smart, sensors,
system, uptime, version, vms, wifi
```

(From `glances --modules-list`, transcript
t00.) Some are obvious (`cpu`, `mem`,
`network`, `processlist`); some are
infrastructure wearing a plugin's
clothes — `quicklook` is the summary bar
at the top, `alert` is the event history
at the bottom, `amps` watches named
processes against counts you set.
Plugins can be switched off by name
(`--disable-plugin`), which the lab
verified from the command line, and a
plugin with nothing to report says so
honestly: in the sandbox, `cloud` and
`connections` report NA (not available),
and `containers` reports an empty list
because there is no container runtime to
ask. An empty panel is a plugin telling
the truth about its subject, not a
malfunction.

## The thresholds: where colour comes from

Each plugin's numbers are judged against
three lines in the config file —
**careful**, **warning** and
**critical** — and the judgement drives
the colour of the panel (green, then
violet, orange and red in the default
scheme's rising order of concern) and,
past the higher lines, entries in the
`alert` plugin's event history. The
shipped defaults are sober: processor
user time is careful at 50, warning at
70, critical at 90; memory is 50 / 70 /
90. The defaults are a starting opinion,
not a law of nature — chapter 7 rewrites
them on purpose and watches events
appear that the defaults would never
have raised.

## The outputs: four shapes, one truth

The collected, judged numbers leave
through four doors:

- **Curses**, the terminal screen —
  Glances's home ground.
- **Stdout** — text, CSV or JSON lines
  printed per refresh (chapter 6).
- **The web server** — an HTML page for
  browsers and a REST API underneath it,
  served by FastAPI in this version
  (chapter 8).
- **Exporters** — 23 of them in the
  lab's build, from the humble `csv` and
  `json` file writers to databases
  (InfluxDB, Elasticsearch, MongoDB),
  queues (Kafka, RabbitMQ, MQTT) and a
  Prometheus endpoint. Only the two file
  exporters were run in the lab; the
  rest are listed honestly in chapter 10.

Behind the web and server shapes there is
one more moving part worth naming: the
**XML-RPC server** that serves the
terminal client of chapter 9 — a
different protocol from the REST API,
which is why a Glances client talks to
`glances -s` and not to `glances -w`.

## Which part holds what

| Question | The part that answers it |
| --- | --- |
| Why is the first CPU reading 0.0? | The collector — a rate needs two samples |
| Why is this panel empty or NA? | That plugin — its subject is absent here |
| Why did the memory bar change colour? | The thresholds in the config file |
| Why is there an event in the footer? | The alert plugin, judging a threshold |
| Why won't the web server start? | The output's own dependency (FastAPI) is missing |
| Why do the CSV columns have dots in their names? | The exporter's flattening of plugin.field names |
| Why can a browser read it but a Glances client can't? | Two different servers — REST for browsers, XML-RPC for clients |

Keep this table in mind. When Glances
surprises you, the surprise has an
address, and the address is one of these
parts.
