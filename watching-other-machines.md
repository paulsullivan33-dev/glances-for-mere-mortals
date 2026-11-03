# Watching Other Machines

Outcome: a Glances screen on *this*
machine showing *another* machine's
numbers, with the header line proving
whose numbers they are. This is the
chapter for the headless box in the
cupboard.

## Server and client

Glances's remote mode is a pair. On the
machine to be watched:

```bash
glances -s --bind 127.0.0.1 --port 18083 --time 2
```

`-s` runs the **server**: it collects
exactly as usual, but instead of drawing,
it answers an XML-RPC service (a
long-standing remote-procedure protocol;
chapter 2 flagged that this is *not* the
REST API — the browser page of chapter 9
and this service share nothing but the
numbers). On your own machine:

```bash
glances -c 127.0.0.1 --port 18083 --time 2
```

`-c` runs the **client**: the familiar
curses screen, fed by the server. The
lab ran both ends on loopback (its only
permitted network) and the client's
screen is transcript
`glances-lab/transcripts/t08-client-server-screen.txt`.
Its first line is the receipt:

```text
Connected to htch-runtime Ubuntu 24.04 64bit / Linux 7.0.0-39-generic   Uptime: 0:52:51
```

"Connected to" plus the remote system's
name and uptime — when a screen might be
showing either of two machines, that
line is how you know which. Everything
below it behaves as chapter 4 taught:
same panels, same thresholds — judged,
note, by the **server's** config file,
because the server is where the numbers
and their opinions live; the client is a
window, and its own thresholds stay
home.

## The warning the server prints

The lab kept the server's own log
because it teaches the security shape
better than a paraphrase:

```text
Glances XML-RPC server is running on 127.0.0.1:18083
WARNING: XML-RPC server is running without authentication and with CORS Allow-Origin: *.
         Mitigations: set a password (-P/--password) and/or restrict
         cors_origins in glances.conf [outputs] section.
WARNING: Glances XML-RPC server is running without Host header validation.
```

Three facts in the tool's own words: no
authentication by default, a permissive
cross-origin setting, and a named
mitigation. On a real network the
password is not optional decoration:
start the server with `--password` (it
prompts, or takes the password options
the help lists) and the client with the
matching `--password`, bind to the
narrowest address that reaches the
machines you intend, and remember what
the screen shows a holder of that
password — every process and its command
line. The lab's loopback run needed
nobody's password because it had
nobody's network; yours will differ, and
the log has already told you so.

## Finding servers, labelled honestly

Glances also documents a **browser**
(not a web browser — a server browser):
`glances --browser` lists Glances
servers it discovers on the local
network by autodiscovery and lets you
pick one, and servers can announce
themselves under names. The lab did not
run discovery — its sandbox offers no
local network of Glances servers to
discover, and a list of one loopback
server would prove little — so the
browser is described here from the
documentation, and the client/server
pair above is the part this guide
stands on. If your fleet grows to the
point where typing addresses is the
chore, the discovery mode is the
project's answer and chapter 12 places
it among the neighbours' concerns.

## When to use which remote shape

Chapter 8's web server and this
chapter's server mode solve different
problems. The **web/API** shape suits
dashboards, scripts and anything that
speaks HTTP and JSON; the viewer needs
nothing installed. The **client/server**
shape suits a person at a terminal who
wants the full curses screen — keys,
sorting, event footer and all — for a
machine with no screen of its own, and
both ends need Glances installed. The
lab ran both, on the same port in turn,
and the ports are interchangeable
because the shapes are alternatives, not
layers.

## The check

Start a server, connect a client, and
compare the client's header line and
uptime against the server machine's own
`hostname` and `uptime`. They must agree.
Then stop the server (Ctrl-C where it
runs) and watch the client notice —
a remote screen whose server has gone
is a fact you want to have seen once in
practice, not first in earnest.
