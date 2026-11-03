# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab ran on loopback with the sandbox's own processes as
   the specimen load.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: rates that read 0.0 on the first sample in every
   mode, panels that are honestly empty without the hardware
   or daemon behind them (containers, sensors), history that
   lives in memory only (1200 samples, gone at exit), a
   failure style of silence (missing config, unknown field and
   unknown exporter all accepted without a word), servers that
   expose a detailed picture of the machine and start without
   authentication by default, one watcher per machine, and a
   witness that names the greedy process but cannot act on it.
8. **The ethics rule is in the text, early.** Glances draws a
   detailed picture of a machine — process command lines,
   network addresses, filesystem names — so chapter 1 and the
   README state the line plainly and early: monitor your own
   machines, or machines you have permission to watch. Every
   server the lab started was bound to loopback, the
   unauthenticated-start warning the XML-RPC server prints is
   quoted verbatim in chapter 9, and the password and bind
   options are taught as part of the server features, not as
   advanced extras.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu 24.04 sandbox (4 cores
visible to the lab, about 8 GB of memory, heavily used by other
work while the lab ran — which is why the specimen readings are
busy ones: memory sat between 88% and 96% throughout, and the
guide says so where it quotes them). Glances **4.5.8** (API
version 4) was installed from PyPI with pip into a fresh
virtual environment, on Python 3.12.3 with psutil **7.2.2**;
the web extra (`glances[web]`) added FastAPI 0.162.0 and
Uvicorn 0.54.0. All transcripts live in
`glances-lab/transcripts/`; the terminal capture script is
`glances-lab/capture_curses.py` (it renders the curses screen
with a terminal emulator, pyte 0.8.2, because a raw capture of
a curses program is escape-code soup); the threshold config
is `glances-lab/lab-glances.conf`; the export samples are
`glances-lab/glances-lab.csv` and `glances-lab/glances-lab.json`.

Run for real, with transcripts as evidence:

- Version (Glances, API, psutil, log path), the full `--help`,
  and `--modules-list`: 35 plugins and 23 exporters, named in
  chapter 2 (t00).
- Stdout mode over nine fields at a 3-second refresh — rates,
  raw byte counts, unrounded load averages (t01); stdout CSV
  (header plus rows) and stdout JSON for the cpu and mem
  plugins (t02).
- The curses screen, driven in a real 110x38 terminal and
  rendered: header, quicklook, network/disk/filesystem
  panels, the process list sorted by appetite, and a live
  "High memory consumption" MEM event in the footer (t03).
- Configuration: the shipped sample's defaults extracted
  (cpu user 50/70/90, mem 50/70/90, load 0.7/1.0/5.0 as core
  fractions, fs 50/70/90) (t04a); a lab config with
  deliberately absurd processor lines (warning 10, critical
  20) producing a `WARNING on CPU_USER` event in eight
  seconds, alongside the memory event judged against the
  lab's lowered critical line of 85 (t04).
- The web server on loopback port 18083: first attempt
  failing on the missing FastAPI extra, with the server's
  two-line refusal kept verbatim (t05a), then after
  `glances[web]`, the API answered — pluginslist, cpu, mem,
  load, uptime, `/cpu/total` (one field alone), `/all`
  (everything, alert history included) and HTTP 200 for the
  web page itself (t05); `/alert`, `/processlist` and `/fs`
  on a second run (t06).
- The first-sample rule, isolated: repeated `/api/4/cpu`
  reads answering 0.0, then 14.9, then 6.9, with percpu and
  quicklook for contrast (t06b).
- Client/server mode on the same port: the XML-RPC server
  started (its unauthenticated/CORS warning captured from
  its log), a curses client connected, and its screen —
  header reading "Connected to ..." — rendered (t08).
- Exports: `--export csv` for 16 s produced a header of
  flattened `plugin.field` columns and four data rows;
  `--export json` produced the matching flattened JSON
  (t07, with sample files kept in the lab folder).
- Failures and switches (t09): an unknown `--stdout` field
  silently ignored; a missing `-C` config file silently
  ignored (defaults used); an unknown exporter silently
  ignored; a second web server on the same port failing
  with uvicorn's `address already in use` error; and
  `--disable-plugin network,fs,diskio` verified working
  from stdout mode.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The browser/discovery mode (`glances --browser`) and named
  server autodiscovery: the sandbox has no local network of
  Glances servers to discover.
- Threshold *actions* (commands run when a line is crossed):
  named in chapter 7 as existing, with behaviour unclaimed.
- Authenticated web and server sessions (the `--username` /
  `--password` flows): the lab bound loopback only, where a
  password protects against nobody; the server's own warning
  text is quoted verbatim instead.
- The 21 exporters other than csv and json (databases,
  queues, Prometheus, graph and the rest): each needs a
  target service the sandbox does not run. Only their shared
  shape is stated.
- The containers plugin's populated view (no container
  runtime in the sandbox; its honest empty list was seen),
  the sensors/GPU/NPU panels on real hardware, ports and
  connections panels in depth, the AMPS plugin beyond its
  appearance in exports, per-processor and light curses
  modes beyond their flags, and the new MCP server option
  visible in `--help`.
- Installs other than pip-in-a-venv (distribution packages,
  the installer script, the container image) and all
  Windows/macOS behaviour.

Fixtures are deliberately generic: the lab's specimen load is
the sandbox's own ordinary processes, every server ran on
loopback at port 18083, and no real network, organisation or
person appears in any example.
