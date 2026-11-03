# Reading the Numbers

Outcome: each headline number on the
screen read *honestly* — what it counts,
over what interval, and what it cannot
mean. The screen is easy to open and
easy to misread; this chapter is the
antidote, and its check is a pair of
numbers you will fetch two ways and
reconcile.

## CPU: a rate, not a reading

The processor did not spend 26.6% of
itself on anything at an instant. It
spent 26.6% of the *interval since the
last refresh* busy — counters subtracted,
divided by elapsed time. Three rules
follow:

1. **The first sample is zero.** A rate
   needs two snapshots. Every mode of
   Glances shows 0.0 processor figures on
   its very first read (the lab's API
   transcript t06b shows 0.0, then 14.9,
   then 6.9 on successive asks). A script
   that reads once and panics at 0 — or
   celebrates it — has measured the
   warm-up, not the machine.
2. **The parts are shares of the
   interval.** *User* is programs doing
   their own work; *system* is the kernel
   working on their behalf; *iowait* is
   the processor idle *because* it is
   waiting for a disk — high iowait with
   low user is a storage story, not a
   processor story; *idle* is what is
   left. In the lab's stdout run the
   split (user 17.8, system 7.3 of a 26.6
   total) says "programs busy, kernel
   helping", the ordinary shape of a
   working machine.
3. **100% means all cores, together.**
   The headline total averages every
   core. One core pegged by a
   single-threaded program on a 4-core
   machine reads as about 25% total —
   which is why the per-core view (key
   `1`, plugin `percpu`) exists, and why
   a "quiet" 30% can still be one program
   running flat out.

## Memory: used is a claim, available is the truth

Linux fills spare memory with cache and
calls it used, so two numbers matter.
Glances's MEM panel shows the
**percent** psutil reports (memory
genuinely held by programs, as a share
of the total), the byte counts, and —
in the detailed output — **available**:
what a new program could actually get.
The lab's JSON sample carries both:

```text
"mem": {"total": 8319905792, "available": 404746240,
        "percent": 95.1, "used": 7915159552, "free": 174116864, ...}
```

(Transcript t02.) Read it as: 95.1% held,
but the witness that decides "is this
machine out of memory?" is *available*
plus whether **swap** is being used —
the SWAP panel sat at 0.0% throughout the
lab, which is why a 95% memory reading
on that busy shared sandbox was a fact,
not an emergency. Swap in steady use,
not a high memory percentage, is the
classic sign of a machine that truly
needs more memory than it has.

## Load: a queue, measured against cores

The three load averages (1, 5, 15
minutes) count processes running *or
waiting to run*, averaged over time.
Their meaning is relative to the core
count Glances prints beside them
(`LOAD 4core`): a 1-minute load of 1.95
on 4 cores is a machine with headroom; the
same 1.95 on 1 core is a queue. The
thresholds agree — the config file's
load lines are *fractions of the core
count* (careful 0.7, warning 1.0), so a
load equal to the number of cores is
where concern begins, by design.
Load also lags: it is an average, so it
keeps reporting a rush for minutes after
the rush has left. In the lab's screen
the falling sequence 1.95 / 1.23 / 1.01
is a machine calming down, read
right-to-left as history.

## Disks, network, processes

**DISK I/O and NETWORK are rates too** —
bytes per second since the last refresh —
so a backup that finished between
refreshes leaves no trace on the screen
(its trace is in an export, chapter 10).
**FILE SYS is not a rate**: used and
total are facts, and their percentage is
judged against the fs thresholds. Two
cautions from the lab's own API output
(transcript t06): read-only squashfs
mounts report 100% used *by construction*
— a full read-only image is normal, not
a disk emergency — and the same real
filesystem appears once per mount point,
so totals summed across rows double
count.

**The process list** sorts by appetite
and shows each process's own CPU% (where
100% is *one* core, the opposite
convention from the headline total —
the single most common misreading of
this screen), MEM%, virtual and resident
memory (VIRT is an address-space claim;
RES is the memory actually held, and is
the column to believe), and the command.
TASKS in its header counts threads as
well as processes; "12 (52 thr)" is
twelve programs wearing fifty-two
threads, not sixty-four suspects.

## The check

Fetch the same fact through two windows
and reconcile them:

```bash
glances --stdout cpu.total,mem.percent --time 3
curl -s http://127.0.0.1:18083/api/4/cpu/total
```

(chapter 8 starts that server). Expect
agreement in story, not in decimals —
the windows sample different intervals.
Expect, too, that one of your first
reads may be the 0.0 warm-up. Knowing
*why* is the difference between reading
the numbers and merely looking at them.
