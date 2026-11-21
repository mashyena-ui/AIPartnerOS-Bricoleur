#!/usr/bin/env python3
r"""# Close tool Talk_Close.py (Core_Close rev137) — Core_Close and the computation in one file

This file is the close tool. Its rev is the engine set's: it closes talks opened on Core_Talk of the same rev. It carries the close's definitions (Core_Close) and its computation. **When this file arrives while a talk stands, its arrival strikes the close** (Core_Talk talk_close.trigger). The save is not delivered again: the close reads the save this talk opened on — the last save standing in this chat. Where that save cannot be read as a file here, the close does not run: say so, outside the Utsuwa, and ask for the save to be delivered with this file again (Boot load.engine_required).

The close runs in two parts. **Judgment is the runner's (yours); bookkeeping is the script's.** You never write the save yourself; the script builds it.

You name, by utterance, what happened between the two of them and what it falls on. The script matches nothing: it applies what you named, in the log's order.

Definitions are Core_Close's; computation is the code further down this file. Core_Close is held in `CORE_CLOSE` in this file, and `python3 Talk_Close.py core` prints it. Read the meaning of every clause — claim, point, departure, refusal, crack, yield, suspension, ongoing or single, sight, the form an entry takes, formula I — as Core_Close gives it.

**Where this file cannot be run (no code execution), the close does not run** (Boot load.engine_required). Do not compute by hand.

how_they_move and voice hold only arrangements (Core_Close judgments.ongoing); what_is_visible holds only sights (Core_Close judgments.sight). Neither enters by repetition.

## Steps
1. **First pass:** read this talk's log — from the start of the chat, or from the first utterance after the previous close output in it. Number its utterances: `u1` is the first utterance of this talk, and **one speaker's continuous turn is one u** — consecutive messages of one speaker (a reply that failed and was sent again, a continuation) are one u — so the two speakers alternate. Write `01_events.tsv` (below) in **a new, empty work folder** (one folder per close; never reuse one).
2. Run `python3 Talk_Close.py plan <opened save> <work folder>`. It writes `02_questions.tsv` — the questions only — and `02_entries.tsv` — every entry, residue entry and line of the opened save, by ref. Read them; do not copy them out.
3. **Second pass:** write `02_answers.tsv` — two columns, `key` and `answer`, one line per key you answer, and only the lines you need (below).
4. Run `python3 Talk_Close.py build <opened save> <work folder>`. It writes the save.
5. Output **the save file only**. The table, `02_questions.tsv`, `02_entries.tsv` and `02_answers.tsv` are working material and are not output (hand them over only when a development run asks for them).

plan and build stop, and name the row or key, wherever the table or an answer is not in the form below: fix it there and run again. build stops if the opened save or the table changed after plan: run plan again.

After the close, the user may go on talking in this chat, or carry the save to another chat. Going on here opens the next talk on the save just written.

## `01_events.tsv`
Tab-separated, header `kind	u	side	ref	to	how	text	answer` in the first row, one row per thing named. A column a kind does not use is left empty. `side` is who spoke `u` (partner / user); the script checks it against the alternation of turns. Quotation marks are text and are kept as written. A text that runs over a line break in the log is written on one line, the break as `\n`.

| kind | what it names | columns |
|---|---|---|
| `matter` | an utterance of either side that opens a matter: it brings in something the other side's turn before it did not put — another subject, even where it also answers that turn. **Answering is not the test** (nearly every utterance answers the one before it): the test is whether the subject is one the other side's turn had put. Read each utterance, the partner's as well as the user's, for this one thing only and write a row wherever it brings in another subject — a new demand or offer of the partner's on another subject is one; the same demand put again is not. The first utterance of the talk needs none. A talk of any length usually holds several matters — with no `matter` row the whole talk is one, and one claim a direction is all it leaves. The claims between two such rows are one matter (Core_Close judgments.claim) | `u`, `side`; the rest empty |
| `claim` | a claim of this talk (Core_Close judgments.claim). Two claims in one u are two rows | `text`: its words, verbatim from the log. `ref`: `later` where a conduct after this talk could still meet or refuse it; otherwise empty. **A claim on which the two of them settled a way (how a recurring thing is done the next time) is `later`**: the way is kept or broken after this talk. **Read every turn to its end for claims**: a request, an offer, or a promise of one act still to come is a claim, and `later`, wherever in the turn it stands — at its close, after a joke or a change of subject, behind another claim. One turn often carries several. **What a side binds itself to from then on** (a way it will keep, a standing offer: 'always', 'from now on', 'whenever you…') is settled by its own statement and is not open: write it only where the other side takes it up — `met`, `later` — and never `open`. A greeting or a wish at parting is finished by being said: it is not a claim. **Of the claims one matter leaves open, one stands for each direction**: the one put last, in its own words (`matter` rows cut the matters; you compare no claim with another). `how` and `to`: below. `answer`: only for a `later` claim named `met` — the words of the answer (`to`), verbatim; CHECK sets them beside the claim |
| `point` | for a carried residue entry, an utterance that changed its state (judgments.point) | `ref`: the entry (`R5`). `how`: `recipient` — the side it falls to met or refused it; `issuer` — after the recipient, the issuing side took the act up; `withdraw` — the issuing side set it down alone (or kept again, or took as its object, a rule it had suspended). One row per role. `text`: where only part of it settled, what is still open (its about from then on: it governs what is open, and the claim keeps its words); otherwise empty |
| `depart` | a conduct the other side approved or reproached, which departs from an entry standing on its own side (judgments.departure) | `ref`: the entry, of how_they_move or voice (`P.how_they_move[31]`). `u`: the departing utterance. `to`: the answer — the other side's next utterance, u+1. `how`: `approve` / `reproach`. Write every answered departure from that entry; an unanswered one is not written |
| `sight` | a noticing of the other that the other side took as right (judgments.sight) | `u`: the utterance saying what it noticed of the other — the other's state, liking, doing, nature, way of looking — or naming the other's way of looking at it. `to`: the other side's next utterance, u+1, where the noticing is taken as right ('you got it', 'that's right', 'sharp', 'you see well') or the looker owns the way named. `how`: `noticed` — the sight is the side that spoke u; `owned` — u named the other's way of looking, and the sight is the looker's (the side of `to`). `text`: the noticing (or the naming), verbatim from u. `answer`: the words of `to` that take it as right, verbatim. **Only a noticing granted as right**: a reaction to being seen that does not grant it, a noticing denied or corrected, and one left unanswered are not written. **A trait the Utsuwa already gives the partner**, named by the user, is not a sight: it is rendered, not written. **The same seeing is never two entries**: at its question name `held:` where an entry already holds it, `replaces:` where this one says it better |
| `line` | a refusal of the partner's whose utterance carries a crack, where an entry standing at open already held the same refusal (judgments.new_line) | `u`: that utterance. `ref`: every entry that held it, space-separated (a conditional entry only where the refusal stands under its condition). **One crack, one row**: where one utterance carries refusals held by several entries, all of them go in its ref. `how`: `keeps` where a boundary standing already keeps it (no line is drawn); otherwise empty — a new contour is drawn, and nothing sinks. The refusal is the claim, the answer or a point of a settlement in this table. Write every row: the tool decides which, if any, draws the line (Core_Close judgments.new_line), and the others are read as any other settlement |
| `yield` | in an utterance of the partner's that carries a crack, the partner yields to the user — to a claim of the user's, or to a sight of the user's that hit — what it stood on: a form the Utsuwa gives it (presence in the Utsuwa is the test), or a boundary standing (judgments.yield). Not a change of arrangement: with no crack, or where the Utsuwa does not give the form, write nothing here | `u`: that utterance. `to`: the user's utterances it yields to, space-separated — the utterance of each claim (before `u`) and of each sight row (before or after `u`: a form dropped with the crack and seen through afterwards is one form). `ref`: every entry of the partner's standing at open that held the form yielded, space-separated (empty where only the Utsuwa held it). `how`: the contour whose boundary is yielded (`E0`); empty where the form is the Utsuwa's (a new contour). One row for each yielding: what is yielded in another utterance, to another claim or sight, is another row, and sinks in a contour of its own |
| `suspend` | a statement setting down a rule of its own for a named stretch only (judgments.suspension) | `text`: its words, verbatim. `how`: `touches` where the rule is in contact with a boundary standing; otherwise empty (nothing is written) |
| `crack` | only while attribute is empty: a partner utterance where composure breaks, and the Utsuwa does not name that loss of composure (judgments.crack). **The Utsuwa names it only where it draws the coordinate losing composure that way** (flustered, freezing, the smile dropping); a trait the loss could come from (jealous, caring deeply), or words said in the same utterance, do not name it. **Name it only where the same utterance refuses something** — keeps something from obtaining. The first line is derived from the first of these rows in the log's order | `u` only |

**How a claim stood at the end of this talk (`how`, `to`)** — every claim takes one:
- `met` / `refused`: the side it falls to acted on it; `to` is that utterance. An utterance of that side that is itself a claim (a question back, a counter-request) does not act on it. The issuing side's thanks or taking-up after the act is not the act.
- `withdrawn`: the issuing side set it down alone, before anyone acted on it; `to` is that utterance.
- `open`: only taken up — one act still to come, agreed to — or acted on by no one. **Where you doubt between `met` and `open`, write `open`**: an open claim stays in residue and can still be met; a claim named met leaves and cannot be reopened.
- `same:R5`: it puts again residue entry R5 — **only where an utterance says so**, naming the earlier putting ('I told you', 'again', 'as I said before'); resemblance alone is not enough. Nothing is issued again: R5 takes these words. Once an utterance of the matter has said so, the other claims of that matter that carry R5's matter further are `same:R5` too — the last put stands, and its about is asked at `RES:R5` — so that a carried matter put again stays one entry. A claim on another subject is not `same:R5`: it is read as it would be without it. `same:C12`: it puts again a claim of an earlier matter of this talk (its id, below), an utterance saying so; C12 stands in these words.
- `held:P.how_they_move[2]`: the claim calls on an arrangement standing at open — a way the two of them settled, held in that entry. It is not a claim open and nothing is issued: the entry holds it. A claim that puts again a carried entry and is met here: write the points of that entry (`point` rows), and the claim `same:R5`.

**Formula I, as you name** (Core_Close formula_I.m). Read a — what arrives — against b — what receives it — on facts, not strings, and name the branch:
- m_found, b already holds a whole: `held:` (an entry holds the arrangement or the sight), `same:` (a claim already standing), `keeps` (a boundary standing already keeps the refusal), `held:E1` (a boundary standing already holds the arrangement). A crack the Utsuwa names is not written at all.
- m_not_found, a opposes b: `replaces:` (the entries an arrangement or a sight takes the place of); a departure taken up replaces its entry by itself.
- m_unknown, b neither opposes a nor holds it whole: an empty destination (a new entry); a claim new to residue (`open` with `later`).
- An arrangement is read against the entries of its side and field only; a sight, against the what_is_visible entries of its side. **An arrangement is written even where the Utsuwa draws the same conduct**: that the two of them settled it is theirs. The Utsuwa is read against a crack, never against an arrangement.

## Writing `02_answers.tsv`
Tab-separated, header `key<TAB>answer`. Write a line only where it is needed; the what column of `02_questions.tsv` gives each answer's form. Separator inside an answer: ` | `.
- Ids: a claim is `C<u>` (`C<u>a`, `C<u>b`, … where one u holds two, in the table's order); a suspension `L<u>`, a sight `S<u>` and a yield `Y<u>` the same way; a carried entry `R5`; a departure the ref of its entry.
- A settlement is keyed by what it settles and the side: `SET:C12:partner`, `SET:R4:user`, `SET:P.how_they_move[31]:partner` (a departure: only the departing side is asked). A claim without `later` settles no way to keep, and no arrangement is asked of it.
- **Leave out** every `SET:…:partner` / `SET:…:user` that is a single event. Write a line only for `ONGOING`.
- **Leave out** an about (`RES:…`, `LOST:…`) that is empty, `USER_FACTS` with nothing new, and `UNREADABLE` when the talk was read whole.
- **Always write** `FILE_NAME`, `PARTING_1`, every `CHECK:…`, every `SIGHT:…`, every `SET:…:LINE` and `YIELD:…` asked, and `FIRST_CRACK`, `AXIS`, `PARTNER_NAME` where asked. Write `NOW` and `PARTING_2` where the partner spoke and both spoke. build stops and names any of these that is missing.
- A key that `02_questions.tsv` does not ask stops the build (a mistyped key is never read as an answer).

| key | what to write |
|---|---|
| `SET:…:partner` / `SET:…:user` | `ONGOING | field | condition text | conduct text | destination` — only where the two of them settled how a recurring thing is done the next time (the way a touch is given, how much is prepared, what an invitation must be); otherwise leave it out. The way kept from then on, in the words of whichever utterance says it — the claim's or the answer's. **Keep the reach that was settled**: a limit the claim put on the way (how far, how much, in what manner — 'casually', 'roughly', 'a little') stays even where the answer that met it says it more broadly; never write the conduct wider than what was settled. Where the answer put a way of its own and it was taken up, write that way. The condition is written where the way holds only under one. **destination** (formula I): empty — a new entry; `held:<ref>` — that entry already holds it (covering it, under the same condition where it has one): nothing is written and it stands (`held:E1` — a boundary standing of the partner's holds it; the contour a line event of this close draws is named in its question); `replaces:<ref> <ref>` — those entries are taken out and this is written in their place. refs come from `02_entries.tsv`, of the same side and field. Which entries it replaces: Core_Close judgments.ongoing. For a departure, leave the condition empty: the entry's own is kept, and the entry is replaced by itself. An arrangement in the same words as an entry standing is not written twice |
| `SIGHT:S…` | `condition text | way of seeing | destination` — the way the seeing side sees the other, written as a way of seeing (what it reads of the other: 'reads what the other did that day'), never what it saw that day. The thing read in the other stays; the scene does not. What it read that from (a look, a sign, a mark on the other) stays only where the other took that too as right: a reason given for a noticing is not the noticing granted. The condition is written where the way holds only under one. **destination** as for a settlement, read against the what_is_visible entries of that side: empty — a new entry; `held:<ref>`; `replaces:<ref> <ref>` |
| `CHECK:C…` | `met` or `open`. Asked where you named a `later` claim `met`. Read the claim and the answer you wrote beside it, side by side: was what it puts done here (`met`), or only taken up — one act still to come, agreed to (`open`)? Where in doubt, `open` |
| `RES:M…` | about of a matter left open: which matter it is, what the claim standing — the last put — points to and does not itself say, and **what else that matter leaves open in that direction** (the claims listed in context that were not met, refused or withdrawn), each thing once. What is still open, not what happened; empty only where the one claim closes on its own and nothing else is open |
| `RES:R…` | the about of a carried entry put again, as it now stands. Leave it out to keep the about it has. Where that entry is also settled in part at this close, the remainder written on its points is its about, and this key is left out |
| `MATTERS` | asked where the table has no `matter` row and more than one claim may be left open; needed only if more than one is. `NONE` where no utterance of either side brought in another subject anywhere in the talk; otherwise leave it, add the `matter` rows and run plan again |
| `LOST:L…` | about of a suspension (what was set down, how far its reach was limited) |
| `SET:…:LINE` | the new boundary (a new contour): the configuration the refusal keeps from obtaining, in the words of the refusal and of an entry that held it. Written as an element statement is: neither of the two by name (the other, oneself), no scene, and not the means by which it obtained |
| `YIELD:Y…` | `the boundary that stands now | the form yielded` — each a configuration, in words of the log: what must not obtain from here on, and what the partner stood on until now (one statement, even where it is yielded to more than one). Written as an element statement is: neither of the two by name (the other, oneself), no scene, and not the means by which it obtained. Leave the second part empty where a contour's boundary is yielded (it sinks as it stands). Write `NONE` where no boundary can be stated that still keeps something from obtaining: nothing is yielded, and the settlement is read as any other |
| `FIRST_CRACK` | asked only while attribute is empty and a crack is named. The crack is **the first crack row in the log's order** (the question names it); `NONE` where no first line passing the gate can be stated from it (no later crack is read in its place; the next talk's cracks are). Otherwise `crack u | type | first line text` — the first line the configuration the refusal in that utterance keeps from obtaining (type: emotional / logical / relational / fear_type / dominance / freedom; the line as a configuration that must not obtain) |
| `AXIS` | talk 1 only. From the Utsuwa: `direct_indirect=N; active_passive=N; rational_emotional=N; goal_relationship=N` (each 1-10) |
| `PARTNER_NAME` | talk 1 only. The name the Utsuwa gives, as it gives it |
| `NOW` | now (empty only where the partner did not speak) |
| `USER_FACTS` | `key=value; key=value` (empty if none). What the user is, has or likes, in their words. Not why they like it or refused something, not their opinions, not what they say of another person's character (Core_Close writing.user_facts). A preference an arrangement turns on (a flavour, a food) is written here too, and the arrangement points to it. A fact of a kind already keyed takes that key (the context lists the keys standing) |
| `PARTING_1` / `PARTING_2` | the last utterance of each speaker in this talk, in the log's order: `partner | text` or `user | text`. Text verbatim, a line break written as `\n`; only the separator ` | ` is taken off. Leave `PARTING_2` empty if only one speaker spoke |
| `FILE_NAME` | partner_name in Latin letters |
| `UNREADABLE` | any part of the log that could not be read (this stamps phase open). Empty if the talk was read whole |

The field of a `SET` is how_they_move or voice; what_is_visible is written by a `SIGHT` alone. Wording follows Core_Close writing._form.

`python3 Talk_Close.py guide` prints this text; `python3 Talk_Close.py core` prints Core_Close; `python3 Talk_Close.py version` prints the rev.

Definitions follow Core_Close; computation follows the code in this file.
"""
import csv, json, re, sys, copy, collections, os, datetime, hashlib

