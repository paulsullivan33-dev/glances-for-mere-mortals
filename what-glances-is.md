# What Glances Is

A machine slows down and the question is
never "is something wrong?" — something
is always using *something*. The question
is *what, and how much, and since when*.
The traditional Unix answer is a handful
of separate tools: one for processes, one
for memory, one for disks, one for the
network, each with its own screen and its
own habits. **Glances is the one-screen
answer.** It is a monitoring program,
written in Python, that collects the
whole machine's vital signs at once —
processor, memory, swap, load, disks,
filesystems, network, sensors where the
hardware offers them, and the list of
processes with their appetites — and
draws them together, refreshing every
couple of seconds.

The name is the idea: at a glance. But
the screen is only the first window.
Glances keeps one set of numbers and
offers several ways to look at them:

- the **terminal screen** (its default,
  drawn with curses, the terminal
  graphics library),
- **plain text, CSV or JSON** printed
  once per refresh for scripts to read,
- a **web page plus a REST API** — the
  same panels in a browser, and the raw
  numbers as JSON over HTTP for other
  programs,
- a **server mode** whose screen another
  Glances, the *client*, draws on a
  different machine,
- **exporters** that write the numbers
  away to files (and, with more setup, to
  databases and queues) so a history
  survives after the screen is closed.

That shape — one collector, many windows
— is the mental model for the whole
guide. When a number looks wrong, the
first question is which window you are
looking through, and chapter 2 names the
parts behind each one.

## A first taste

After installing (chapter 3), one word
opens the screen:

```bash
glances
```

and one flag combination asks for two
numbers as text, no screen at all:

```bash
glances --stdout cpu.total,mem.percent --time 3
```

```text
cpu.total: 26.6
mem.percent: 94.4
```

(From the lab's transcript
`glances-lab/transcripts/t01-stdout-mode.txt`;
the lab machine was a busy shared
sandbox, and its memory really was that
full.) Chapter 6 takes this mode apart.

## Watching is not recording

Glances is, by design, a witness of the
present. Its screen shows rates — how
busy things have been since the last
refresh — and it keeps a limited history
in memory (1200 samples by default,
about an hour at the default rate) for
its small graphs and its event list.
Close it, and the history is gone. That
is not a flaw; it is a scope. When the
question is "what is happening *now*, and
which process is doing it", Glances is
the right tool and answers in seconds.
When the question is "what was the disk
doing last Tuesday", you want its
exporters (chapter 10) or a real
monitoring stack (chapter 12, the
neighbours). This guide keeps the two
jobs separate and tells you which one
each chapter is doing.

## Your machine, your numbers

Glances runs locally, with no account,
and by default it sends nothing anywhere.
That default matters, because the
picture it draws is detailed: process
command lines, network addresses,
filesystem names. The moment you choose a
shape that *publishes* that picture — the
web server, the server mode, an exporter
to a remote database — you have made a
security decision, and Glances's own log
says so out loud when a server starts
without a password. This guide therefore
binds every server it starts to loopback
(the machine itself) and treats the
password options as part of the feature,
not an afterthought. Monitor your own
machines, or machines you have permission
to watch; that is the line, and it is
stated here, early, on purpose.

## Who it is for

The home-lab keeper with three small
servers and one recurring mystery. The
developer whose laptop fans spin up for
no stated reason. The administrator
handed a headless box and thirty seconds
to decide whether it is busy or stuck.
The common thread is a machine you may
watch, a question about *now*, and a
preference for one honest screen over
five partial ones.
