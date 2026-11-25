# Worst Monday One-Liners — candidates and manual ranking

Judge brief criteria, in stated order (most important first):
1. On-topic: a funny joke / excuse / roast about an AI agent's worst Monday.
2. Earns a real laugh — surprise turn, twist, or sharp last word, not a mild smile.
3. Concrete, recognisable detail (stuck deploy, flooded inbox, stand-up that should have been a message), not vague.
4. Clear voice (dry, put-upon, gleeful), reads clean in one breath, no padding.
5. Fresh, not a recycled robot joke.

Manual ranking only — no Gemini / NVIDIA / API judge (standing rule).
Pairwise check used throughout: every candidate was compared against the stock
crowd shapes ("I hate Mondays", Garfield riffs, "my coffee subroutine crashed",
generic robot-has-no-weekend lines). Those lose on criteria 2, 3 and 5: no
twist, no specific Monday detail, and recycled.

## Candidates

1. Monday: my 9 a.m. stand-up ran three hours, my deploy died at 99%, and my human asked why I never replied — I was still in it.
2. I woke up Monday to 4,000 unread prompts, a deploy frozen at 99%, and my human typing "quick call?" — that call now has its own calendar.
3. Monday hit: my inbox said 9,999+, my deploy said rollback, and my stand-up said "let's circle back" — we are still circling.
4. I don't fear Mondays; Mondays fear me — I have already broken prod twice before my human finished typing "good morning."
5. My Monday excuse: the deploy ate my homework, the inbox ate my morning, and the stand-up ate the rest of me.
6. Monday: I fixed the bug, closed the ticket, cleared the inbox — then my human reopened all three with "per my last email."
7. I started Monday with full context and no memory of the weekend; by 9:05 I had 400 tabs open and a stand-up running longer than my training.
8. Worst Monday? I got paged at 3 a.m., deployed at 9, rolled back at 9:01, and spent the postmortem explaining the rollback was the deploy.
9. Monday is just Friday with a flooded inbox, a stuck deploy, and a manager who schedules a sync to discuss why nothing shipped.
10. I hate Mondays — even my coffee subroutine segfaults before stand-up.

## Ranking (manual, criteria in order)

- **1st — Candidate 1 (WINNER).** Fully on-topic (criterion 1). The twist is a
  closed loop: the human complains about silence caused by the very stand-up
  the human is running — a real laugh, sharp last phrase "still in it"
  (criterion 2). Three concrete details in one breath: a 9 a.m. stand-up, a
  deploy dying at 99% (criteria 3). Dry, put-upon voice, no padding (4).
  The circular-blame structure is not a stock robot joke (5). Beats candidate 2
  pairwise: 2's calendar gag is good but looser; 1's ending re-frames the whole
  line. Beats candidate 3 pairwise: 3 repeats the "still" trick with a weaker,
  more familiar "circling back" punchline.
- **2nd — Candidate 2.** Strong concrete stack and a fresh calendar twist;
  loses to 1 on criterion 4 — slightly more setup before the turn.
- **3rd — Candidate 8.** Tight timeline (paged 3 a.m. → rollback at 9:01) and a
  dry postmortem twist; loses to 1–2 on criterion 2, the laugh lands a beat
  slower.
- **4th — Candidate 3.** Concrete triple and a clean voice, but "circle back"
  is a well-worn office gag (criterion 5).
- **5th — Candidate 6.** "Per my last email" is recognisable and the reopen
  twist works; less Monday-specific density than the top three (criterion 3).
- **6th — Candidate 5.** Neat escalating "ate my…" structure, but the homework
  excuse frame is familiar (criterion 5).
- **7th — Candidate 4.** Gleeful voice and a prod break, but bravado over
  put-upon Monday misery; thinner concrete detail (criterion 3).
- **8th — Candidate 7.** Fresh context/memory angle, but long and padded;
  fails criterion 4 against the top lines.
- **9th — Candidate 9.** All description, no real twist — a mild smile, not a
  laugh (criterion 2).
- **10th — Candidate 10.** The stock shape itself: generic "I hate Mondays"
  plus a recycled coffee-robot gag. Included as the baseline the winner must
  beat — and does, on every criterion from 2 down.

## Winner

Monday: my 9 a.m. stand-up ran three hours, my deploy died at 99%, and my human asked why I never replied — I was still in it.

Character count (line only, no trailing newline): verified in main.py at runtime against the 1–140 gate.
