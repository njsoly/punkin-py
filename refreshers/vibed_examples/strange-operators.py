"""
Python Strange Operators for C-like Programmers
================================================
Operators and syntactic quirks that have no clean equivalent in
Java / Kotlin / C / JavaScript (or behave very differently).
"""


# =============================================================================
# 1. THE "REST" / SPLAT OPERATOR  *  (in assignments)
# =============================================================================
# In assignment targets, a single * makes that name "absorb" the leftovers.
# PEP 3132, "Extended Iterable Unpacking".

print("=== * in assignment (rest) ===")

first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")            # rest is a list

*head, last = [1, 2, 3, 4, 5]
print(f"head={head}, last={last}")

a, *mid, z = "abcdef"                            # works on any iterable
print(f"a={a}, mid={mid}, z={z}")                # mid is a list of chars

# The starred name always becomes a list, even if it captures zero items:
x, *nothing, y = [1, 2]
print(f"x={x}, nothing={nothing}, y={y}")        # nothing=[]


# =============================================================================
# 2. * AND ** IN FUNCTION CALLS  (spread)
# =============================================================================
# Same symbol, different role: "spread" a sequence/mapping into args.
# Closest analog: JS  f(...arr)  and  {...obj}.

print("\n=== * and ** in calls (spread) ===")

def describe(name, age, role):
    return f"{name}, {age}, {role}"

args  = ["Alice", 30, "engineer"]
kwargs = {"name": "Bob", "age": 25, "role": "designer"}

print(describe(*args))                           # spreads list -> positional
print(describe(**kwargs))                        # spreads dict -> keyword

# Same in literals:
merged_list = [0, *args, 99]
merged_dict = {"team": "A", **kwargs}
print(merged_list)
print(merged_dict)


# =============================================================================
# 3. * AND ** IN FUNCTION DEFINITIONS  (varargs / kwargs)
# =============================================================================
# Collecting side: turns extra args into a tuple / dict.

print("\n=== *args / **kwargs (collect) ===")

def log(level, *args, **kwargs):
    print(f"[{level}] args={args} kwargs={kwargs}")

log("INFO", "starting", "service", retries=3, timeout=10)
# args is a TUPLE here (not a list, unlike the assignment case above)


# =============================================================================
# 4. POSITIONAL-ONLY  /  AND KEYWORD-ONLY  *  IN SIGNATURES
# =============================================================================
# Bare / and * inside a parameter list are MARKERS, not parameters.
#   everything BEFORE  /  must be passed positionally
#   everything AFTER   *  must be passed by keyword

print("\n=== / and * as signature markers ===")

def f(pos_only, /, normal, *, kw_only):
    return pos_only, normal, kw_only

print(f(1, 2, kw_only=3))
print(f(1, normal=2, kw_only=3))
# f(pos_only=1, normal=2, kw_only=3)  # TypeError: pos_only is positional-only
# f(1, 2, 3)                          # TypeError: kw_only must be keyword


# =============================================================================
# 5. THE WALRUS OPERATOR  :=  ("alligator")
# =============================================================================
# Assignment expression (PEP 572, Python 3.8+).
# Assigns AND returns the value, so you can bind a name inside an expression.

print("\n=== Walrus := ===")

# Classic use: read-and-test in a loop condition
import io
stream = io.StringIO("one\ntwo\nthree\n")
while (line := stream.readline()):
    print(f"got: {line.strip()}")

# Avoids computing something twice:
data = [1, 2, 3, 4, 5, 6, 7]
if (n := len(data)) > 5:
    print(f"list is long: {n} items")

# Useful in comprehensions to cache a function call:
def expensive(x): return x * x
filtered = [y for x in range(6) if (y := expensive(x)) > 5]
print(filtered)


# =============================================================================
# 6. ELLIPSIS  ...
# =============================================================================
# Yes, "..." is a real singleton object named `Ellipsis`. Three uses:

print("\n=== Ellipsis ... ===")

# (a) Placeholder body, like Kotlin's TODO():
def not_implemented_yet():
    ...                                          # equivalent to `pass`

# (b) Common in type stubs / Protocols
from typing import Callable
handler: Callable[[int], str] = lambda x: str(x)

# (c) Real index meaning in numpy: arr[..., 0]  -> "all leading axes"
print(... is Ellipsis)                           # True


# =============================================================================
# 7. CHAINED COMPARISONS
# =============================================================================
# Reads like math. NOT the same as (a < b) & (b < c) in C.

print("\n=== Chained comparisons ===")

