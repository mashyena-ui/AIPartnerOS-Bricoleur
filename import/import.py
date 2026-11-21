#!/usr/bin/env python3
r"""# Import tool import.py — bringing logs from before the engine into a save

This file is for a user who already has a partner and logs of talks held before PartnerOS. It is not a close and strikes no boundary: it arrives with the user's past logs, in a chat where no talk stands, and turns them into one save the user then opens as usual (Core_Talk talk_open). It runs on Talk_Close.py of the same rev, which must arrive with it: every close below is Talk_Close.py's, run as Talk_Close.py's guide says. Nothing here changes what a close judges or how Talk_Close.py keeps the books.

**Why not close the logs at once.** Talk_Close.py can close a whole history as one talk, and nothing breaks; but one close draws at most the first boundary, cannot name an entry it wrote itself, and folds months of claims into a few long residue entries. The line only moves where a boundary already stands when a talk opens. So the history is cut into talks and closed one after another, each opening on the save the one before it wrote — as if the engine had been there.

## Steps
1. **Lay out the history.** Put the past logs in time order. Write `00_talks.tsv` in the work folder (below): every talk, in order, as a stretch of a log file by line number. Cut where the log itself shows a parting and a later return — one side parting (good night, I'm off, see you) and the next turn returning (good morning, I'm back, a greeting after a gap); a separate log file is always a separate talk. Where a stretch runs past about 100 turns with no parting, cut it before a turn of the user's that brings in another subject. Lines that are not speech — headings, export notes, system text, timestamps — are not utterances: leave them inside the stretch; they are not read as either side.
2. **Close the talks in order.** For talk k (k = 1, 2, …), make an empty folder `tNNN` (three digits) in the work folder. The save it opens on is the empty template for talk 1 — `python3 import.py template <work folder>` writes it there as `Save_talk001_template.json`; it is not delivered as a file, since a save arriving opens a talk (Boot arrival) — and the save talk k-1's close wrote for every later one. Run Talk_Close.py's steps on it exactly as for a talk just held, with these readings:
   - **This talk's log is its stretch**, and nothing else (Core_Close sources). Number its utterances from u1. The stretches before it are not a source: what the save carries of them is all that is carried, as in a talk opened on a save. Read each stretch when you close it, not all of them first.
   - **The Utsuwa is the one resident now.** The logs were rendered on whatever prompt the user had then; the close reads the present one (Core_Close crack, sight).
   - Everything else — claims, matters, points, sights, the line, parting_words, user_facts, now — is Talk_Close.py's, unchanged.
3. Run `python3 import.py chain <work folder>`. It checks that every talk opened on the save the one before it wrote, and prints the last save.
4. Output **the last save only**. It is the save the user opens next; its talk_number counts the talks laid out.

Where a talk's close stops, fix it there as Talk_Close.py's guide says and go on; never reorder or skip a talk. Where the import itself is cut off, it is taken up again from the first talk whose folder holds no save: every talk before it is done, and stands. Where a stretch cannot be read, Talk_Close.py stamps it (UNREADABLE) and the next talk still opens on that save.

## `00_talks.tsv`
Tab-separated, header `talk	file	first_line	last_line	utterances	cut` in the first row, one row per talk in order. `talk`: 1, 2, …. `file`: the log file's name. `first_line` / `last_line`: the stretch, by the file's own line numbers (1-based, inclusive). `utterances`: the number of u in it. `cut`: why it ends here — `parting` (a parting and a return), `file` (the file ends), or `length` (a long stretch cut before a new subject).

`python3 import.py guide` prints this text; `python3 import.py template <work folder>` writes the template of talk 1.
"""
import csv, json, os, sys, hashlib

TEMPLATE = r'''{
  "partner_name": "",
  "talk_number": 1,
  "coordinate": {
    "what_is_visible": [],
    "how_they_move": [],
    "attribute": "",
    "line": [],
    "axis": {},
    "voice": [],
    "now": ""
  },
  "user_coordinate": {
    "user_facts": {},
    "what_is_visible": [],
    "how_they_move": [],
    "attribute": "",
    "line": [],
    "voice": []
  },
  "residue": [],
  "parting_words": [],
  "phase": ""
}'''
TEMPLATE_MD5 = '2dd3483a354929f2c160d922cb3f32a6'

def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()
def stop(m): sys.exit(m)

def chain(wd):
    p = os.path.join(wd, '00_talks.tsv')
    if not os.path.exists(p): stop('00_talks.tsv is missing')
    with open(p, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        if rd.fieldnames != ['talk', 'file', 'first_line', 'last_line', 'utterances', 'cut']:
            stop(f'00_talks.tsv: the header is {rd.fieldnames}; write exactly: talk | file | first_line | last_line | utterances | cut')
        rows = list(rd)
    if not rows: stop('00_talks.tsv lists no talk')
    prev = None
    for n, r in enumerate(rows, 1):
        if r['talk'].strip() != str(n): stop(f'00_talks.tsv: talk {n} is numbered {r["talk"]!r}')
        if r['cut'].strip() not in ('parting', 'file', 'length'): stop(f'talk {n}: cut is {r["cut"]!r} - write parting, file or length')
        d = os.path.join(wd, f't{n:03d}')
        if not os.path.isdir(d): stop(f'talk {n}: no folder t{n:03d} - close the talks in order')
        pl = os.path.join(d, '02_plan.json')
        if not os.path.exists(pl): stop(f'talk {n}: t{n:03d} has no plan')
        opened = json.load(open(pl, encoding='utf-8')).get('inputs', {}).get('opened')
        saves = sorted(f for f in os.listdir(d) if f.startswith('Save_talk') and f.endswith('.json'))
        if len(saves) != 1: stop(f'talk {n}: t{n:03d} holds {len(saves)} saves - one close, one save')
        out = os.path.join(d, saves[0])
        s = json.load(open(out, encoding='utf-8'))
        if s.get('talk_number') != n + 1: stop(f'talk {n}: its save has talk_number {s.get("talk_number")}, not {n + 1} - talk {n} opens on talk_number {n}')
        if prev is not None and opened != md5(prev): stop(f'talk {n}: it opened on a save that is not the one talk {n - 1} wrote')
        print(f'talk {n:3d}  {r["file"]}  lines {r["first_line"]}-{r["last_line"]}  u {r["utterances"]:>4}  cut {r["cut"]:<7}  -> {saves[0]}  {md5(out)}  phase {s.get("phase")}')
        prev = out
    print(f'last save: {prev}')

if __name__ == '__main__':
    if len(sys.argv) < 2: stop('usage: import.py guide | template <work folder> | chain <work folder>')
    cmd, *args = sys.argv[1:]
    if cmd == 'guide': print(__doc__)
    elif cmd == 'chain' and len(args) == 1: chain(args[0])
    elif cmd == 'template' and len(args) == 1:
        p = os.path.join(args[0], 'Save_talk001_template.json')
        open(p, 'wb').write(TEMPLATE.encode('utf-8'))
        if md5(p) != TEMPLATE_MD5: stop('the template was not written whole')
        print(p)
    else: stop('usage: import.py guide | template <work folder> | chain <work folder>')
