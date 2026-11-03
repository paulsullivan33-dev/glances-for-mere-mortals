# Exporting History

Outcome: Glances writing its numbers to
files that outlive the screen — a CSV a
spreadsheet can open and a JSON a script
can re-read — and an honest account of
the twenty-one other exporters this
guide did not run.

## Why export at all

The screen forgets. Its history is 1200
samples in memory, and closing Glances
closes the record. An **exporter**
writes each refresh somewhere durable,
turning the witness of chapter 1 into a
recorder: what was the memory doing
during last night's backup, when did the
disk's write rate peak, is this Tuesday
spike a pattern. The export runs
*alongside* whichever interface is
showing — the lab exported while the
numbers printed nowhere at all, the
exporter being the whole point of the
run.

## The CSV exporter, run

```bash
glances --export csv \
  --export-csv-file glances-lab.csv \
  --export-csv-overwrite --time 3
```

Run for sixteen seconds at a three-second
refresh, the lab's file held a header row
and four data rows (transcript
`glances-lab/transcripts/t07-exports-csv-json.txt`;
the file's head is kept as
`glances-lab/glances-lab.csv`). The
header teaches the exporter's naming
rule at a glance:

```text
timestamp,amps.Dropbox.key,amps.Dropbox.name,...,cpu.total,...
```

Every column is `plugin.field`, flattened
with dots — the same names chapter 6
asks for by hand — and there are
*hundreds* of them, one per field of
every plugin, AMPS included. The CSV
exporter does not take a field list; it
writes everything, and selecting columns
is the reader's job downstream (a
spreadsheet, `cut`, the Miller or
VisiData guides' tools). Budget for that:
a full export is wide first and useful
second.

## The JSON exporter, run

```bash
glances --export json \
  --export-json-file glances-lab.json --time 3
```

The JSON file (kept in part as
`glances-lab/glances-lab.json`) holds the
same flattened names as keys of one
object per refresh — `{"amps": {"Dropbox.key": "name", ...}, ...}` in
the lab's build, the flattening showing
even inside the structure. It is the
shape to choose when a program will
re-read the history; the CSV is the
shape for a person with a spreadsheet.
Neither file rotates or prunes itself:
a monitor exporting every two seconds
writes forever, and the keeping of the
file — rotation, retention, disk space —
belongs to your arrangement around it,
which recipe 2 in chapter 11 turns into
a complete overnight pattern.

## The other exporters, honestly

`glances --modules-list` names 23
exporters in the lab's build: Cassandra,
ClickHouse, CouchDB, DuckDB,
Elasticsearch, Graphite, InfluxDB in
three generations, Kafka, MongoDB, MQTT,
NATS, OpenTSDB, Prometheus, RabbitMQ,
RESTful, Riemann, StatsD, TimescaleDB,
ZeroMQ — and the graph exporter, which
draws history charts as images, and the
two file exporters above. **Only csv
and json were run.** The rest share a
shape the guide can state plainly — each
needs its target service running, its
client library installed (the extras
pattern of chapter 3), and its section
in the config file — and beyond that
shape this guide claims nothing, because
the lab ran none of them and a monitoring
pipeline deserves better than a
paraphrase of its manual. The Prometheus
exporter deserves its one sentence of
direction: it makes Glances a target
Prometheus can scrape, which is the
bridge into the stack of chapter 12 —
and the Prometheus and Grafana guide in
this series is where that world is
taught properly.

## The check

Export for half a minute, then count:

```bash
wc -l glances-lab.csv
```

Rows should number the seconds divided
by your refresh, plus the header, give
or take the warm-up. Then find one value
you also saw on the screen — the memory
percent in the row nearest a moment you
remember — and confirm the file's story
is the screen's story, kept.