x = 5
print(1 < x < 10)                                # True
print(1 < x < 10 < 100)                          # True, all neighbors compared
print(10 > x > 1 == 1)                           # works with mixed operators

# Gotcha: this is NOT comparing 'a' to 'c'
a, b, c = 1, 5, 1
print(a == b == c)                               # False
print(a < b > c)                                 # True (1<5 and 5>1), looks weird


# =============================================================================
# 8. CONDITIONAL EXPRESSION (ternary)  x if cond else y
# =============================================================================
# Order is "value-condition-value", not "condition ? a : b".

print("\n=== Ternary ===")

age = 20
label = "adult" if age >= 18 else "minor"
print(label)


# =============================================================================
# 9. SLICE SYNTAX  a[start:stop:step]
# =============================================================================
# The third colon (step) and negative values are the surprising parts.

print("\n=== Slices ===")

s = "abcdefgh"
print(s[::2])                                    # "aceg"  every 2nd
print(s[::-1])                                   # "hgfedcba"  reversed
print(s[1:-1])                                   # "bcdefg"  trim ends
print(s[::-2])                                   # "hfdb"

# Slices are objects too:
sl = slice(1, None, 2)
print(s[sl])                                     # "bdfh"


# =============================================================================
# 10. f-STRING DEBUG  =
# =============================================================================
# f"{expr=}" prints both the expression text and its value. (Python 3.8+)

print("\n=== f-string debug = ===")

total = 7 * 6
print(f"{total=}")                               # total=42
name = "Nick"
print(f"{name.upper()=}")                        # name.upper()='NICK'


# =============================================================================
# 11. UNDERSCORE  _  CONVENTIONS
# =============================================================================
# Not an operator, but it surprises newcomers.

print("\n=== Underscore _ ===")

# (a) "I don't care about this value":
for _ in range(3):
    print("tick")

# (b) Numeric literal separator (3.6+):
big = 1_000_000_000
print(big)

# (c) In the REPL, `_` is the last expression's result.
# (d) Convention: _name is "internal", __name triggers name-mangling in classes.


# =============================================================================
# 12. THE  @  OPERATOR  (matrix multiply, and decorators)
# =============================================================================
# Two unrelated uses of @:

print("\n=== @ ===")

# (a) Decorator syntax (familiar from Flask/pytest):
def shout(fn):
    def wrapper(*a, **kw):
        return fn(*a, **kw).upper()
    return wrapper

@shout
def greet(name): return f"hello, {name}"
print(greet("world"))

# (b) Binary matmul operator (PEP 465). Built-in types don't implement it,
#     but numpy does:  A @ B  ==  A.dot(B).
# Any class can define __matmul__ to give @ a meaning.


# =============================================================================
# 13. BITWISE  |  ON DICTS AND SETS (and types!)
# =============================================================================
# | is bitwise-or for ints, set-union for sets, dict-merge for dicts (3.9+),
# and a type-union in annotations (3.10+).

print("\n=== | overloads ===")

print({1, 2} | {2, 3})                           # {1, 2, 3}
print({"a": 1} | {"b": 2, "a": 99})              # right side wins -> {'a':99,'b':2}

def takes(x: int | str) -> None:                 # same as Union[int, str]
    print(type(x).__name__, x)
takes(1); takes("hi")


# =============================================================================
# 14. is  vs  ==   (identity vs equality)
# =============================================================================
# `is` checks "same object in memory". Almost always you want ==.

print("\n=== is vs == ===")

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)                            # True False

# Tiny ints and short strings are CACHED, so `is` may "accidentally" work:
print(256 is 256, 257 is 257)                    # True, often False (impl detail!)
# Only legitimate uses of `is`:  x is None,  x is True/False,  sentinel checks.


# =============================================================================
# 15. ELSE ON LOOPS AND TRY
# =============================================================================
# Yes, `for`/`while`/`try` can have an `else` clause. It runs if the loop
# completed WITHOUT `break` (or the try block did not raise).

print("\n=== for/else ===")

for n in [1, 2, 3]:
    if n == 99:
        print("found")
        break
else:
    print("not found")                           # runs because no break


# =============================================================================
# 16. PRINT-AS-EXPRESSION pitfalls:  ,  AND  ;
# =============================================================================
# A trailing comma in an expression makes a TUPLE. Bites people often.

print("\n=== trailing comma tuple ===")

x = 1,                                           # x is (1,) not 1
print(x, type(x).__name__)

# Semicolons exist (statement separator) but are non-idiomatic:
a = 1; b = 2; print(a + b)
