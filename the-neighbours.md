# The Neighbours

Outcome: an honest map of the tools
beside Glances — which question each is
the best answer to — so choosing Glances
is a decision, not a default. These
tools are characterised here, not run:
the lab measured Glances, and this
chapter's judgements come from each
project's own documentation and from
what the neighbouring guides in this
series verified.

## top and htop, and the Watching Your System guide

`top` is everywhere already, and its
younger sibling `htop` adds colour,
scrolling and mouse sense. For the
narrow question "which process is eating
the processor *right now*", they are
faster to reach than Glances and ask
nothing installed beyond themselves. The
[Watching Your System](https://paulsullivan33-dev.github.io/watching-your-system-for-mere-mortals/)
guide teaches them with `ps` as a trio,
and its process craft — families,
signals, the census — is deeper than
Glances's process panel tries to be.
What they do not do is the rest of
Glances's screen (filesystems, sensors,
alerts with memory) or any of its other
shapes: no API, no exporters, no remote
client. Reach for them for a process
question on a strange machine; reach for
Glances when the question is about the
machine.

## btop

[btop](https://paulsullivan33-dev.github.io/btop-for-mere-mortals/)
draws the same whole-machine picture as
Glances's terminal screen, in a single
compiled program with no Python runtime,
a strong eye for layout, and history
graphs drawn in the terminal. If your
want is exactly the screen — prettier,
faster, self-contained — btop is the
stronger screen. What it does not have
is Glances's other doors: no REST API
serving fields to scripts, no exporter
row, no client/server pair. The honest
summary is that btop wins the window
both tools share, and Glances is the
one that is more than a window.

## Cockpit

[Cockpit](https://paulsullivan33-dev.github.io/cockpit-for-mere-mortals/)
is a web console for *administering* a
server — services, storage, accounts,
updates, a terminal — with monitoring as
one panel among many. Where Glances
watches and reports, Cockpit watches and
*acts*. A machine you must manage wants
Cockpit (or SSH and intent); a machine
you must merely understand, from a
browser, with an API underneath the
page, is Glances's shape. They coexist
without rivalry on many real servers.

## Beszel, and the history keepers

[Beszel](https://paulsullivan33-dev.github.io/beszel-for-mere-mortals/)
keeps a small hub-and-agent history of a
fleet's vital signs — the remembering
that Glances deliberately does not do.
And at the far end of that road,
[Prometheus and Grafana](https://paulsullivan33-dev.github.io/prometheus-and-grafana-for-mere-mortals/)
is the full stack: a database built for
metrics, a query language, dashboards
and alert routing. Glances's place among
them is the first five minutes and the
live question — *what is happening now,
and which process* — plus, through its
Prometheus exporter, a side door into
the stack for machines where a watcher
is already running. Nobody sensible
keeps a year of two-second samples in a
CSV; nobody sensible opens a dashboard
project to find out why the fan is loud.

## vmstat, iostat, free and the old guard

The traditional one-subject tools
(`vmstat`, `iostat`, `free`, `df`,
`ss`) remain the right witnesses in
scripts and in court: stable output
formats, decades of documentation, and
exactly one subject each, known deeply.
Chapter 5 used `free` as the second
witness for a reason. Their cost is the
assembly — the whole-machine picture is
yours to build from five readings taken
at five moments. Glances is, in one
sense, that assembly done for you, at
the price of a younger tool's habits:
output shapes that serve humans first,
and the occasional silence where an old
tool would have printed an error.