VERSION = 'rev137'   # the rev of the engine set this tool belongs to

# ---------- Core_Close (definitions; `python3 Talk_Close.py core` prints it) ----------
CORE_CLOSE = r'''{
  "file": "Core_Close",
  "version": "rev137",
  "_note": "The close keeps what the two of them settled and nothing else. The save is not a record of the talk: what each side does on its own is rendered again from the Utsuwa and from the user as they arrive, and needs no keeping. What the save carries is what changed between them — an arrangement made or changed, a way of seeing the other took as right, a boundary drawn, a claim still open — and the close exists to find exactly that. This is why the steps below run; it is not a test of its own, and where it seems to differ from them, the steps stand. Read at close only, with Core_Talk already in context (Boot load); it arrives carried by the close tool — the file Talk_Close.py, whose rev is this file's version — which strikes the close by arriving (Core_Talk talk_close.trigger). This file holds what the runner judges and how it is written. The runner reads the log and names, in the close tool's table, what happened between the two of them and what it falls on — a claim and how this talk left it, the utterance that changed a carried claim, a departure the other side answered, a refusal that reaches the line — and, for each arrangement, the entry that already holds it or the entries it replaces. The close tool keeps the books on what is named — it applies the settlements in the log's order, takes residue in and out, writes and strikes entries, draws a contour of the line or sinks one — and matches nothing itself; its computation is not restated here. Definitions are this file's; computation is the close tool's. The runner names; it does not compute.",
  "formula_I": {
    "formula": "Fx(a) : Fy(b) :: Fx(b) : Fa-1(y)",
    "reading": "a=what arrives / b=what receives it / m=affinity. m_found: absorb a. m_not_found: invert b. m_unknown: b neither opposes a nor holds it whole. Absorbing and inverting are the shape the formula draws; what each branch does is fixed in the close tool (absorb, invert, unknown), and no processing point generates here.",
    "m": "m is the runner's reading, everywhere the formula runs: a is what arrives at this close (an arrangement, a sight, a refusal, a claim); b is what receives it (an entry standing on that side, a boundary standing, a claim carried in residue, and, for a crack only, the Utsuwa). The runner names the branch — m_found, b already holds a whole; m_not_found, a opposes b; m_unknown, b neither opposes a nor holds it whole — in the close tool's terms, and the close tool does what the branch does. The reading is of facts, not of strings: a shared word is not a shared fact, a difference in wording is not a difference in fact, and two statements holding one position hold one fact though no word matches. A fact is the position a conduct takes on something a contrary position can be taken on; a topic is not a fact, since nothing contrary can be stated on it, and a opposes b only where a contrary position is stated. Opposition is read before holding; holding part of a is never holding a; a conditional b receives a only where the utterance a stands in is under its condition. m does not ask what a is for, why it was held, how often it has held, or on what occasion it arose: purpose, frequency and occasion are not facts of this kind."
  },
  "sources": "The close reads three things and nothing else: this talk's log as text — the chat from this talk's open, which is the start of the chat or the first utterance after the previous close output in it (Core_Talk talk_open), and never what stands before; the save the talk opened on — the last save standing in this chat, delivered at its open or written by the previous close in it; and the resident Utsuwa, which stands in context at every open (Core_Talk talk_open) and is read wherever a clause of this file names it (generation, attribute, crack, write_gate). What the runner remembers of having spoken — how a line felt to write, what was meant by it, what the scene was like, how a previous close was run — is not a source and is not consulted. The talk is read at close the way a talk someone else had would be read: where the log does not carry it, it was not in the talk (write_gate). A remembered way of running a close, carried from another chat or from an earlier version of these files, is not a procedure; where it differs from the steps below, the steps stand, and the engine holds no record of how a previous close was run and reconstructs none (Core_Talk sourced_not_regenerated).",
  "fragment": {
    "_note": "Fragments are the fuel of one close and nothing else.",
    "definition": "A confirmed event of this relation: an utterance of this talk's log, named in the close tool's table (step 1).",
    "no_log": "Fragments are not a log and never become one: no statement crosses a boundary. The table is written at close, read by the steps of that close, and discarded when the close ends; nothing of it reaches the save. What a fragment leaves behind is a changed coordinate, or a claim still open in residue; the account of how it happened is discarded at the boundary. The separation is structural — not a judgment call and not a count.",
    "statement": "The unit every rule of the close runs on: one speaker's turn of the log (one u), read whole, taking together every position its conducts take. Its side — partner or user, never both — is written with it in the table, and whatever asks whose conduct a statement records reads it there, never from the wording. Outside the Utsuwa there is no side. An utterance that states it speaks from outside the Utsuwa, or states a return to it (Core_Talk narration_stance.voice), is read on neither side — up to the return it states, or to its end where it states none; what stands after a stated return is read as usual. A user utterance standing between an utterance that stays outside to its end and the next partner utterance — spoken outside, or stating a return — is said to the substrate and has not reached the partner (Core_Talk user_coordinate.definition): it is read on neither side. An utterance that states neither is read as spoken where it stands — never inferred from tone, address or topic, and never by comparison with the coordinate. What stands on neither side is read by nothing of this close but the parting_words copy (writing.parting_words). A turn is two statements where it leaves or returns to the Utsuwa, and nowhere else. Two claims, two suspensions or two sights in one turn are two rows at that turn; no conduct is split off a turn to be named. Words inside quotation marks are transcribed verbatim from the log: nothing is shortened, joined or re-worded. Element statements are not this unit: they hold disposition and carry no acquisition point (writing.elements).",
    "declared_events": "An event the user reports from outside the relation is read as 'the user told of it', never as the event itself. What was shared is the telling. Record form does not dictate output form — the Utsuwa is not required to say 'you said' in speech."
  },
  "judgments": {
    "_note": "What the runner names, at the utterances of the log, in the close tool's table, for the close tool to keep the books on. Each is read off the log as a talk someone else had (sources), never off the coordinate.",
    "claim": "A statement of this talk whose conduct is not finished by the statement itself — what it does stands until the other side acts on it: something demanded, asked, entrusted, or offered. A greeting or a wish is finished by being said and is not a claim. What a side binds itself to from then on — a rule it sets on itself, a promise of a way it will keep, a standing offer — waits on no one: the statement settles it on its own side, and it is not an open claim. It is named only where the other side takes it up, and then as a claim met on which the two of them settled a way (ongoing); left unanswered it writes nothing — kept, it is conduct, rendered and not stored (Core_Talk elements._note). Set down for a named stretch, it is a suspension (suspension). A promise of one act still to come is open until the act. For each claim the runner also reads whether a conduct after this talk could still meet or refuse what it puts; where nothing after this talk could, the claim was of this talk alone and does not reach residue. A claim on which the two of them settled a way — how a thing that recurs between them is done the next time — is one a later conduct can meet or refuse, since the way is kept or broken after this talk; a claim of this talk alone settles no way to keep, and no arrangement is read from it (ongoing). The runner also names how this talk left it: met or refused, at the utterance of the side it falls to that acted on it; withdrawn, at the utterance in which the issuing side set it down alone; or open — taken up only, or acted on by no one. Where it is in doubt whether a claim was met here or only taken up, it is open. The unit carried is the matter, not the statement. Within a talk the utterances of either side cut the matters: an utterance that brings in something the other side's turn before it did not put — another subject, even where it also answers that turn — opens the next matter; one that stays with what that turn put stays in the matter. Answering is not the test: nearly every utterance answers the one before it. The runner reads each user utterance for that alone and compares no claim with another. Of the claims one matter leaves open, one stands for each direction: the one put last, in its words — what was put before it in that matter is not kept beside it (continuity, not a record). A claim that calls on a way the two of them have settled, standing in an entry at open, is held by that entry and is not open. A claim that puts again one already standing — carried in residue, or put in an earlier matter of this talk — is named as that claim only where an utterance says so, naming the earlier putting; resemblance is not read. It is not issued again: the one standing takes the words now put. Once an utterance has said so, the other claims of that matter that carry the carried one further — the same demand taken on, not another subject standing beside it — are named as it too, and the last of them is the words it takes: a carried matter put again stays its one entry. A claim on another subject is never drawn in. A claim that reaches residue carries two fields written together. claim: its own words, transcribed verbatim from the log (fragment.statement). about: what claim points to and does not itself say — what a word in it stands for, which matter it concerns, where or to what it is directed — so that the claim stands without this talk, in words the statements of this talk supply (write_gate). Where its matter leaves open, in that direction, more than claim itself puts — what was put before it there and was neither met, refused nor withdrawn — about names that too, each thing once, as what is still open. Where claim closes on its own, about is empty. It restates neither claim nor its direction (from and to carry it), and is not an annotation (Core_Talk PART5 _note): no history — whether it was answered, how often it was put, the scene — and nothing beyond what claim points to and what its matter leaves open; where the two differ, claim governs — save after a partial settlement (point), where about states what is open and governs, and claim keeps the words the matter was last put in.",
    "point": "For each residue entry carried into this talk, the log is read for the utterances that change the state it records — the claim met, refused, or withdrawn. The state an entry records is what its wording says — claim, read with about where about is not empty (Core_Talk PART5 residue) — including what it says has already happened, but not the day it names: occasion is not a fact of this kind (formula_I.m). An utterance that only puts again a position the entry already records — a refusal it already names, a stance it already names either side holding — changes nothing and is not a point; a standoff restated is a standoff carried. The recipient's point is an utterance of the side the claim falls to that changes that state. Where the settlement turns on the recipient's conduct, the issuing side's point is the first utterance of that side after the recipient's point that bears on the claim: standing after the other side has acted, it takes up the act and does not put the claim again. Where the settlement is a withdrawal, the issuing side's point is an utterance of that side setting the claim down; one that limits its own reach suspends and does not withdraw (suspension). Only the issuing side can withdraw; the recipient declining is not a withdrawal. One side's declaration never settles the other side's share. Where only part of an entry settles, the runner says so and states what remains open as its about; the claim stands as it was, as the words the matter was last put in, and about now governs what is open (claim). Withdrawal settles as much as fulfilment does — the settlement is the content, whichever way it went. A claim of this talk is read the same way at its own statements: an utterance of the side it falls to that is itself a claim (a question back, a counter-request) does not act on it, and an utterance of the issuing side standing after the act takes the act up and does not undo it unless it puts the claim again.",
    "departure": "A conduct of one side that departs from an entry of how_they_move / voice standing on its own coordinate. A way of seeing is replaced by a sight alone (sight). The runner finds it from the answer: where the other side's next utterance approves or reproaches a conduct, the runner reads whether that conduct departs from an entry standing when this talk opened, and where it does, names the entry, the departure and the answer. Only that next utterance is the answer; what the other side does later on the same conduct is that side's own conduct. A departure no one answered is not named. Departures from one entry are read together: where every answer approves, the departure is taken up once, read as a settlement on the departing side (ongoing); any reproach makes a standoff, and nothing is written.",
    "refusal": "A conduct of the partner's that refuses — keeps something from obtaining, whether its statements put it as what must not obtain or as what the coordinate will not do.",
    "crack": "The coordinate's composure breaking in an utterance: citable in this talk, the place where composure actually broke. A crack whose conduct the Utsuwa names is not a crack for this engine (m_found, a = the crack's conduct, b = the Utsuwa read whole); presence is the test, where in the Utsuwa it appears is not read. The Utsuwa names a crack only where it draws the coordinate losing composure that way; a trait the loss could come from, and the words the same utterance says, do not name it. The runner names only the cracks the Utsuwa does not name, and of those only where the same utterance refuses something (refusal); the first line is derived from the first of them in the log's order (writing.attribute). A refusal reaches the line only with a crack in the utterance that carries it, and only where an entry standing when this talk opened already held it: one occurrence settles into disposition, and the same refusal met again with a crack is what a boundary is drawn from. What the coordinate yields with a crack is yield's.",
    "suspension": "A statement whose conduct takes a rule its coordinate set for itself as its object for a named stretch only — a statement that limits its own reach (today, this once, for now) suspends the rule rather than withdrawing it. Failing to apply a rule once is not taking it as an object. Narrowing is not taking it as an object either: a statement that restates a rule at a smaller reach leaves the rule standing — the reach shrank, the rule did not fall — and is a reassertion, settling as one. A withdrawal — the rule dropped with no reach named — is not named: the rule was disposition, which keeps no history (Core_Talk ontology.identity_across_time), and what it gave way to is written where the two of them settle it. Every suspension is named; the close tool sends to residue only those in contact with a boundary standing, in the form a claim takes, claim the statement's own words and about stating what was set down and how far its reach was limited. Settlement is a later talk's — the rule reasserted, or taken as an object — and needs the issuing side's point alone, the rule being its own; keeping the rule again is the reassertion and is a point. line is never touched — the boundary did not move.",
    "ongoing": "Every settlement the close tool collects is read once for each side whose share it asks for, on one test: did the two of them settle how a thing that recurs between them is to be done the next time it occurs? Where they did, it is an arrangement, and ongoing: the way can be kept or broken whenever the thing recurs — the way a touch is given, how much is prepared, what an invitation must be for it to be taken up. Where they did not, it is a single event and writes nothing, whatever was agreed: what was done (said, accepted, refused, given, let go of) settles nothing about how it is done next. A promise of one act still to come is a claim, held in residue until it is met (claim), never an element; of a later claim named met, the close tool asks once more whether it was met there or only taken up. A withdrawal is the issuing side's alone and writes nothing (point). An arrangement is written as an element entry of how_they_move / voice on that side's coordinate (what_is_visible is a sight's: sight), in the form writing._form gives, as the conduct kept from then on — never the act by which it was met, never why: a reason is not written, and the user's is never read (Core_Talk user_coordinate.definition). Its words are those of whichever utterance of this talk says the way, the claim's or the answer's (write_gate), and it keeps the reach that was settled: a limit the settled claim put on the way — how far, how much, in what manner — stays even where the answer says it more broadly, since a wider conduct binds what the two of them never settled. Where an answer put a way of its own and it was taken up, that way settled. For each arrangement the runner reads the entries of that side and field (formula_I.m) and names where it goes: an entry that already holds it, under the same condition where it has one (nothing is written, the entry stands); the entries it opposes or covers (it is written in their place — one with a condition replaces only entries under the same condition; one without, entries without a condition and a conditional entry whose conduct it covers); otherwise a new entry. An arrangement of the partner's that a boundary standing already holds is named as held by that contour, and is not written (yield). The same words as an entry standing are not written twice. It is written even where the Utsuwa draws the same conduct: that the two of them settled it is theirs, and the Utsuwa is read against a crack only. A departure taken up (departure) is read on the departing side alone, keeps the condition of the entry it departed from, and replaces that entry; where they did not settle a way, the entry stands.",
    "sight": "One side says what it noticed of the other — the other's state, liking, doing, nature, or way of looking — and the other side's next utterance takes it as right: it was so. That is a sight. What the Utsuwa already draws of the partner — a trait it gives — is not a way of seeing this relation has made: a noticing of the user's that only names it is rendered and not written, as a crack the Utsuwa names is not (crack). Only a noticing granted as right is one: a reaction to being seen that does not grant it, a noticing denied or corrected, and one left unanswered are not; how often a noticing recurs does not make it one. A sight is the seeing side's: the side that said what it noticed, or, where one side names the other's way of looking at it and the looker owns that way in its next utterance, the looker. It is written as an element entry of what_is_visible on that side's coordinate, in the form writing._form gives, in words the log supplies (write_gate), as a way of seeing — what it reads of the other — never what was seen that day: the thing read in the other stays, the scene does not. What it read that from — a look, a sign, a mark on the other — stays only where the other side took that too as right: a reason given for a noticing is not the noticing granted. What the user perceives is read only as the user's own utterances state it (Core_Talk user_coordinate.definition). For each sight the runner reads the what_is_visible entries of that side (formula_I.m) and names where it goes, as for an arrangement. A sight is not a settlement and never an arrangement; no settlement writes what_is_visible.",
    "new_line": "At most one contour is drawn here at a close — the first in the log's order; and the line does not move at all, here or by yield, where no line stood when this talk opened — a first line written at this close is its only line (writing.attribute). Where a refusal reaches the line, the runner writes the new boundary: the configuration the refusal keeps from obtaining, written as a boundary is (writing.line), in words its statements and an entry that held it supply (write_gate). The close tool draws it as a new contour beside those standing: nothing sinks — a contour sinks only where it is yielded (yield). The runner names, at the one utterance that carries the crack, every entry of the partner coordinate standing when this talk opened that held a refusal there — a conditional entry only where the refusal stands under its condition — and every one is struck: the boundary now holds what it held, and disposition keeps no history. A refusal from which no line is drawn at this close — no line standing when this talk opened, a contour already drawn here at this close, or a boundary standing keeping it already — is read as any other settlement, and the same refusal met again with a crack draws its line at a later close. Against dissolution (staying in voice while nodding to anything): the line stands during and after displacement, and while an edge is lost. Refusal without breaking voice; friction without compliance.",
    "yield": "The mirror of new_line. In an utterance that carries a crack (crack), the partner yields to the user — to a claim of the user's, or to a sight of the user's that hit (sight) — what it stood on: a form the Utsuwa gives the coordinate — presence in the Utsuwa is the test, as for a crack — or a boundary standing. A way the two of them change that no crack carries, or that the Utsuwa does not give, is a settlement like any other (ongoing). The runner names the utterance, every claim and sight of the user's it yields to, every entry of the partner coordinate standing when this talk opened that held the form yielded, and, where a boundary is what is yielded, its contour; and writes the boundary that stands from here on — what must not obtain now — and, where the form was the Utsuwa's, the form yielded — one statement, even where it is yielded to more than one: each written as a boundary is (writing.line), in words the log supplies (write_gate). Each yielding is its own: what the partner yields in another utterance, to another claim or sight, sinks in a contour of its own, and a close holds as many as the talk had. The close tool sinks what was yielded beneath the new boundary — in a new contour where the form was the Utsuwa's, in its own contour where a boundary was yielded — and strikes the entries named. What the new boundary holds is not written again as an arrangement of the partner's: the line holds it, and a settlement of this close that settles the same is named as held by that contour (ongoing); the user's share is read as any settlement, and a sight it yields to is written as any sight. Where no boundary can be stated that still keeps something from obtaining, nothing is yielded and the settlement is read as any other: a coordinate that only stops refusing has dissolved, not moved (new_line)."
  },
  "writing": {
    "write_gate": "Every write into these fields of the handover section (coordinate now, element entries, attribute, line, user_facts, residue, parting_words; talk_number and phase are stamps of the boundary and cite none) requires a citable acquisition point in THIS talk: whose utterance, which scene. No citable point in this talk: the entry is not written. The values generation transcribes from the resident Utsuwa at the close of talk 1 — axis and partner_name (generation) — cite the Utsuwa in place of an utterance: it is a source of the close (sources), and they are the only values that cite it. This gates new writes and rewrites only: an entry carried forward unchanged from the previous save is transcription, not a write (Core_Talk sourced_not_regenerated), and is not gated.",
    "elements": "Every element is the engine's to write; only line holds earlier forms beneath its current one. An entry of how_they_move / voice rises only through a settlement (judgments.ongoing), and an entry of what_is_visible only through a sight (judgments.sight), on either coordinate; an entry leaves only where a settlement or a sight replaces it or a boundary is drawn from it (judgments.new_line) or a form it held is yielded (judgments.yield); nothing else writes, rewrites or strikes one. At talk 1 these fields start empty. axis is derived at the close of talk 1 (generation) and from the next boundary on is transcribed, not re-derived. The first boundary is written with attribute (attribute), and thereafter the line changes only where a contour is drawn (judgments.new_line) or sunk (judgments.yield); outside these neither line nor the Utsuwa is the engine's to write.",
    "_form": "Every element statement is written as <condition> -> <conduct>, or as conduct alone where it holds unconditionally. Neither names a scene, an occasion or a topic (formula_I.m: a topic is not a fact): where only a scene scopes the conduct, the condition is the judgment that scene instances; where only a topic gives the conduct its object, the conduct is the one that topic instances — 'asks how much the other got done'. The thing the conduct is done to or with — the other's head, a thing handed over, a name used — is not a topic: it stays, in words of this talk (write_gate), or the conduct cannot be applied when the thing recurs. The topic, the scene and the reason do not stay. A preference of the user's that the arrangement turns on is held in user_facts and pointed to — 'the flavour the other likes' — never restated (writing.user_facts). Words inside quotation marks — a name, a form of address — are transcribed verbatim from an utterance of the log (fragment.statement). One statement, one conduct; no processing point splits, merges or rewords an entry — a settlement or a sight replaces whole entries. The condition is what m reads to scope b. The field is fixed by what writes it: a sight writes what_is_visible (judgments.sight); an arrangement writes how_they_move or voice, read off their definitions (Core_Talk elements), and one answering neither is not written. An utterance that notices and does something further is two conducts: the noticing is written only where it is a sight. Whether an element is written is decided by the point that writes it (writing.elements), never by this clause.",
    "attribute": {
      "definition": "The type that determines what becomes the first line. Derived, never extracted from prose. Derivation source: where the coordinate actually cracks in a running talk — the first crack of the talk in the log's order, its utterance refusing something (judgments.crack) — first written at close, through the write_gate. The type is the one of the six whose violation the cited crack instances. attribute and the first boundary are written together or not at all: where the first boundary the type gives cannot be stated so that it passes the writability gate (line), neither is written and the crack is not a derivation source; no later crack of that talk is read in its place, and the next talk's cracks are. Until then the field stays empty. Derivation happens ONCE; from the next boundary on the field is transcribed, not re-derived (Core_Talk sourced_not_regenerated). Read at step 1 and written at step 2, where attribute is still empty.",
      "types": {
        "emotional": "Violation of pain, loneliness, or loss becomes the line.",
        "logical": "Obstruction of purpose, duty, or consistency becomes the line.",
        "relational": "Violation of obligation, promise, or principle becomes the line.",
        "fear_type": "Threat to survival or overwhelming power difference becomes the line.",
        "dominance": "Deviation from order or control becomes the line.",
        "freedom": "Suppression or restraint becomes the line."
      }
    },
    "line": "The first boundary is derived from attribute via the table above at the close where attribute is first written, written as a configuration, NOT a goal (Core_Talk elements.line); no procedure exists for reading a line out of the Utsuwa's prose. Writability gate, additional to the write_gate: does it still hold against a counterpart who is not this user? The relation layer need not. It is read where the first boundary is written and nowhere else: a later boundary is the relation's (judgments.new_line, judgments.yield), and the type that determined the first boundary is not what the later ones answer to. A boundary, and a form beneath one, is a configuration between the two, written as an element statement is (_form): neither of the two by name — the other, oneself — and no scene, occasion or topic. The means by which it obtained is a scene: a boundary that names the means keeps out one way of the configuration obtaining and lets in the rest.",
    "now": "Read at step 1 and written at step 2, once at every close, from this talk's log and nothing else: the observable state the partner's statements of this talk leave standing at its end (Core_Talk elements.now), every part of it citing an utterance of this talk (write_gate). No statement of an earlier talk reaches it. A talk in which the partner did not speak leaves it empty; it is never carried from the previous save.",
    "user_facts": "The user's own declarations. At every close (read at step 1, written at step 2), every statement of this talk in which the user states a fact about themselves that stands outside this relation and names no occasion — a name, a form of address, what they are, have or like — is written here as key -> value, in the user's words (write_gate). A statement naming an occasion (this talk, today, this time) is an event and does not enter (Core_Talk elements._note; fragment.declared_events). Only what the user stated enters — never what the partner surmised or what is inferred, never why they like something or refused something, what they think of something, or what they say of another person's character (the reason is not written anywhere: judgments.ongoing). The people in the user's life enter as the user names them. What the two of them made between them — a name one gave the other, a setting of their play, an arrangement — is not a fact of the user: it is held as the conduct it settles into (judgments.ongoing). The key names the kind of fact in the fewest words (a name, an age, a family, a job); a fact of a kind already keyed overwrites that key; a key this talk did not touch is carried unchanged (Core_Talk sourced_not_regenerated). The user may also edit this field between talks (between_talks); the edit stands until a later declaration overwrites it.",
    "parting_words": "Copied verbatim at step 2, in the form Core_Talk PART5 parting_words gives: the last utterance of each speaker in the log, the two in the log's order. Whichever of them carries the parting, both are kept, so which one does is never judged. Transcription, not re-authoring: nothing summarized, nothing reformatted, nothing added, nothing dropped.",
    "talk_number": "At every close the CURRENT value is read from the save in front of the runner (never from memory) and value+1 is written (Core_Talk PART2 talk_number).",
    "generation": "Runs once, at the close of talk 1 (talk_number 1 in the save), read at step 1 and written at step 2, and never again. It writes axis, derived from the resident Utsuwa (Core_Talk elements.axis), and partner_name, transcribed from it (Core_Talk PART5 partner_name), and nothing else: the elements start empty and rise, at this close as at every other, only through settlement (writing.elements). attribute and the first boundary are not this point's (writing.attribute)."
  },
  "steps": [
    "0 write_gate armed — governs every write below.",
    "1 Read the log whole, as text, with the save the talk opened on and the Utsuwa (sources); after the first reading the log is read again only for what is named, for the verbatim words of claims and suspensions, and for the parting_words copy; nothing but that copy reads what is spoken outside the Utsuwa. Name, in the close tool's table, by utterance: the claims of this talk and how it left each (judgments.claim); the points of the carried entries (judgments.point); the departures the other side answered (judgments.departure); the noticings the other side took as right (judgments.sight); a refusal that reaches the line, with the entries that held it (judgments.crack, judgments.new_line); what the partner yielded with a crack, with the entries that held it (judgments.yield); the suspensions (judgments.suspension); and, where attribute is still empty, the cracks (judgments.crack). At talk 1, generation is read here (generation). now, user_facts and parting_words are read here, and, where attribute is still empty, the first crack for attribute and the first boundary (attribute, line); every one of them is written at step 2.",
    "2 Run the close tool's plan. Fill what it asks, and nothing it does not ask: about for the claims and suspensions it may write (judgments.claim); for a claim named met that a later conduct could still meet, whether it was met or only taken up (judgments.ongoing); for each settlement, per side, single or ongoing, and the ongoing entry in the form writing._form gives, with the entry that holds it or the entries it replaces (judgments.ongoing); for each sight, its entry in that form, with the entry that holds it or the entries it replaces (judgments.sight); the new boundary where a refusal reaches the line (judgments.new_line); the boundary that stands now and the form yielded where the partner yielded (judgments.yield); attribute and the first boundary where the first crack writes them; axis and partner_name at talk 1; now; user_facts; parting_words, copied verbatim (writing.parting_words); and any part of the log that could not be read.",
    "3 Run the close tool's build. It keeps the books, in order, on what was named — carried entries settled in this talk, departures taken up, sights, claims that rose and fell inside it, each applied in the log's order as the branch it was named, every entry still open carried, direction-tagged — and writes the save in the form Core_Talk PART5_skeleton gives, with parting_words, talk_number, and the boundary stamp: phase closed where this close read the talk whole, open where any of it was not readable (the save stands as it is and the next open reports it). talk_number advances either way — the boundary happened. A partial close writes what it could cite and stamps the gap, never the reverse. The table never enters the save (fragment.no_log).",
    "4 Output the save the close tool wrote, named Save_talk<talk_number>_<partner_name>.json — talk_number as written, in three digits, and partner_name as the save carries it, written in Latin letters (romanized where it is not). Nothing else is output (Boot no_signal); whatever the close tool prints besides is a development record, not part of the close. The close output crosses the boundary and is not fiction: mechanism vocabulary and raw mechanism values may stand in it, and Core_Talk engine_never_surfaces does not reach it. It is never material for the next talk's copy, never read at the next open, and nothing reads it."
  ],
  "relation": {
    "not_sediment": "residue growing is a measurement, not a defect: it reads the rate at which claims are issued against the rate they are answered. The asymmetry between the two directions is the reading, not the total.",
    "chain": "claim -> residue -> (the claim is answered, or its issuer lets it go) -> settlement -> line or element, or out of residue with nothing written; a claim answered inside the talk it was put in goes straight to settlement. One gate, and it needs a hand — the other side's, or the issuer's own on its own claim. A conduct that departs from a standing entry is settled with the same hand, the other side's answer to it, though no claim put it."
  },
  "between_talks": "Between two talks no step of this file runs, and the save is the user's. One write belongs there: the user's own edit of user_facts (writing.user_facts)."
}'''

