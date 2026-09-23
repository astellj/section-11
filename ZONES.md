# Heart Rate Zones

_Last set: 2026-09-09 · Anchored to LTHR (Lactate Threshold Heart Rate)_

> **Revised 2026-09-09: LTHR 181 → 177.** The previous value was derived from a single effort
> that could not measure it. Deliberately conservative pending lactate testing later in 2026.
> See *Why LTHR was revised* below. **Every boundary moved down by 4 bpm.**

## Anchor values (cycling)

| Metric | Value | Source / confidence |
|--------|-------|---------------------|
| **LTHR** | **177 bpm** | Revised estimate, 2026-09-09. Plausible range 175–180. Derived from maximal-effort HR across the 42-day window (5 min @ 281 W → 188 bpm implies LTHR ~176–179) and cross-checked against max HR (177 = 90.8% of 195, within the normal 88–92% band). **Deliberately set at the conservative end.** Confirm with lactate testing or a 30-min TT. |
| **Max HR** | **195 bpm** | Highest observed ride HR = 192 (7HCC). VO2 sessions are leg-limited, not maximal, so the true ceiling is a touch higher. 220−26 = 194. 195 remains a solid working number. |
| **LT1 (aerobic threshold)** | **~150 bpm** | Estimate: ~85% LTHR. This is the true "zone 2 / fat-max" ceiling. Was ~155 under the old anchor. |
| FTP | 252 W | intervals.icu (eFTP ~240). Stale — tested 2026-05-12. |

These values are set in **intervals.icu (7-zone)**, **Garmin Connect (5-zone, custom bounds)**, and **Strava (5-zone, custom bounds)** so a prescribed workout zone means the same thing everywhere.

## Why LTHR was revised (2026-09-09)

The old value of 181 came from the 7HCC chaingang: 42 minutes at **216 W**, average HR 181, in warm conditions.

**216 W is roughly 90% of eFTP (240 W) — sweet spot, not threshold.** Averaging threshold-level heart rate at sub-threshold power for 42 minutes does not locate the threshold; it records cardiac drift. The original note already half-caught this, flagging "−5.5% decoupling at only sweet-spot power suggests some HR drift". Heat and the surging of a group chaingang are two further reasons for the HR to sit high relative to the actual work.

So 181 was not a bad auto-detection — it was a valid calculation applied to an effort that cannot measure LTHR.

**Supporting evidence for the lower value:**

| Check | Result |
|---|---|
| 5-min max (281 W → 188 bpm) | Maximal 5-min efforts run 102–107% of LTHR → implies **176–179** |
| 20-min "best" (230 W → 181 bpm) | Power *below* eFTP 240, so not a maximal effort — HR again drifted |
| % of max HR | 181 = 92.8% of 195, at the very top of the plausible band. 177 = 90.8%, mid-band |

**Why 177 and not lower:** 177 sits at the conservative end of the 175–180 range without over-correcting. Erring low is the safe direction — it lowers the Z2 ceiling, which protects easy rides from drifting into tempo. If the true value turns out to be 181 after all, nothing is lost: the aerobic adaptation lives at the *bottom* of Z2 regardless.

**To resolve properly:** lactate testing (planned later in 2026), or a 30-min solo TT on flat road in cool conditions with LTHR taken as the average HR of the final 20 minutes. Do not re-derive it from a group ride.

## 7-zone model (intervals.icu / Joe Friel)

intervals.icu's default HR zone system **is** the Friel model. Boundaries are fixed % of LTHR.

| Zone | Name | % LTHR | BPM | Was |
|------|------|--------|-----|-----|
| Z1 | Recovery | <81% | **< 143** | < 147 |
| **Z2** | **Endurance** | **81–89%** | **143–157** | 147–161 |
| Z3 | Tempo | 90–93% | **158–164** | 162–168 |
| Z4 | Threshold | 94–99% | **165–176** | 169–179 |
| Z5 | VO2max | 100–102% | **177–180** | 181–184 |
| Z6 | Anaerobic | 103–106% | **181–188** | 185–192 |
| Z7 | Neuromuscular | >106% | **189+** | 193+ |

## 5-zone model (Garmin / Strava)

Same boundaries as the 7-zone — Friel's Z5a/5b/5c are merged into one top zone. Enter these as **custom** bounds (do **not** use the platforms' default %-max-HR zones, which won't align).

| Zone | Name | BPM | Enter lower bound | Was |
|------|------|-----|-------------------|-----|
| Z1 | Recovery | < 143 | (min) | — |
| **Z2** | **Endurance** | **143–157** | **143** | 147 |
| Z3 | Tempo | 158–164 | **158** | 162 |
| Z4 | Threshold | 165–176 | **165** | 169 |
| Z5 | VO2 / Max | 177–195 | **177** | 181 |

## Executing a Zone 2 endurance ride

Aim for the **lower-to-middle of Z2 (~141–150)**, not the top. The band's ceiling (157) sits slightly **above** LT1 (~150), so riding the top of Z2 is already drifting past true aerobic pace. Use the talk test: full sentences, comfortable nasal breathing, RPE 3–4/10.

> **Practical cap: keep endurance rides at or below 150 bpm.** This holds at or under LT1 across the entire plausible LTHR range (175 → LT1 149; 181 → LT1 154), so it is the right number whether or not the revision is exactly correct.

## Why anchor to LTHR instead of max HR?

LTHR tracks a real physiological event (the threshold) and is measurable in the field; max HR is a ceiling you rarely touch and formulas for it carry ±10–12 bpm error. Anchoring both models to the same LTHR means **Zone 2 = 143–157 in every app** — a prescribed "Endurance / Zone 2" ride needs no translation between platforms.

## Why LT1 (~150) ≠ the top of Zone 2 (157)

A zone boundary and a physiological threshold are two different things:

- **Zone boundaries are arithmetic.** Friel's 7-zone system has exactly **one** physiological anchor — LTHR, which is your *second* threshold (LT2, ~threshold effort). Every other boundary is a fixed *percentage* of that anchor (81%, 89%, 90%…). The top of Z2 is simply "89% of LTHR = 157" — a line on a calculator, not a measured event in your body.
- **LT1 is biology.** Your *first* lactate threshold (aerobic threshold, where lactate first rises off baseline) is a real, separate physiological point. The Friel model never pins it — it only pins LT2/LTHR — so LT1 lands wherever your physiology puts it, which for most trained athletes is roughly **85% of LTHR**. For you that's ~150.
- **So they don't coincide by design.** LT1 (~150, ~85% LTHR) falls in the **upper-middle of Z2**, not at its top edge (~89% LTHR). The gap between ~150 and 157 is just the mismatch between a two-threshold physiology (LT1 *and* LT2) and a zone chart that only anchors one of them. That's exactly why "true zone 2 / fat-max" (below LT1) is the *lower* part of the labelled Z2 band, and why we target ~141–150 rather than riding to the 157 ceiling.

## Open

- [ ] **Lactate testing later in 2026** to pin LTHR properly and narrow the 175–180 range.
- [ ] Alternative if lactate testing slips: 30-min solo TT, flat, cool, LTHR = avg HR of final 20 min. Best done at the start of the winter block alongside the FTP retest, not during the hill climb block.
- [ ] Power zones are unaffected by this change — they key off FTP 252 W (also stale, eFTP ~240). Retest at winter block start.
- [ ] DFA a1 (alphaHRV) would give ongoing LT1/LT2 estimates with no testing, but requires the Connect IQ field to stay on a rendered data screen. **Declined 2026-09-09** — not worth reworking the data screens.
