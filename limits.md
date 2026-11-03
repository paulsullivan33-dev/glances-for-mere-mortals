# Limits

Outcome: the edges, named before they
surprise you. Everything in this chapter
was either measured in the lab or
follows from a limit the lab ran into;
`criteria.md` keeps the receipts.

**Rates start at zero.** Every
percentage that is really a rate —
processor above all — reads 0.0 on the
first sample in every mode, because a
rate needs two snapshots. Any tool or
habit built on a single read inherits
the warm-up. Glances is a watcher; it
rewards staying, not glancing once —
despite the name.

**Panels are only as real as their
subject.** The containers plugin
reported an empty list because the
sandbox has no container runtime; the
sensors plugin has nothing to say on a
virtual machine with no hardware
sensors; cloud and connections reported
NA. On such machines those panels are
not broken, they are absent, and a
guide (this one included) can only
describe the panels it could fill.

**History is short and mortal.** 1200
samples in memory, gone at exit. The
exporters are the bridge to anything
longer, and only the two file exporters
were proven here; the database and
queue exporters exist, are documented,
and are unrun by this guide. A CSV
written every two seconds also grows
without rotation or mercy — the
recorder's housekeeping is yours.

**Silence is a failure style.** A
missing config file, an unknown field
name, an unknown exporter: in the lab,
all three were accepted without a word
on the output, the run proceeding on
defaults or partial data. Every other
monitor in your life that fails this way
teaches the same lesson — verify a new
configuration by making it produce one
visible, deliberate effect (chapter 7's
absurd threshold) before trusting it
with real lines.

**The server shapes expose what they
show.** The web and XML-RPC servers
publish process command lines, addresses
and filesystem details; the XML-RPC
server starts by default with no
authentication and says so in its log.
Loopback binding, tunnels and passwords
are not advanced topics for these modes;
they are the modes, used responsibly.
Glances also offers no fine-grained
permissions — a password admits a
watcher to everything the watcher can
see.

**One machine per watcher.** A Glances
watches the machine it runs on; the
client/server pair extends the *screen*,
not the collection, so a fleet means a
Glances per machine (or a loop of API
calls), each with its own config and
thresholds to keep honest. Aggregation,
long retention and fleet alerting belong
to the neighbours of chapter 12.

**It is a witness, not a mechanic.**
Glances will name the greedy process;
it will not slow it, renice it or kill
it from its screen (the process keys
stop at sorting and filtering). And its
numbers are psutil's reading of the
machine, at a two-second floor on the
refresh: a spike shorter than the
interval can pass between samples
unseen, and a virtual machine's numbers
describe the guest's view, not the
host's whole truth.
