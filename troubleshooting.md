# Troubleshooting

Outcome: the failures this guide's lab
actually met, in the order a reader is
likely to meet them, each with the check
that separates it from its lookalikes.

## "Glances cannot start in web server mode"

The full message begins `FastAPI import
error: No module named 'fastapi'`. The
web server is an optional extra and the
plain install does not carry it. Fix:
install `"glances[web]"` into the same
environment (chapter 3), then start
again. The check that you fixed the
right thing: the same command now serves
`curl -s http://127.0.0.1:18083/api/4/pluginslist`
with a JSON list. Other optional shapes
fail in this family resemblance — a
missing client library behind an
exporter — and Glances's log file (its
path is printed by `glances --version`)
is where the import error is written
down.

## "Address already in use" on the port

The web server's log says, verbatim in
the lab's catch, `[Errno 98] error while
attempting to bind on address ('127.0.0.1', 18083):
address already in use`. Something
holds the port — most often an earlier
Glances you started in another terminal
and forgot, which is precisely how the
lab produced it. Find the holder
(`ss -tlnp` or the lsof guide's craft),
stop it or choose another port, and
remember that the failed second instance
still exits politely; a script that
checks only the exit code will believe
a server started that did not. Check by
asking the API, not by trusting the
launch.

## The config change that does nothing

Three suspects, in the lab's order of
likelihood. The path is wrong: a missing
`-C` file is **silently** ignored and
defaults rule (transcript t09), so prove
the file is read by changing `refresh`
and watching the screen's tempo. The
section or key is misspelled: INI files
forgive nothing, and a `[mem]` line
typed under `[cpu]` judges a value you
did not mean to move. The line is right
but the value never crosses it: a
warning at 70 on a machine whose normal
is 88 is not a broken threshold, it is a
permanent event — chapter 7's tuning
discussion is the fix.

## A field that never appears

In `--stdout` and `--stdout-csv`, an
unknown field is silently dropped
(transcript t09: `nonsense.field` came
and went without a whisper). Ask for the
whole plugin once with `--stdout-json`
and copy the key's spelling from the
answer. The same habit protects API
callers: fetch `/api/4/<plugin>` whole
before depending on one field's name.

## CPU reads 0.0

Almost certainly the warm-up of chapter
5: the first sample in every mode has
no predecessor to subtract. Ask again
after two refreshes (transcript t06b:
0.0, then 14.9, then 6.9). If processor
figures stay at zero across many samples
while the machine is plainly busy, the
suspicion moves to the collector —
check the process list's own CPU% column
and the psutil version in
`glances --version`, and run
`glances --issue`, which exercises every
plugin and prints a per-plugin report
(the lab ran it while orienting, and its
alert section showed a live MEM event).

## The screen is missing panels, or shows NA

Width first: Glances drops panels on a
narrow terminal rather than truncating
them, so widen the window before
diagnosing an absence. Then the plugin's
subject: NA and empty panels on virtual
or containerless machines are the plugin
telling the truth (chapter 13). A panel
you disabled in a config or with
`--disable-plugin` on an earlier run
stays a choice, not a symptom — check
the command you actually ran.

## The client shows the wrong machine, or nothing

The client's header line begins
"Connected to" and names the system it
is watching; read it before reading any
number (chapter 9). A client that
cannot connect wants the server checked
first — is `glances -s` running, on the
port and bind you think, with a password
the client also has — in that order.
And a client connected to a server whose
thresholds surprise you is reading
another machine's opinions: thresholds
live with the server, by design.

## The trap this lab fell into, kept as a warning

Starting servers in background shells
and stopping them by name-matching is
how a lab kills its own shell: a
`pkill` pattern matched the command line
of the very script that ran it. Keep the
PID when you start a server (`$!` in
shell), stop it by that PID, and confirm
the port is free afterwards. The lab's
transcripts are cleaner for the lesson,
and chapters 8 and 9's servers were all stopped
by number before the chapter was
written.