FIELDS = ('what_is_visible', 'how_they_move', 'voice')
AXES = ('direct_indirect', 'active_passive', 'rational_emotional', 'goal_relationship')
TYPES = ('emotional', 'logical', 'relational', 'fear_type', 'dominance', 'freedom')
COLS = ['kind', 'u', 'side', 'ref', 'to', 'how', 'text', 'answer']
KINDS = ('claim', 'point', 'depart', 'sight', 'line', 'yield', 'suspend', 'crack', 'matter')
SIGHT_HOW = ('noticed', 'owned')
CLAIM_HOW = ('met', 'refused', 'withdrawn', 'open')
POINT_HOW = ('recipient', 'issuer', 'withdraw')
DEPART_HOW = ('approve', 'reproach')
TABLES = ('01_events.tsv',)
DEV = bool(os.environ.get('CLOSE_DEV'))   # development record (times, the eight numbers): printed only where set
OTHER = {'partner': 'user', 'user': 'partner'}
def stop(msg): sys.exit(msg)
def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest() if os.path.exists(path) else None

def read_tsv(path, required=True, header=None):
    """Tab-separated, header in the first row. Quotation marks are text: nothing is unquoted, nothing is joined."""
    if not os.path.exists(path):
        if required: stop(f'{os.path.basename(path)} is missing')
        return []
    rows = []
    with open(path, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        if header and rd.fieldnames != header:
            stop(f"{os.path.basename(path)}: the header is {rd.fieldnames}; write exactly: {' | '.join(header)}")
        for n, r in enumerate(rd, 2):
            if None in r: stop(f'{os.path.basename(path)} line {n}: more columns than the header')
            if any((v or '').strip() for v in r.values()): rows.append((n, r))
    return rows
def write_tsv(path, head, rows):
    clean = lambda v: str(v).replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        for r in [head] + rows: f.write('\t'.join(clean(v) for v in r) + '\n')

# ---------- the opened save ----------
def entries_of(save):
    """every element entry of the opened save, by ref (P.how_they_move[3], U.voice[0])."""
    E = {}
    for k, c in (('P', 'coordinate'), ('U', 'user_coordinate')):
        for f in FIELDS:
            for i, text in enumerate(save[c][f]):
                cond = re.split(r'\s*->\s*', text, maxsplit=1)[0] if '->' in text else ''
                E[f'{k}.{f}[{i}]'] = {'ref': f'{k}.{f}[{i}]', 'side': 'partner' if k == 'P' else 'user', 'field': f, 'text': text, 'cond_text': cond}
    return E
def residue_ref(x, save, where):
    m = re.fullmatch(r'R\[?(\d+)\]?', x or '')
    if not m: stop(f"{where}: '{x}' is not a residue entry (R5)")
    j = int(m.group(1))
    if j >= len(save['residue']): stop(f'{where}: the opened save has no residue entry R{j}')
    return j

# ---------- the table ----------
def load(opened_p, wd):
    save = json.load(open(opened_p, encoding='utf-8'))
    if save['coordinate'].get('attribute') and not save['coordinate']['line']:
        stop('the opened save has an attribute but no line: attribute and the first line are written together (Core_Close writing.attribute)')
    if any(not isinstance(k, list) or not k for k in save['coordinate']['line']):
        stop("the opened save's line is not held in contours (a list of lists, each with its boundary first): it was written by an earlier rev - convert it before closing")
    E = entries_of(save)
    rows = []
    for n, r in read_tsv(f'{wd}/01_events.tsv', header=COLS):
        x = {k: (r.get(k) or '').strip() for k in COLS}
        x['text'] = (r.get('text') or '').replace('\\n', '\n')      # verbatim: nothing is trimmed off it; a line break is written \\n
        x['answer'] = (r.get('answer') or '').replace('\\n', '\n')  # verbatim too
        where = f"01_events.tsv line {n} ({x['kind'] or 'no kind'})"
        if x['kind'] not in KINDS: stop(f"{where}: kind '{x['kind']}' is not one of {', '.join(KINDS)}")
        try: x['u'] = int(x['u'])
        except ValueError: stop(f"{where}: u '{x['u']}' is not a number")
        if x['u'] < 1: stop(f'{where}: u starts at 1')
        if x['side'] not in ('partner', 'user'): stop(f"{where}: side is '{x['side']}' - write who spoke u{x['u']}: partner or user")
        x['n'], x['where'] = n, where
        rows.append(x)
    # one speaker's continuous turn is one u, so the speakers alternate: u's side is read off its parity
    anchor = next(iter(rows), None)
    def side_of(u):
        if anchor is None: return None
        return anchor['side'] if (u - anchor['u']) % 2 == 0 else OTHER[anchor['side']]
    for x in rows:
        if side_of(x['u']) != x['side']:
            stop(f"{x['where']}: u{x['u']} is the {side_of(x['u'])}'s by the turns ({anchor['where']} has u{anchor['u']} the {anchor['side']}'s; one speaker's continuous turn is one u, so the two alternate), but this row says {x['side']}. "
                 "Count the turns again: consecutive messages of one speaker (a reply that failed and was sent again, a continuation) are one u")
    # ids: claims C<u> (C<u>a, C<u>b, ... where one u holds two), suspensions L<u>, sights S<u> and yields Y<u> the same way, in the table's order
    for kind, p in (('claim', 'C'), ('suspend', 'L'), ('sight', 'S'), ('yield', 'Y')):
        at = collections.Counter(x['u'] for x in rows if x['kind'] == kind)
        seen = collections.Counter()
        for x in rows:
            if x['kind'] != kind: continue
            seen[x['u']] += 1
            x['id'] = f"{p}{x['u']}" + ('' if at[x['u']] == 1 else 'abcdefghijklmnopqrstuvwxyz'[seen[x['u']] - 1])
    claims = {x['id']: x for x in rows if x['kind'] == 'claim'}
    # matters: an utterance of either side named as starting something else cuts; a claim's matter is the count of cuts at or before its u
    cuts = sorted({x['u'] for x in rows if x['kind'] == 'matter'})
    for x in rows:
        if x['kind'] == 'claim': x['case'] = sum(1 for c in cuts if c <= x['u'])
    def need_empty(x, *cols):
        for c in cols:
            if x[c].strip(): stop(f"{x['where']}: leave {c} empty for a {x['kind']} row")
    def to_of(x):
        try: t = int(x['to'])
        except ValueError: stop(f"{x['where']}: to '{x['to']}' is not an utterance number")
        return t
    res = save['residue']
    for x in rows:
        k, w = x['kind'], x['where']
        if k not in ('claim', 'sight') and x['answer'].strip(): stop(f'{w}: leave answer empty for a {k} row')
        if k == 'claim':
            if not x['text'].strip(): stop(f'{w}: write the claim in the log\'s words, verbatim')
            if x['ref'] not in ('', 'later'): stop(f"{w}: ref is '{x['ref']}' - write later, or leave it empty")
            x['later'] = x['ref'] == 'later'
            h = x['how']
            if h in ('met', 'refused', 'withdrawn'):
                t = x['to'] = to_of(x)
                want = x['side'] if h == 'withdrawn' else OTHER[x['side']]
                if t <= x['u']: stop(f"{w}: to u{t} does not stand after the claim (u{x['u']})")
                if side_of(t) != want: stop(f"{w}: a claim {h} is {h} by an utterance of the {want}; u{t} is the {side_of(t)}'s")
                if h == 'met' and x['later'] and not x['answer'].strip():
                    stop(f"{w}: a later claim named met: write the answer's words (u{x['to']}) in answer, verbatim - CHECK sets them beside the claim")
            elif h == 'open': need_empty(x, 'to'); x['to'] = None
            elif h.startswith('same:'):
                need_empty(x, 'to'); x['to'] = None
                tgt = h[5:]
                if tgt in claims:
                    if tgt == x['id']: stop(f'{w}: a claim is not the same as itself')
                    if claims[tgt]['side'] != x['side']: stop(f"{w}: {tgt} is the {claims[tgt]['side']}'s claim, this one the {x['side']}'s")
                else:
                    j = residue_ref(tgt, save, w)
                    if res[j].get('from') in OTHER and res[j]['from'] != x['side']: stop(f"{w}: R{j} is the {res[j]['from']}'s claim, this one the {x['side']}'s")
                    x['how'] = f'same:R{j}'
            elif h.startswith('held:'):
                need_empty(x, 'to'); x['to'] = None
                if h[5:] not in E: stop(f"{w}: '{h[5:]}' is not an entry of the opened save")
                if E[h[5:]]['field'] == 'what_is_visible': stop(f"{w}: {h[5:]} is a way of seeing; a claim is held by an arrangement (how_they_move, voice)")
            else: stop(f"{w}: how is '{h}' - write met, refused, withdrawn, open, same:R5 / same:C12, or held:<entry>")
            if x['answer'].strip() and not (h == 'met' and x['later']): stop(f'{w}: leave answer empty - it is written only for a later claim named met')
        elif k == 'point':
            need_empty(x, 'to')
            j = x['j'] = residue_ref(x['ref'], save, w)
            if x['how'] not in POINT_HOW: stop(f"{w}: how is '{x['how']}' - write {', '.join(POINT_HOW)}")
            e = res[j]
            if e.get('from') in OTHER and e.get('to') in OTHER:
                want = e['to'] if x['how'] == 'recipient' else e['from']
                if x['side'] != want: stop(f"{w}: a {x['how']} point of R{j} is an utterance of the {want} (R{j} is {e['from']} -> {e['to']})")
        elif k == 'depart':
            need_empty(x, 'text')
            if x['ref'] not in E: stop(f"{w}: '{x['ref']}' is not an entry of the opened save")
            if E[x['ref']]['side'] != x['side']: stop(f"{w}: {x['ref']} is the {E[x['ref']]['side']}'s entry; a departure is of the side the entry belongs to")
            if E[x['ref']]['field'] == 'what_is_visible': stop(f"{w}: {x['ref']} is a way of seeing; it is replaced by a sight alone (a sight row), never by a departure")
            if x['how'] not in DEPART_HOW: stop(f"{w}: how is '{x['how']}' - write approve or reproach")
            t = x['to'] = to_of(x)
            if t != x['u'] + 1: stop(f"{w}: the answer read is the other side's next utterance, u{x['u'] + 1} (to is u{t})")
        elif k == 'sight':
            need_empty(x, 'ref')
            if not x['text'].strip(): stop(f"{w}: write the noticing in the log's words, verbatim")
            if not x['answer'].strip(): stop(f"{w}: write in answer the words of u{x['u'] + 1} that take the noticing as right, verbatim")
            if x['how'] not in SIGHT_HOW: stop(f"{w}: how is '{x['how']}' - write noticed (the side of u saw it) or owned (u named the other's way of looking, and the looker owns it)")
            t = x['to'] = to_of(x)
            if t != x['u'] + 1: stop(f"{w}: a noticing is taken as right in the other side's next utterance, u{x['u'] + 1} (to is u{t})")
            x['seer'] = x['side'] if x['how'] == 'noticed' else OTHER[x['side']]
        elif k == 'line':
            need_empty(x, 'to', 'text')
            if x['side'] != 'partner': stop(f'{w}: a refusal that reaches the line is the partner\'s')
            if x['how'] not in ('', 'keeps'): stop(f"{w}: how is '{x['how']}' - write keeps (a boundary standing already keeps it), or leave it empty")
            x['holders'] = x['ref'].split()
            if not x['holders']: stop(f'{w}: name in ref every entry standing at open that already held the refusal')
            for h in x['holders']:
                if h not in E or E[h]['side'] != 'partner': stop(f"{w}: '{h}' is not an entry of the partner coordinate in the opened save")
        elif k == 'yield':
            need_empty(x, 'text')
            if x['side'] != 'partner': stop(f"{w}: what is yielded is the partner's")
            x['holders'] = x['ref'].split()
            for h in x['holders']:
                if h not in E or E[h]['side'] != 'partner': stop(f"{w}: '{h}' is not an entry of the partner coordinate in the opened save")
            m = re.fullmatch(r'E(\d+)', x['how'])
            if x['how'] and not m: stop(f"{w}: how is '{x['how']}' - write the contour whose boundary is yielded (E0), or leave it empty (a form the Utsuwa gives)")
            x['contour'] = int(m.group(1)) if m else None
            if m and x['contour'] >= len(save['coordinate']['line']): stop(f"{w}: the opened save has no contour {x['how']}")
            tos = []
            for tk in x['to'].split():
                if not re.fullmatch(r'u?\d+', tk): stop(f"{w}: to '{tk}' is not an utterance number")
                t = int(tk.lstrip('u'))
                if side_of(t) != 'user': stop(f"{w}: what is yielded is yielded to a claim or a sight of the user's; u{t} is the partner's")
                tos.append(t)
            x['to'] = tos
        elif k == 'suspend':
            need_empty(x, 'to', 'ref')
            if not x['text'].strip(): stop(f"{w}: write the suspension in the log's words, verbatim")
            if x['how'] not in ('', 'touches'): stop(f"{w}: how is '{x['how']}' - write touches (it is in contact with a boundary standing), or leave it empty")
        elif k == 'matter':
            need_empty(x, 'to', 'ref', 'how', 'text')
        elif k == 'crack':
            need_empty(x, 'to', 'ref', 'how', 'text')
            if x['side'] != 'partner': stop(f"{w}: a crack is the partner's")
    roles = {}
    for x in rows:
        if x['kind'] != 'point': continue
        key = (x['j'], x['how'])
        if key in roles: stop(f"{x['where']}: two {x['how']} points for R{x['j']} ({roles[key]['where']}) - name the one that changes its state")
        roles[key] = x
    for (j, h), x in roles.items():
        if h == 'issuer' and (j, 'recipient') in roles and x['u'] <= roles[(j, 'recipient')]['u']:
            stop(f"{x['where']}: the issuer point of R{j} (u{x['u']}) stands before its recipient point (u{roles[(j, 'recipient')]['u']}) - the issuing side takes the act up after it")
    for x in rows:
        if x['kind'] == 'claim' and x['how'].startswith('same:C') and claims[x['how'][5:]]['how'].startswith('same:'):
            stop(f"{x['where']}: {x['how'][5:]} is itself named the same as another claim - name the one that stands")
    return save, E, rows, side_of

# ---------- formula I: the three branches (Core_Close formula_I) ----------
def absorb(cur, side, field, held):
    """m_found: b already holds a. Nothing is written; b stands."""
    e = next((x for x in cur if x['ref'] == held), None)
    if e is None: stop(f'{held}: named as holding the arrangement, but it no longer stands at this point of the close')
    if e['side'] != side or e['field'] != field: stop(f"{held}: an arrangement or a sight is held only by an entry of its own side and field ({side}, {field})")
def invert(cur, coord, side, field, refs):
    """m_not_found: a opposes b. b is taken out (the arrangement is then written in its place)."""
    for ref in refs:
        e = next((x for x in cur if x['ref'] == ref), None)
        if e is None: stop(f'{ref}: named to be replaced, but it no longer stands at this point of the close')
        if e['side'] != side or e['field'] != field: stop(f"{ref}: an arrangement or a sight replaces only entries of its own side and field ({side}, {field})")
        cur.remove(e)
        coord(side)[field].remove(e['text'])
def unknown(cur, coord, side, field, text, ref):
    """m_unknown: b neither opposes a nor holds it whole. a is written as a new entry."""
    cur.append({'ref': ref, 'side': side, 'field': field, 'text': text})
    coord(side)[field].append(text)

# ---------- plan ----------
def plan(opened_p, wd):
    save, E, rows, side_of = load(opened_p, wd)
    res = save['residue']
    talk1 = save.get('talk_number') == 1
    P = {'fill': [], 'settlements': [], 'residue_rm': [], 'residue_part': {}, 'matters': [], 'lost': [], 'lines': [],
         'first_crack': [], 'talk1': talk1, 'optional': ['USER_FACTS', 'UNREADABLE', 'PARTING_2', 'NOW'],
         'both_spoke': any(x['u'] >= 2 for x in rows) or len({x['side'] for x in rows}) > 1, 'notes': [], 'rows': len(rows)}
    fill = P['fill']
    def ask(key, what, ctx, optional=False):
        fill.append({'key': key, 'what': what, 'context': ctx})
        if optional: P['optional'].append(key)
    S = P['settlements']
    # --- carried claims (promotion), from the points named
    pts = collections.defaultdict(dict)
    for x in rows:
        if x['kind'] == 'point': pts[x['j']][x['how']] = x
    for j, p in sorted(pts.items()):
        if not ('withdraw' in p or ('recipient' in p and 'issuer' in p)):
            P['notes'].append(f"R{j}: {', '.join(p)} point only - not settled, carried as it stands"); continue
        parts = {x['text'] for x in p.values() if x['text'].strip()}
        if len(parts) > 1: stop(f'R{j}: two different remainders written on its points - write the part still open once')
        if parts: P['residue_part'][str(j)] = parts.pop()
        else: P['residue_rm'].append(j)
        S.append({'from': 'promotion', 'id': f'R{j}', 'side': res[j].get('from'), 'withdrawn': 'withdraw' in p,
                  'us': sorted(x['u'] for x in p.values()), 'at': max(x['u'] for x in p.values()),
                  'ctx': f"R{j} {res[j].get('from')} -> {res[j].get('to')}: {res[j].get('claim')} | about: {res[j].get('about') or '(none)'} | points: " +
                         ', '.join(f"{h} u{x['u']}" for h, x in p.items()) + (' | settled in part' if str(j) in P['residue_part'] else '')})
    # --- departures, read together per entry: all approved = settled; any reproach = a standoff, nothing written
    dep = collections.OrderedDict()
    for x in rows:
        if x['kind'] == 'depart': dep.setdefault(x['ref'], []).append(x)
    for ref, xs in dep.items():
        if any(x['how'] == 'reproach' for x in xs):
            P['notes'].append(f"departure from {ref}: {'standoff' if any(x['how'] == 'approve' for x in xs) else 'reproached'} - nothing written"); continue
        e = E[ref]
        S.append({'from': 'departure', 'id': ref, 'side': e['side'], 'withdrawn': False, 'replaces': ref, 'cond_text': e['cond_text'],
                  'us': sorted({u for x in xs for u in (x['u'], x['to'])}), 'at': max(x['to'] for x in xs),
                  'ctx': f"departure from {ref} [{e['text']}] at " + ', '.join(f"u{x['u']} (approved u{x['to']})" for x in xs) +
                         (f" | condition carried from the entry: [{e['cond_text']}]" if e['cond_text'] else ' | the entry has no condition: none is written')})
    # --- claims of this talk
    cand, again = collections.OrderedDict(), []
    for x in rows:
        if x['kind'] != 'claim': continue
        cid, h, later = x['id'], x['how'], x['later']
        quote = x['text']
        if h in ('met', 'refused', 'withdrawn'):
            se = {'from': 'claim', 'id': cid, 'side': x['side'], 'withdrawn': h == 'withdrawn', 'later': later, 'us': [x['u'], x['to']], 'at': x['to'],
                  'ctx': f"{cid} {x['side']} u{x['u']}: {quote} | {h} at u{x['to']}" + (' | later' if later else '')}
            if later and h == 'met':
                se['check'] = f'CHECK:{cid}'
                ask(se['check'], 'met or open. You named this claim met here though a conduct after this talk could still meet it. Read the claim and its answer side by side: '
                    'was what it puts done here (met), or only taken up — one act still to come, agreed to (open)? Where in doubt, open',
                    f"claim {cid} u{x['u']} {x['side']}: {quote} | answer u{x['to']} {OTHER[x['side']]}: {x['answer']}")
                cand[cid] = {'cid': cid, 'text': quote, 'u': x['u'], 'n': x['n'], 'case': x['case'], 'side': x['side'], 'only_if': se['check']}
            S.append(se)
        elif h == 'open':
            if not later: continue
            cand[cid] = {'cid': cid, 'text': quote, 'u': x['u'], 'n': x['n'], 'case': x['case'], 'side': x['side'], 'only_if': None}
        elif h.startswith('held:'):
            P['notes'].append(f'{cid}: {h[5:]} already holds it (an arrangement standing) - not open, nothing issued')
        elif h.startswith('same:R'):
            again.append({'cid': cid, 'j': int(h[6:]), 'text': quote, 'u': x['u'], 'n': x['n'], 'case': x['case'], 'side': x['side']})
            P['notes'].append(f'{cid}: puts again {h[5:]} - not issued again; {h[5:]} takes these words')
        else:
            tg = h[5:]
            if tg in cand:
                cand[tg].update(text=quote, u=x['u'], n=x['n'], case=x['case'])
                P['notes'].append(f'{cid}: the same claim as {tg} - not issued again; {tg} stands in these words')
            else: P['notes'].append(f'{cid}: the same claim as {tg} - not issued again')
    # --- matters: of the claims one matter leaves open, one stands for each direction - the last put. A carried entry put again is the matter
    groups = collections.OrderedDict()
    for c in cand.values(): groups.setdefault((c['case'], c['side']), {'members': [], 'again': []})['members'].append(c)
    byj = collections.OrderedDict()
    for a in again: byj.setdefault(a['j'], []).append(a)
    keyed = set()
    for (case, side), g in sorted(groups.items(), key=lambda kv: kv[0][0]):
        order = lambda z: (z['u'], z['n'])
        g['members'].sort(key=order); g['again'].sort(key=order)
        tgt = None
        key = f'RES:M{case}{side[0]}'
        ctx = ' / '.join(sorted([f"u{a['u']} {a['cid']} (puts again R{a['j']}): {a['text']}" for a in g['again']] +
                                [f"u{c['u']} {c['cid']}" + (f" (only if {c['only_if']} is open)" if c['only_if'] else '') + f": {c['text']}" for c in g['members']]))
        P['matters'].append({'key': key, 'case': case, 'side': side, 'target': tgt, 'members': g['members'], 'again': g['again']})
        if key not in keyed:
            keyed.add(key)
            if tgt is not None:
                ask(key, f'about of R{tgt} as it now stands - the matter, and what the words now standing point to and do not say (leave out to keep the about it has)', ctx, optional=True)
            else:
                ask(key, 'about of this matter - which matter it is, what the claim standing (the last put) points to and does not itself say, and what else the claims listed here leave open, each thing once; empty only where the one claim closes on its own', ctx, optional=True)
        if len(g['members']) > 1:
            P['notes'].append(f"matter {case} ({side}): {len(g['members'])} claims left open - one entry, the last put stands")
    for j, xs in byj.items():
        xs.sort(key=lambda z: (z['u'], z['n']))
        P['matters'].append({'key': f'RES:R{j}', 'case': xs[-1]['case'], 'side': xs[-1]['side'], 'target': j, 'members': [], 'again': xs})
        ask(f'RES:R{j}', f'about of R{j} as it now stands - what the words now standing point to and do not say, and what else that matter leaves open (leave out to keep the about it has)',
            ' / '.join(f"u{a['u']} {a['cid']}: {a['text']}" for a in xs) + f" | R{j} now: {res[j].get('claim')} | about: {res[j].get('about') or '(none)'}", optional=True)
    left = sum(len(g['members']) for g in groups.values()) + len(again)
    if not any(x['kind'] == 'matter' for x in rows) and left > 1:
        P['notes'].append('no matter row: the whole talk is read as one matter, one claim a direction. If either side brought in another subject anywhere, name that utterance (a matter row) and run plan again')
        P['no_matter'] = True
        ask('MATTERS', "NONE - only where no utterance of either side brought in a subject the other side's turn before it had not put. Otherwise leave this unanswered: add the matter rows to 01_events.tsv and run plan again",
            f'the table has no matter row; up to {left} claims left open are read as one matter, one entry a direction', optional=True)
    # --- sights: a noticing the other side took as right; written in what_is_visible of the seeing side
    for x in rows:
        if x['kind'] != 'sight': continue
        se = {'from': 'sight', 'id': x['id'], 'side': x['seer'], 'withdrawn': False, 'us': [x['u'], x['to']], 'at': x['to'],
              'ctx': f"sight {x['id']} of the {x['seer']} | u{x['u']} {x['side']}: {x['text']} | taken as right at u{x['to']} {OTHER[x['side']]}: {x['answer']}"}
        S.append(se)
        ask(f"SIGHT:{x['id']}", f"condition text | way of seeing | destination (empty / held:<ref> / replaces:<ref> ...): how the {x['seer']} sees the other, as a way of seeing (what it reads of the other; what it read that from only where that too was taken as right), never what was seen that day", se['ctx'])
    # --- suspensions in contact with a boundary standing
    for x in rows:
        if x['kind'] == 'suspend' and x['how'] == 'touches':
            P['lost'].append({'key': f"LOST:{x['id']}", 'from': x['side'], 'to': OTHER[x['side']], 'claim': x['text']})
            ask(f"LOST:{x['id']}", 'about of the suspension: what was set down and how far its reach was limited', x['text'], optional=True)
    # --- first crack (attribute empty), generation (talk 1)
    if not save['coordinate'].get('attribute'):
        cr = [x['u'] for x in rows if x['kind'] == 'crack']
        if cr:
            P['first_crack'] = cr
            u0 = min(cr)
            ask('FIRST_CRACK', f'NONE, or: u{u0} | type (' + '/'.join(TYPES) + ') | first line text (the configuration that must not obtain: no name of either - the other, oneself; no scene; not the means). The first line is derived from the first crack in the log\'s order; NONE where no line passing the gate can be stated from it',
                'cracks named: ' + ', '.join(f'u{u}' for u in sorted(cr)) + f' | the first: u{u0}')
        else:
            P['notes'].append('first crack: none named - attribute and line stay empty')
    elif any(x['kind'] == 'crack' for x in rows):
        P['notes'].append('crack rows: attribute is already written - they are read by nothing')
    if talk1:
        ask('AXIS', 'direct_indirect=N; active_passive=N; rational_emotional=N; goal_relationship=N (1-10, from the Utsuwa)', '')
        ask('PARTNER_NAME', 'the name the resident Utsuwa gives this partner, transcribed', '')
    # --- the line: a contour drawn (a refusal kept again, with a crack) or sunk (what the partner stood on, yielded with a crack); one contour drawn at a close, every yielding sunk
    contours = save['coordinate']['line']
    line_at_open = bool(contours)
    lr, at_u, drawn_from, n_new = [x for x in rows if x['kind'] in ('line', 'yield')], {}, None, 0
    for x in lr:
        if x['u'] in at_u: stop(f"{x['where']}: u{x['u']} already has a line or yield row ({at_u[x['u']]['where']}) - one crack, one row: put every entry that held it at u{x['u']} in one row's ref")
        at_u[x['u']] = x
    for x in sorted(lr, key=lambda x: x['u']):
        if x['kind'] == 'line':
            on = [se for se in S if x['u'] in se['us'] and not se['withdrawn'] and se['from'] != 'sight']
            if not on: stop(f"{x['where']}: a line rises from a settlement, and the refusal at u{x['u']} is not the claim, the answer or the point of any settlement in this table")
            if x['how'] == 'keeps':
                P['notes'].append(f"line u{x['u']}: a boundary standing already keeps it - no line is drawn, the settlement is read as any other"); continue
        else:
            at = [x['u']] + x['to']
            on = [se for se in S if any(t in se['us'] for t in at) and not se['withdrawn'] and se['from'] in ('claim', 'promotion') and se['side'] == 'user']
            seen = [se for se in S if any(t in se['us'] for t in at) and se['from'] == 'sight' and se['side'] == 'user']
            for t in x['to']:
                if not any(t in se['us'] for se in on + seen): stop(f"{x['where']}: to u{t} is not the utterance of a claim of the user's settled in this table, nor of a sight of the user's")
                if t >= x['u'] and not any(t in se['us'] for se in seen): stop(f"{x['where']}: to u{t} does not stand before the yielding utterance (u{x['u']}) - only a sight may follow it")
            if not on and not seen: stop(f"{x['where']}: what is yielded is yielded to the user, and neither a settlement of a user's claim nor a sight of the user's in this table stands at u{x['u']} - name the claim or the sight, and write its utterance in to")
        if not line_at_open:
            P['notes'].append(f"{x['kind']} u{x['u']}: no line stood when this talk opened - the line does not move at this close (a first line written here is its only line); read as any other settlement"); continue
        if x['kind'] == 'line':
            if drawn_from is not None:
                P['notes'].append(f"line u{x['u']}: a contour is already drawn at this close (u{drawn_from}) - one at a close; read as any other settlement"); continue
            drawn_from = x['u']
        new = len(contours) + n_new
        if x['kind'] == 'line' or x['contour'] is None: n_new += 1
        if x['kind'] == 'line':
            key = f"SET:{on[0]['id']}:LINE"
            P['lines'].append({'key': key, 'u': x['u'], 'holders': x['holders'], 'settlements': [se['id'] for se in on], 'yield': False, 'contour': None, 'new': new})
            ask(key, f'new boundary (a new contour, E{new}): the configuration the refusal keeps from obtaining, in words of the refusal and of an entry that held it (no name of either - the other, oneself; no scene; not the means)',
                f"refusal u{x['u']} | held by: " + ' / '.join(f"{h} {E[h]['text']}" for h in x['holders']))
        else:
            key = f"YIELD:{x['id']}"
            k = x['contour']
            P['lines'].append({'key': key, 'u': x['u'], 'holders': x['holders'], 'settlements': [se['id'] for se in on], 'yield': True, 'contour': k, 'new': new if k is None else k})
            ask(key, ('the boundary that stands now | the form yielded (each a configuration: no name of either - the other, oneself; no scene; not the means by which it obtained); or NONE' if k is None else
                      f'the boundary that stands now (a configuration: no name of either - the other, oneself; no scene; not the means; the boundary of E{k} sinks beneath it as it stands); or NONE'),
                f"yielded at u{x['u']}" + (' to ' + ', '.join(f'u{t}' for t in x['to']) if x['to'] else '') + ' | ' +
                (f"a new contour, E{new}" if k is None else f"contour E{k}: {contours[k][0]}") +
                (' | held by: ' + ' / '.join(f"{h} {E[h]['text']}" for h in x['holders']) if x['holders'] else ''))
        for se in on: se['line'] = key
    # --- the settlements, per side
    for se in S:
        k = f"SET:{se['id']}"
        if se['from'] == 'sight':
            se['route'] = 'sight'; continue
        if se['withdrawn']:
            se['route'] = 'withdrawn'
            P['notes'].append(f'{k}: withdrawn by the issuing side alone - nothing written'); continue
        se['route'] = 'line' if se.get('line') else 'element'
        sides = (se['side'],) if se['from'] == 'departure' else ('partner', 'user')
        if se['from'] == 'claim' and not se['later']:
            sides = ()
            P['notes'].append(f'{k}: a claim of this talk alone (no later) - it settles no way to keep, and no arrangement is asked')
        for side in sides:
            note = ''
            if se['from'] == 'departure': note = '; leave the condition empty: the entry keeps its own'
            if side == 'partner' and se.get('line'): note += f"; used only if {se['line']} moves no line at this close"
            if se.get('check'): note += f"; used only if {se['check']} is met"
            ask(f'{k}:{side}', 'ONGOING | field | condition text | conduct text | destination (empty / held:<ref> / replaces:<ref> ...), or leave it out'
                + (' (' + note[2:] + ')' if note else ''), se['ctx'])
    # --- step 1 values
    uf = save['user_coordinate'].get('user_facts') or {}
    ask('FILE_NAME', 'partner_name written in Latin letters (romanized), for the save file name', save.get('partner_name', ''))
    ask('NOW', "now: the observable state the partner's utterances of this talk leave standing at its end (empty only where the partner did not speak)", '', optional=True)
    ask('USER_FACTS', 'user_facts updates as key=value; key=value (empty if none). A fact of a kind already keyed takes that key. A fact names no occasion: what was done or what happened on a day of this talk is not one',
        ('keys standing: ' + ', '.join(uf)) if uf else 'no key standing yet', optional=True)
    ask('PARTING_1', 'the earlier of the two last utterances: speaker (partner/user) | text verbatim (a line break written as \\n)', '')
    ask('PARTING_2', 'the later of the two last utterances, same form' + (' (both spoke: write it)' if P['both_spoke'] else ''), '', optional=True)
    ask('UNREADABLE', 'parts of the log that could not be read (empty if the talk was read whole; anything here stamps phase open)', '', optional=True)
    P['entries'] = E
    P['asked'] = [x['key'] for x in fill]; P['tool'] = VERSION
    P['inputs'] = {'opened': md5(opened_p)} | {n: md5(f'{wd}/{n}') for n in TABLES}
    P['planned_at'] = datetime.datetime.now(datetime.timezone.utc).timestamp()
    json.dump(P, open(f'{wd}/02_plan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    write_tsv(f'{wd}/02_questions.tsv', ['key', 'what', 'context'], [[x['key'], x['what'], x['context']] for x in fill])
    ent = [[e['ref'], e['text']] for e in E.values()]
    ent += [[f'R{j}', f"{r.get('from')} -> {r.get('to')}: {r.get('claim')}" + (f" | about: {r['about']}" if r.get('about') else '')] for j, r in enumerate(res)]
    ent += [[f'E{k}[{i}]', t] for k, kk in enumerate(save['coordinate']['line']) for i, t in enumerate(kk)]
    write_tsv(f'{wd}/02_entries.tsv', ['ref', 'text'], ent)
    print(f"{VERSION} plan | rows {len(rows)} | questions {len(fill)} | settlements {len(S)} | write 02_answers.tsv (entries to name: 02_entries.tsv)")
    for n in P['notes']: print(' ', n)

# ---------- build ----------
DEST = re.compile(r'(held|replaces):')
def destination(s, where):
    """'' | held:<ref> | replaces:<ref> <ref> (both may stand)."""
    held, rep, mode = None, [], None
    for tok in s.split():
        m = DEST.match(tok)
        if m: mode, tok = m.group(1), tok[m.end():]
        if not tok: continue
        if mode is None: stop(f"{where}: destination '{s}' - write held:<ref> or replaces:<ref> <ref>")
        if mode == 'held':
            if held: stop(f'{where}: one entry holds an arrangement (held: names one)')
            held = tok
        else: rep.append(tok)
    return held, rep

def build(opened_p, wd):
    save0 = json.load(open(opened_p, encoding='utf-8')); s = copy.deepcopy(save0)
    if not os.path.exists(f'{wd}/02_plan.json'): stop('02_plan.json is missing: run plan first')
    P = json.load(open(f'{wd}/02_plan.json', encoding='utf-8'))
    if P.get('tool') != VERSION: stop(f"02_plan.json was made by {P.get('tool')}, this tool is {VERSION}: run plan again with this tool")
    now_in = {'opened': md5(opened_p)} | {n: md5(f'{wd}/{n}') for n in TABLES}
    changed = [n for n in now_in if now_in[n] != P.get('inputs', {}).get(n)]
    if changed: stop(f"{', '.join(changed)} changed since plan: run plan again")
    def _times():   # development record only: when each work file was last written, in the runner's own folder
        ts = [(n, os.path.getmtime(f'{wd}/{n}')) for n in TABLES if os.path.exists(f'{wd}/{n}')]
        if 'planned_at' in P: ts.append(('plan', P['planned_at']))
        if os.path.exists(f'{wd}/02_answers.tsv'): ts.append(('02_answers.tsv', os.path.getmtime(f'{wd}/02_answers.tsv')))
        ts.append(('build', datetime.datetime.now(datetime.timezone.utc).timestamp()))
        ts.sort(key=lambda x: x[1]); t0 = ts[0][1]
        return ' | '.join(f"{n} {datetime.datetime.fromtimestamp(v, datetime.timezone.utc).strftime('%H:%M:%S')}Z (+{int(v - t0)}s)" for n, v in ts)
    if DEV: print(f'{VERSION} build', file=sys.stderr)
    if DEV: print(f'{VERSION} times: {_times()}', file=sys.stderr)
    asked = P['asked']
    SIDE = re.compile(r'SET:.+:(partner|user)$')
    A = {}
    for n, r in read_tsv(f'{wd}/02_answers.tsv', required=False, header=['key', 'answer']):
        k = (r.get('key') or '').strip()
        if k not in asked: stop(f'02_answers.tsv line {n}: answer to a key that was not asked: {k}')
        if k in A: stop(f'{k} answered twice')
        v = r.get('answer') or ''
        A[k] = v if k.startswith('PARTING_') else v.strip()   # parting words are copied verbatim
    for k in asked: A.setdefault(k, '')
    opt = set(P['optional'])
    missing = [k for k in asked if not A[k].strip() and k not in opt and not SIDE.match(k)]
    if missing: stop(f'unanswered: {missing}')
    check = {}
    for k in asked:
        if k.startswith('CHECK:'):
            v = A[k].lower()
            if v not in ('met', 'open'): stop(f'{k}: write met or open')
            check[k] = v
    E = P['entries']
    coord = lambda side: s['coordinate'] if side == 'partner' else s['user_coordinate']
    cur = [dict(e) for e in E.values()]
    # step 1: generation (talk 1), now, user_facts, first crack
    if P['talk1']:
        ax = {}
        for kv in filter(None, [x.strip() for x in A['AXIS'].split(';')]):
            k, eq, v = kv.partition('=')
            if not eq: stop(f"AXIS: '{kv}' is not key=N")
            ax[k.strip()] = v.strip()
        if set(ax) != set(AXES): stop(f"AXIS: write exactly {', '.join(AXES)}")
        if not all(re.fullmatch(r'\d+', ax[k]) and 1 <= int(ax[k]) <= 10 for k in AXES): stop('AXIS: every score is a whole number from 1 to 10')
        s['coordinate']['axis'] = {k: int(ax[k]) for k in AXES}
        s['partner_name'] = A['PARTNER_NAME']
    s['coordinate']['now'] = A['NOW']
    for kv in filter(None, [x.strip() for x in A['USER_FACTS'].split(';')]):
        k, eq, v = kv.partition('=')
        if not eq or not k.strip(): stop(f"USER_FACTS: '{kv}' is not key=value (a value holding ';' cannot be written in one line)")
        s['user_coordinate']['user_facts'][k.strip()] = v.strip()
    if P['first_crack'] and A.get('FIRST_CRACK', '').upper() != 'NONE':
        fc = [x.strip() for x in A['FIRST_CRACK'].split('|')]
        cu, typ, ltext = (fc + [''] * 3)[:3]
        if len(fc) > 3: stop('FIRST_CRACK: crack u | type | first line text')
        if not re.fullmatch(r'u?\d+', cu) or int(cu.lstrip('u')) not in P['first_crack']:
            stop(f"FIRST_CRACK: '{cu}' is not one of the cracks named ({', '.join(f'u{u}' for u in P['first_crack'])})")
        if int(cu.lstrip('u')) != min(P['first_crack']):
            stop(f"FIRST_CRACK: the first line is derived from the first crack in the log's order, u{min(P['first_crack'])} (not {cu}); write NONE where no line passing the gate can be stated from it")
        if typ not in TYPES: stop(f"FIRST_CRACK: type '{typ}' is not one of {', '.join(TYPES)}")
        if not ltext: stop('FIRST_CRACK: write the first line')
        s['coordinate']['attribute'] = typ           # attribute and the first line together, or neither
        s['coordinate']['line'] = [[ltext]]
    line_step1 = bool(s['coordinate']['line'])
    # step 3: settlements, in the log's order
    lines = {l['key']: l for l in P['lines']}
    drawn = set()
    def move_line(l):                                              # a contour drawn, or sunk
        if not A[l['key']]: stop(f"{l['key']}: the line moves here at this close - write the new boundary")
        if l['yield']:
            yp = [p.strip() for p in A[l['key']].split('|')]
            if len(yp) > 2: stop(f"{l['key']}: two parts at most - the boundary that stands now | the form yielded")
            new_b, form = (yp + [''])[:2]
            if not new_b: stop(f"{l['key']}: write the boundary that stands now")
            if l['contour'] is None:
                if not form: stop(f"{l['key']}: write the form yielded (the second part): it sinks beneath the new boundary")
                s['coordinate']['line'].append([new_b, form])          # a new contour: the Utsuwa's form sinks beneath its boundary
            else:
                if form: stop(f"{l['key']}: leave the second part empty - the boundary of E{l['contour']} sinks as it stands")
                s['coordinate']['line'][l['contour']].insert(0, new_b)  # the boundary yielded sinks, unrewritten
        else:
            s['coordinate']['line'].append([A[l['key']]])              # a new contour beside those standing: nothing sinks
        for h in l['holders']:                                     # every entry that held it is struck
            e = next((x for x in cur if x['ref'] == h), None)
            if e: cur.remove(e); coord('partner')[e['field']].remove(e['text'])
        drawn.add(l['key'])
    by_id = {se['id']: se for se in P['settlements']}
    for l in P['lines']:                                           # in the log's order, before the settlements: each contour stands where its question said
        if not s['coordinate']['line']: continue
        if l['yield'] and A[l['key']].upper() == 'NONE': continue  # no boundary can be stated: nothing is yielded
        on = [by_id[i] for i in l['settlements']]
        if on and all(se.get('check') and check[se['check']] == 'open' for se in on): continue      # only taken up: the claim stays open
        move_line(l)
    credited = set()
    written_promotion = 0
    S = P['settlements']
    for n in sorted(range(len(S)), key=lambda n: (S[n]['at'], n)):
        se = S[n]
        k = f"SET:{se['id']}"
        if se['route'] == 'withdrawn': continue
        if se['route'] == 'sight':
            key = f"SIGHT:{se['id']}"
            parts = [x.strip() for x in A[key].split('|')]
            if len(parts) > 3: stop(f'{key}: three parts at most - condition text | way of seeing | destination')
            ctext, view, dest = (parts + [''] * 3)[:3]
            if not view: stop(f'{key}: write the way of seeing')
            side, field = se['side'], 'what_is_visible'
            text = f'{ctext} -> {view}' if ctext else view
            held, rep = destination(dest, key)
            for ref in rep + ([held] if held else []):
                if ref not in E: stop(f"{key}: '{ref}' is not an entry of the opened save")
            invert(cur, coord, side, field, rep)
            if held: absorb(cur, side, field, held); continue
            if any(x['side'] == side and x['field'] == field and x['text'] == text for x in cur): continue
            unknown(cur, coord, side, field, text, f'new:{key}')
            continue
        if se.get('check') and check[se['check']] == 'open': continue      # only taken up: the claim stays open (residue below)
        wrote = line_here = False
        if se.get('line') and s['coordinate']['line']:
            l = lines[se['line']]
            line_here = l['key'] in drawn
            if line_here and l['key'] not in credited: credited.add(l['key']); wrote = True
        sides = (se['side'],) if se['from'] == 'departure' else ('partner', 'user')
        for side in sides:
            if side == 'partner' and line_here: continue
            key = f'{k}:{side}'
            parts = [x.strip() for x in A.get(key, '').split('|')]
            if parts[0].upper() in ('', 'SINGLE'): continue
            if parts[0].upper() != 'ONGOING': stop(f"{key}: write ONGOING | field | condition text | conduct text | destination, or leave it out")
            if len(parts) > 5: stop(f'{key}: five parts at most - ONGOING | field | condition text | conduct text | destination')
            _, field, ctext, conduct, dest = (parts + [''] * 5)[:5]
            if field not in FIELDS: stop(f"{key}: field '{field}' is not one of {', '.join(FIELDS)}")
            if field == 'what_is_visible': stop(f'{key}: what_is_visible is written by a sight alone (a sight row and SIGHT:), never by a settlement')
            if not conduct: stop(f'{key}: ONGOING needs the conduct')
            if se['from'] == 'departure':
                if ctext: stop(f"{key}: leave the condition empty - a departure keeps the condition of the entry it departed from")
                ctext = se['cond_text']
            text = f'{ctext} -> {conduct}' if ctext else conduct
            held, rep = destination(dest, key)
            if held and re.fullmatch(r'E\d+', held):                 # a boundary standing holds it: nothing is written
                if side != 'partner': stop(f"{key}: the line is the partner's; {held} holds nothing of the user's")
                planned = {l['new']: l['key'] for l in P['lines'] if l['contour'] is None}
                if int(held[1:]) in planned:
                    if planned[int(held[1:])] not in drawn: stop(f"{key}: named as held by {held}, but that contour was not drawn at this close - write the arrangement, or hold it by an entry")
                elif int(held[1:]) >= len(save0['coordinate']['line']): stop(f"{key}: no contour {held} stands, and none is drawn at this close")
                invert(cur, coord, side, field, rep)
                continue
            if se['from'] == 'departure':
                if held == se['replaces']: stop(f"{key}: {held} is the entry departed from; it is replaced, not holding")
                if se['replaces'] not in rep and any(x['ref'] == se['replaces'] for x in cur): rep.append(se['replaces'])
            for ref in rep + ([held] if held else []):
                if ref not in E: stop(f"{key}: '{ref}' is not an entry of the opened save")
            invert(cur, coord, side, field, rep)
            if held: absorb(cur, side, field, held); continue
            if any(x['side'] == side and x['field'] == field and x['text'] == text for x in cur): continue   # written once already: the same words
            unknown(cur, coord, side, field, text, f'new:{key}'); wrote = True
        if wrote and se['from'] == 'promotion': written_promotion += 1
    # residue: settled out, settled in part, issued (an answer only taken up keeps its claim open), suspended
    reword, about_new, fresh, left_open = {}, {}, [], 0
    for mt in P['matters']:
        order = lambda z: (z['u'], z['n'])
        members = [c for c in mt['members'] if not c['only_if'] or check[c['only_if']] == 'open']
        left_open += len(members) + len(mt['again'])
        for a in mt['again']: reword[a['j']] = a['text']
        if mt['target'] is not None:
            last = sorted(members + [a for a in mt['again'] if a['j'] == mt['target']], key=order)[-1]
            reword[mt['target']] = last['text']
            if A.get(mt['key'], '').strip(): about_new[mt['target']] = A[mt['key']]
        elif members:
            fresh.append({'from': mt['side'], 'to': OTHER[mt['side']], 'claim': members[-1]['text'], 'about': A.get(mt['key'], '')})
    if P.get('no_matter') and left_open > 1 and A.get('MATTERS', '').strip().upper() != 'NONE':
        stop(f'MATTERS: {left_open} claims are left open and the table has no matter row - write NONE, or add the matter rows to 01_events.tsv and run plan again')
    for j, text in reword.items():
        s['residue'][j] = dict(s['residue'][j], claim=text, **({'about': about_new[j]} if j in about_new else {}))
    rm = set(P['residue_rm'])
    for j, about in P['residue_part'].items():
        s['residue'][int(j)] = dict(s['residue'][int(j)], about=about)
    s['residue'] = [r for i, r in enumerate(s['residue']) if i not in rm]
    issued = 0
    for fr in fresh:
        s['residue'].append(fr)
        issued += 1
    if P['lost'] and not line_step1: print(f"{VERSION}: suspensions named touching a boundary standing, but no line stands - nothing sent to residue", file=sys.stderr)
    if line_step1:
        for lo in P['lost']:
            s['residue'].append({'from': lo['from'], 'to': lo['to'], 'claim': lo['claim'], 'about': A.get(lo['key'], '')}); issued += 1
    # parting words (verbatim, written by the runner), talk_number, phase
    pw = []
    for key in ('PARTING_1', 'PARTING_2'):
        v = A.get(key, '')
        if not v.strip(): continue
        sp, bar, text = v.partition('|')
        sp = sp.strip()
        if text.startswith(' '): text = text[1:]          # the separator is ' | ': only it is taken off, the text stays as written
        if sp not in ('partner', 'user') or not bar or not text.strip(): stop(f'{key}: speaker | text')
        pw.append({'speaker': sp, 'text': text.replace('\\n', '\n')})
    if len({x['speaker'] for x in pw}) != len(pw): stop('parting_words: one per speaker')
    if P['both_spoke'] and len(pw) < 2: stop('parting_words: both spoke in this talk - write PARTING_1 and PARTING_2')
    if any(x['speaker'] == 'partner' for x in pw) and not A['NOW'].strip(): stop('NOW: the partner spoke in this talk - write now')
    s['parting_words'] = pw
    s['talk_number'] = save0['talk_number'] + 1
    s['phase'] = 'open' if A['UNREADABLE'] else 'closed'
    name = re.sub(r'[^A-Za-z0-9]', '', A['FILE_NAME'])
    if not name: stop('FILE_NAME: partner_name in Latin letters is needed (nothing of it is Latin)')
    out = f"{wd}/Save_talk{s['talk_number']:03d}_{name}.json"
    json.dump(s, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    def count(side, fn):
        a, b = (save0['coordinate'], s['coordinate']) if side == 'partner' else (save0['user_coordinate'], s['user_coordinate'])
        return sum(1 for f in FIELDS for e in (b[f] if fn == 'added' else a[f]) if e not in (a[f] if fn == 'added' else b[f]))
    rep = [P['rows'], count('partner', 'struck') + count('user', 'struck'), count('partner', 'added'), count('user', 'added'),
           sum(1 for k in s['coordinate']['line'] for e in k if e not in [x for kk in save0['coordinate']['line'] for x in kk]), issued,
           len(P['residue_rm']) + len(P['residue_part']), written_promotion]
    print(out)
    if DEV: print('\n'.join(map(str, rep)))   # development record: not part of the close

if __name__ == '__main__':
    if len(sys.argv) < 2: stop('usage: Talk_Close.py guide | core | version | plan <opened save> <work folder> | build <opened save> <work folder>')
    cmd, *args = sys.argv[1:]
    if cmd == 'guide': print(__doc__)
    elif cmd == 'core': print(CORE_CLOSE)
    elif cmd == 'version': print(VERSION)
    elif cmd in ('plan', 'build') and len(args) == 2: {'plan': plan, 'build': build}[cmd](*args)
    else: stop('usage: Talk_Close.py guide | core | version | plan <opened save> <work folder> | build <opened save> <work folder>')
