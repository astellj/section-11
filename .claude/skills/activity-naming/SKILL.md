---
name: activity-naming
description: Naming convention for cycling activities and planned workouts on intervals.icu / Strava. Use whenever creating, renaming, planning, or pushing a workout title (e.g. via push.py or the intervals.icu events API) so titles follow the standard format.
---

# Activity Naming Convention

Standardised activity titles across intervals.icu, Strava, and other platforms.

## Title Format

```
[Session Type] (Sets x Duration @ %FTP)
```

- Use lowercase `x` (not ×) for easy mobile editing
- Include intensity as `@ %FTP` (e.g. `@ 112%`) — useful at a glance
- No raw wattages in the title — use % FTP; structure tells the rest
- Always use fixed values (no duration/intensity ranges)
- Keep concise where possible

## Session Types

Ordered easy → hard.

| Type | Label |
|------|-------|
| Active Recovery | `Recovery` |
| Easy ride with short sprints / on-bike activations | `Activations` |
| Zone 2 / Endurance | `Endurance` |
| Long ride | `Endurance` |
| Tempo | `Tempo` |
| Sweet Spot | `Sweet Spot` |
| Over-Unders | `Over-Unders` |
| Threshold | `Threshold` |
| VO2 Max | `VO2 Max` |
| Anaerobic capacity (30 s–3 min, >120% FTP) | `Anaerobic` |
| Mixed zones (wide range) | `Mixed Intervals` |
| Pre-ride off-bike activation (bands, mobility) | `Pre-Ride Activation` |

Note: `VO2 Max` uses the letter **O** (VO₂), spaced — never `VO2max` or a zero.

`VO2 Max` is for efforts of ~3–8 min at 106–120% FTP or 30/15-style sets, where time at ≥90% VO₂max is the point. Short supramaximal reps (30 s–3 min at >120% FTP, e.g. hill-climb reps, 3x90s sharpeners) are `Anaerobic` — they train W′, and the VO₂ exposure per rep is incidental.

## Unstructured Rides

The table above is prescribed work, ordered by intended intensity. These two labels sit off
that axis entirely — they mark rides where nothing was prescribed and the efforts were
decided by terrain, the group, or the mood on the day.

| Type | Label |
|------|-------|
| Unstructured ride, group-driven efforts | `Group Ride` |
| Unstructured ride, solo, no plan | `Free Ride` |

- Both take **no parenthetical**. There is no structure to encode, and whole-ride IF is not
  the same quantity as the `@ %FTP` work intensity used elsewhere — reusing that slot would
  make `Sweet Spot (3x12 @ 85%)` and `Group Ride (@ 88%)` look comparable when they are not.
- Use these only when efforts actually happened. A solo ride that genuinely stayed in Z2 is
  still `Endurance`; `Free Ride` is the flag for unplanned climbs, sprints, and surges.
- Do not reach for `Mixed Intervals` here — that label implies prescribed sets.
- Neither label carries load. These rides can be anything from a coffee spin to 90+ TSS at
  IF 0.88; read TSS/IF off intervals.icu rather than encoding it in the title.

Both mean: *don't read training intent into this one.*

## Sets Within Sets

Use parentheses: `3x(3x3)` — 3 sets of 3x3-minute intervals.

## Over/Under Splits

Use `/` to encode the over/under pair — two fixed levels, in both the duration and the intensity:
`2x(6x2/2) @ 105/93%` — 2 sets of 6 reps of (2min over / 2min under), at 105% over / 93% under.

## Examples

Each example covers a distinct case:

```
Title: Endurance                         # bare label, no structure
Title: VO2 Max (5x5 @ 112%)              # standard interval + intensity
Title: Over-Unders (2x(6x2/2) @ 105/93%) # sets within sets + over/under split
Title: Mixed Intervals 4 sets            # irregular structure
Title: Group Ride                        # unstructured, group-driven
Title: Free Ride                         # unstructured, solo
```

## Quick Reference Card

| Element | Rule |
|---------|------|
| Multiplication | lowercase `x` |
| Intensity | `% FTP` format, e.g. `@ 92%` |
| Sets within sets | parentheses `3x(3x3)` |
| Over/under split | slash `2/2`, `105/93%` (two fixed levels) |
| Wattages | never in title |
