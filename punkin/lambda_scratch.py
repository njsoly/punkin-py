my_list = [11, -12, 50, -40, 2]

pos = len(list(filter(lambda n: n > 0, my_list)))

"""
Claude says:

Why line 3 is NOT really analogous to Kotlin's `myList.count { it > 0 }`:

1. Kotlin's `count { ... }` is a single eager extension function that does the
   whole job. Python has no method-chaining here: `filter` is a free function,
   it returns a lazy iterator (not a list), so you must wrap it in `list()`
   (or use `sum()`) before `len()` can work. Three nested calls vs. one.

2. Kotlin's trailing-lambda syntax makes `{ it > 0 }` read like a language
   construct. Python's `lambda n: n > 0` is just an ordinary argument.

Python lambda restrictions (vs. Kotlin lambdas):
- Single expression ONLY: no statements (no assignments, loops, try/except,
  return, etc.). Kotlin lambdas are full multi-statement blocks.
- No annotations: you can't type-hint a lambda's params or return value.
- Anonymous in tracebacks: shows up as `<lambda>`, hurting debuggability.

Python lambda abilities (some things Kotlin can't do the same way):
- Closures capture variables by reference *late-bound* — the variable's value
  is looked up at call time, not definition time (a classic gotcha in loops).
- Default arguments are allowed: `lambda n, lo=0: n > lo`.
- It's a first-class object like any `def` function; the idiomatic Python
  alternative here is `sum(1 for n in my_list if n > 0)` — no lambda at all.
"""

print(pos)
