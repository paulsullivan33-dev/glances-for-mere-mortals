# Installing Glances

Outcome: Glances installed in an
isolated Python environment, its version
reported in its own words, and — if you
want the web server — the extra package
present *before* the first time it
refuses to start. The check at the end
of the chapter is the version command;
if it prints three version lines, the
install is real.

## The shape of the install

Glances is a Python program, distributed
on **PyPI**, Python's package index. The
project's recommended install for a
single user is `pipx` (which gives the
program its own isolated environment
automatically); the lab used a plain
**virtual environment** — a private
folder holding its own Python packages,
so nothing the lab installed could
disturb the system Python or any other
project:

```bash
python3 -m venv ~/glances-venv
~/glances-venv/bin/pip install glances
```

That one command fetched Glances and its
core dependency psutil. Every command in
this guide is then run as
`~/glances-venv/bin/glances`; the guide
writes it as plain `glances` from here
on, and the transcripts show the lab's
own paths.

## The web server's extra

The plain install is enough for the
terminal screen, the stdout modes, the
file exporters and the client/server
pair. It is **not** enough for the web
server. The lab's first attempt:

```bash
glances -w --bind 127.0.0.1 --port 18083
```

stopped with two lines that are worth
reading once, slowly:

```text
FastAPI import error: No module named 'fastapi'
Glances cannot start in web server mode.
```

(Transcript `glances-lab/transcripts/t05a-webserver-missing-fastapi.txt`,
with the server's own log kept beside
it.) The web shape is an optional extra,
installed by naming it in square
brackets:

```bash
~/glances-venv/bin/pip install "glances[web]"
```

That brought in FastAPI 0.162.0 and
Uvicorn 0.54.0 in the lab, and the same
command then started and served. The
lesson generalises: Glances's optional
features — exporters to particular
databases among them — lean on optional
packages, and the ones this guide runs
are named where they are used.

## The check

```bash
glances --version
```

```text
Glances version:	4.5.8
Glances API version:	4
PsUtil version:		7.2.2
Log file:		/home/hatch/.local/share/glances/glances.log
```

Three facts to take from this output.
The **API version (4)** is the number in
every REST address in chapter 8 — it is
Glances's own API generation, not the
release number. The **psutil version**
matters because psutil is the collector:
a surprising number usually traces back
to it, not to the drawing. And the **log
file** path is where Glances writes its
own complaints; chapter 14 starts there
more than once.

Two more orientation commands, both run
in the lab and kept in transcript t00:
`glances --help` prints the full option
list (it is long — this guide introduces
options where they earn their keep), and
`glances --modules-list` prints the
plugin and exporter lists quoted in
chapter 2.

## Other ways in, honestly labelled

The project also documents a system
package on several Linux distributions,
a standalone installer script, and a
container image. None of those was run
in this lab — the sandbox has no
container runtime and the guide's rule
is to teach what it ran — so they are
named here as existing, and the pip
route above is the one the chapters
stand on. On Windows and macOS the same
pip install works, with the platform
notes in the project's documentation;
every measurement in this guide is from
Linux.
