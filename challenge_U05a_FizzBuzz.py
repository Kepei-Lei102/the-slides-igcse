"""
FizzBuzz  —  the Ice-Cream Challenge 🍦  (U5a)
----------------------------------------------
Print the numbers 1 to 100 — one per line — BUT:
  · multiples of 3 print   Fizz
  · multiples of 5 print   Buzz
  · multiples of both print FizzBuzz

Since 2007 this exact question has been used in real job interviews
to filter out programmers who cannot actually program. Today it
filters ice cream.

HOW TO WORK (this is Test-Driven Development — how real engineers build):
  1. Run this file NOW, before writing anything. Watch it fail. That's RED.
  2. Write a little code inside my_fizzbuzz() below.
  3. Run again. Read what the judge says — it tells you WHERE to look.
  4. Repeat until GREEN. Then bring the green run to class.
"""


def my_fizzbuzz():
    # Your code here. Delete this line when you start.
    pass


# ── Leave everything below alone — it is the judge. ──────────────────────
import io
import contextlib
import traceback


def _expected_line(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def _hint(n, exp, got):
    if got.lower() == exp.lower():
        return "Spelling right, CAPITALS wrong — interviewers care: Fizz, Buzz, FizzBuzz."
    if exp == "FizzBuzz" and got in ("Fizz", "Buzz"):
        return ("%d is a multiple of BOTH 3 and 5. Your checks run in order, top to\n"
                "     bottom — which one catches %d first? The 'both' test must come FIRST.\n"
                "     (Hint inside the hint: %d %% 15)" % (n, n, n))
    if exp in ("Fizz", "Buzz") and got == "FizzBuzz":
        return ("%d is a multiple of only ONE of 3 and 5, but your code shouted for both.\n"
                "     Check the test that decides 'both' — does it really require 3 AND 5?" % n)
    if exp in ("Fizz", "Buzz", "FizzBuzz") and got == str(n):
        which = "3" if exp == "Fizz" else ("5" if exp == "Buzz" else "3 and 5")
        return ("%d is a multiple of %s, but your code printed the number.\n"
                "     Remember U4: %% is the remainder. 'n %% 3 == 0' asks: does 3 divide n?" % (n, which))
    if exp == str(n) and got in ("Fizz", "Buzz", "FizzBuzz"):
        return ("%d is NOT a multiple of 3 or 5, but your code shouted anyway.\n"
                "     One of your tests is too eager — read each condition out loud." % n)
    return "Compare the two carefully — character by character."


def _judge():
    print("=" * 52)
    print("  FIZZBUZZ JUDGE — red, fix, run, green")
    print("=" * 52)

    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            my_fizzbuzz()
    except Exception as e:
        frames = [f for f in traceback.extract_tb(e.__traceback__) if f.name == "my_fizzbuzz"]
        where = ("on line %d of this file" % frames[-1].lineno) if frames else "in your code"
        print("❌ RED — your program crashed %s:" % where)
        print("     💥 %s: %s" % (type(e).__name__, e))
        print("\nFix the crash first, then run again.")
        return

    lines = [ln.rstrip() for ln in buf.getvalue().splitlines()]
    expected = [_expected_line(n) for n in range(1, 101)]

    if not lines:
        print("❌ RED — your program printed nothing at all.")
        print("     Have you deleted 'pass' and written your code inside my_fizzbuzz()?")
        print("     Karel rules apply: the code must live INSIDE the def block (indented).")
        return

    problems = 0

    if len(lines) != 100:
        problems += 1
        print("❌ Line count: expected 100 lines, you printed %d." % len(lines))
        if len(lines) == 99:
            print("     💡 Off by one! Remember: range(1, 101) — the end number is not included.")
        elif len(lines) == 101:
            print("     💡 One extra line — are you printing 0, or printing something after the loop?")
        print()

    for i, (exp, got) in enumerate(zip(expected, lines)):
        if got != exp:
            problems += 1
            n = i + 1
            print("❌ Your line %d is wrong:" % n)
            print("     expected: %s" % exp)
            print("     you got : %s" % got)
            print("  💡 " + _hint(n, exp, got))
            print()
            break  # one problem at a time — fix it, run again

    fizz = lines.count("Fizz")
    buzz = lines.count("Buzz")
    both = lines.count("FizzBuzz")

    if problems == 0:
        print("✅ GREEN — all 100 lines perfect!")
        print("   Scoreboard: Fizz 27 · Buzz 14 · FizzBuzz 6 — checksum matches.")
        print()
        print("🍦 Bring this green run to class. The ice cream is yours.")
        print("   (You just passed a real job-interview question. Remember this feeling.)")
    else:
        print("Scoreboard — a correct run: Fizz 27 · Buzz 14 · FizzBuzz 6")
        print("            your run     : Fizz %d · Buzz %d · FizzBuzz %d" % (fizz, buzz, both))
        print()
        print("One problem shown at a time. Fix it, run again. RED → fix → run → GREEN.")


# Leave this part alone — it starts the judge up.
if __name__ == "__main__":
    _judge()
