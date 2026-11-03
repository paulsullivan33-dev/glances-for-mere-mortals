# The Web Server and the API

Outcome: Glances serving a page your
browser can open and an API your
programs can ask — on loopback, on a
port you chose — with three endpoints
answered and read. The check is a single
field fetched on its own.

## Starting it

```bash
glances -w --bind 127.0.0.1 --port 18083 --time 2
```

`-w` selects the web server;
`--bind 127.0.0.1` keeps it on this
machine only (the lab's rule, and the
right default until you have set a
password — see below); `--port` is
yours to choose. If the start fails with
a FastAPI import error, chapter 3 has
the extra package that fixes it; if it
fails with `address already in use`,
something — quite possibly an earlier
Glances of yours — already holds the
port (transcript t09 caught exactly
that, in the server's own words).

Two doors then open on the same port.
The **web page** at `http://127.0.0.1:18083/`
answers with HTTP 200 and draws the
familiar panels in the browser — the
same plugins, the same thresholds, no
terminal required. Underneath it, the
**REST API** serves the numbers as JSON.
The page is for people; the API is the
durable feature, because everything the
page knows, a program can ask for.

## The API's shape

Every address begins `/api/4/` — the 4
is the API version from `glances --version`
— followed by a plugin name:

```bash
curl -s http://127.0.0.1:18083/api/4/pluginslist
curl -s http://127.0.0.1:18083/api/4/cpu
curl -s http://127.0.0.1:18083/api/4/mem
curl -s http://127.0.0.1:18083/api/4/load
curl -s http://127.0.0.1:18083/api/4/uptime
```

```json
{"min1": 1.701171875, "min5": 1.34619140625, "min15": 1.06884765625, "cpucore": 4}
```

```json
{"total": 8319905792, "available": 983146496, "percent": 88.2,
 "used": 7336759296, "free": 158515200, ...}
```

(Transcript
`glances-lab/transcripts/t05-webserver-and-api.txt`.)
Three refinements the lab verified.
**One field only**: add the field name —
`/api/4/cpu/total` answers `{"total": 0.0}`,
a complete answer to a small question,
which is how a dashboard widget or a
health check should ask. **Everything
at once**: `/api/4/all` returns every
plugin in one document, alert history
included — convenient, and heavy; the
per-plugin doors exist so callers take
only what they need. **The event
history is data too**: `/api/4/alert`
returns the alert plugin's events as
JSON (transcript t06), so "has anything
crossed a line since I last looked?" is
a question a script can ask, not just a
footer a person can read.

Two reading cautions, both earned in
the lab. The **first processor read is
0.0** — the rate needs two samples, and
transcript t06b shows the same endpoint
answering 0.0, then 14.9, then 6.9 as
real intervals accumulate; a poller must
expect the warm-up. And list endpoints
like `/api/4/processlist` and
`/api/4/fs` return *everything*,
unabridged — the fs answer in transcript
t06 runs to fourteen mounts including
the sandbox's odd read-only images at
their honest, meaningless 100%. The API
does not summarise; summarising is the
caller's job.

## The password is part of the feature

The web server can require a login:
`--username` sets the user and Glances
prompts for the password at startup (the
project also documents password options
for the server mode of chapter 9, whose
own log prints a pointed warning when
started without one — the lab kept that
warning verbatim in transcript t08's
notes). This guide did not run an
authenticated session — its lab never
bound beyond loopback, where the
password protects against nobody — so
the authenticated flow is described from
the documentation and the warning, not
from a run. The rule stands regardless:
**a Glances port reachable by other
people gets a password and the narrowest
bind that serves the purpose**, because
the API's answers include process
command lines and network addresses,
which is a reconnaissance report on your
machine, gift-wrapped.

## The check

With the server running:

```bash
curl -s http://127.0.0.1:18083/api/4/mem/percent
```

One small JSON document with one number
in it — the machine's memory percent,
asked and answered — is the whole idea
working. Then open the same port in a
browser and confirm the page tells the
same story as the terminal did.
