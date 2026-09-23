#!/usr/bin/env python3
"""PreToolUse reminder: nudge Claude to apply the activity-naming convention
whenever a Bash command creates or updates a workout on intervals.icu.

Non-blocking. Emits additionalContext only when the command looks like a
workout push (push.py, or the intervals.icu events API); otherwise exits
silently so it never interferes with unrelated Bash calls.
"""
import json
import re
import sys

# Patterns that indicate a workout is being created/updated.
PUSH_PATTERNS = (
    r"push\.py",
    r"intervals\.icu/api/v1/athlete/[^/\s]+/events",
)

REMINDER = (
    "This command creates or updates a workout on intervals.icu. Before proceeding, "
    "make sure every workout title follows the activity-naming convention "
    "(skill: activity-naming): correct session-type label, lowercase 'x', '@ %FTP' "
    "intensity, fixed values only, and 'VO2 Max' spelled with a letter O (never "
    "'VO2max' or a zero). Load the activity-naming skill first if it is not already active."
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # Never block on malformed input.

    command = (payload.get("tool_input") or {}).get("command", "") or ""
    if not any(re.search(p, command) for p in PUSH_PATTERNS):
        return 0

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": REMINDER,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
