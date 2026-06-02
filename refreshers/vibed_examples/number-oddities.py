"""
Python Number Oddities for C-like Programmers
=============================================
Pointed examples of how Python differs from Java, Kotlin, C/C++, and JavaScript.
"""

# =============================================================================
# 1. DIVISION: True Division vs Floor Division
# =============================================================================
# In C/Java/Kotlin: 7 / 2 == 3 (integer division truncates)
# In Python 3: / always returns a float

print("=== Division ===")
print(f"7 / 2 = {7 / 2}")        # 3.5 (NOT 3 like in Java!)
print(f"7 // 2 = {7 // 2}")      # 3 (floor division - use this for integer division)
print(f"-7 // 2 = {-7 // 2}")    # -4 (floors toward negative infinity, NOT -3!)

# Compare to Java/C: -7 / 2 == -3 (truncates toward zero)


# =============================================================================
# 2. EXPONENTIATION OPERATOR
# =============================================================================
# C/Java/Kotlin: Math.pow(2, 10) or pow(2, 10)
# Python: ** operator built-in

print("\n=== Exponentiation ===")
print(f"2 ** 10 = {2 ** 10}")    # 1024
print(f"2 ** 0.5 = {2 ** 0.5}")  # 1.414... (square root)
print(f"(-1) ** 0.5 = {(-1) ** 0.5}")  # (6.123...e-17+1j) - returns complex!


# =============================================================================
# 3. NO INTEGER OVERFLOW
# =============================================================================
# C/Java/Kotlin: int overflows at 2^31-1, long at 2^63-1
# Python: integers have arbitrary precision

print("\n=== Arbitrary Precision Integers ===")
big = 2 ** 100
print(f"2 ** 100 = {big}")
print(f"Type: {type(big)}")  # Still just 'int', not a special BigInteger class

# This would overflow in Java:
java_max_long = 9223372036854775807
print(f"Java max long + 1 = {java_max_long + 1}")  # Works fine in Python


# =============================================================================
# 4. MODULO WITH NEGATIVE NUMBERS
# =============================================================================
# Python's modulo ALWAYS returns same sign as divisor (mathematical modulo)
# C/Java: sign of remainder matches dividend

print("\n=== Modulo with Negatives ===")
print(f"-7 % 3 = {-7 % 3}")      # 2 (Python) vs -1 (Java/C)
print(f"7 % -3 = {7 % -3}")      # -2 (Python) vs 1 (Java/C)
print(f"-7 % -3 = {-7 % -3}")    # -1 (both agree here)


# =============================================================================
# 5. NO ++ OR -- OPERATORS
# =============================================================================
# C/Java/Kotlin/JS: i++ or ++i
# Python: doesn't exist!

print("\n=== Increment/Decrement ===")
i = 5
# i++  # SyntaxError!
# ++i  # Parses but does nothing (unary + applied twice)
i += 1  # This is the Python way
print(f"i after += 1: {i}")

# Gotcha: ++i parses as +(+i) = i, not an increment!
j = 5
result = ++j  # This is legal but useless
print(f"++j where j=5: {result}")  # Still 5!


# =============================================================================
# 6. CHAINED COMPARISONS
# =============================================================================
# C/Java: (x > 5 && x < 10)
# Python: can chain naturally

print("\n=== Chained Comparisons ===")
x = 7
print(f"5 < {x} < 10: {5 < x < 10}")  # True - reads like math!
print(f"1 < 2 < 3 < 4: {1 < 2 < 3 < 4}")  # True

# This is NOT the same as (1 < 2) < 3 in C!
# In C: (1 < 2) evaluates to 1, then 1 < 3 is true
# Python actually checks 1 < 2 AND 2 < 3


# =============================================================================
# 7. BOOLEAN OPERATORS: and/or/not vs &&/||/!
# =============================================================================
# Python uses words, not symbols

print("\n=== Boolean Operators ===")
a, b = True, False
print(f"True and False: {a and b}")   # not &&
print(f"True or False: {a or b}")     # not ||
print(f"not True: {not a}")           # not !

# and/or return actual values, not just True/False!
print(f"0 or 'default': {0 or 'default'}")      # 'default'
print(f"'hello' and 'world': {'hello' and 'world'}")  # 'world'
print(f"'' or 'fallback': {'' or 'fallback'}")  # 'fallback'


# =============================================================================
# 8. TRUTHY/FALSY VALUES
# =============================================================================
# Python's falsy: False, None, 0, 0.0, '', [], {}, set()
# Different from JS where [] and {} are truthy!

print("\n=== Truthy/Falsy ===")
print(f"bool([]): {bool([])}")        # False (empty list)
print(f"bool([0]): {bool([0])}")      # True (non-empty, even with falsy element)
print(f"bool(''): {bool('')}")        # False
print(f"bool(' '): {bool(' ')}")      # True (space is a character!)
print(f"bool(0.0): {bool(0.0)}")      # False


# =============================================================================
# 9. DIVMOD - QUOTIENT AND REMAINDER IN ONE
# =============================================================================
# No direct equivalent in C/Java (though Kotlin has destructuring)

print("\n=== divmod ===")
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5) = ({quotient}, {remainder})")  # (3, 2)


# =============================================================================
# 10. WALRUS OPERATOR := (Assignment Expression)
# =============================================================================
# Python 3.8+: assign and use in one expression
# Similar to = in C conditionals, but explicit

print("\n=== Walrus Operator ===")
numbers = [1, 2, 3, 4, 5]
# Instead of:
#   n = len(numbers)
#   if n > 3:
# You can write:
if (n := len(numbers)) > 3:
    print(f"List has {n} elements, which is more than 3")


# =============================================================================
# 11. BITWISE OPERATORS ARE THE SAME (mostly)
# =============================================================================
# &, |, ^, ~, <<, >> work the same

print("\n=== Bitwise (familiar) ===")
print(f"5 & 3 = {5 & 3}")   # 1
print(f"5 | 3 = {5 | 3}")   # 7
print(f"5 ^ 3 = {5 ^ 3}")   # 6
print(f"5 << 1 = {5 << 1}") # 10
print(f"5 >> 1 = {5 >> 1}") # 2

# BUT: ~ on arbitrary precision ints works differently conceptually
# ~x == -(x+1), not a fixed-width bit flip
print(f"~5 = {~5}")  # -6 (mathematically -(5+1))


# =============================================================================
# 12. NO TERNARY ? : OPERATOR
# =============================================================================
# C/Java: condition ? if_true : if_false
# Python: if_true if condition else if_false

print("\n=== Ternary Expression ===")
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Order is different! Value first, then condition, then else value


# =============================================================================
# 13. MULTIPLE ASSIGNMENT & SWAP
# =============================================================================
# Python can assign multiple values simultaneously

print("\n=== Multiple Assignment ===")
a, b = 1, 2
print(f"a={a}, b={b}")

# Swap without temp variable
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Unpacking
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")  # first=1, rest=[2, 3, 4, 5]


# =============================================================================
# 14. NUMERIC LITERALS
# =============================================================================
print("\n=== Numeric Literals ===")
binary = 0b1010      # Same as C/Java
octal = 0o17         # 0o prefix, not just 0 like C!
hexadecimal = 0xFF   # Same as C/Java
big_num = 1_000_000  # Underscores for readability (Java 7+, Python 3.6+)

print(f"0b1010 = {binary}")
print(f"0o17 = {octal}")
print(f"0xFF = {hexadecimal}")
print(f"1_000_000 = {big_num}")

# Complex numbers built-in!
c = 3 + 4j
print(f"Complex: {c}, magnitude: {abs(c)}")  # 5.0


# =============================================================================
# 15. TYPE COERCION IS STRICTER
# =============================================================================
print("\n=== Type Strictness ===")
# Python won't automatically convert between string and number
# "5" + 3  # TypeError!
print(f"int('5') + 3 = {int('5') + 3}")
print(f"'5' + str(3) = {'5' + str(3)}")

# But numeric types do coerce
print(f"5 + 3.0 = {5 + 3.0}")  # 8.0 (int promoted to float)
print(f"True + 5 = {True + 5}")  # 6 (bool is subclass of int!)


# =============================================================================
# SUMMARY TABLE
# =============================================================================
"""
| Operation          | C/Java/Kotlin      | Python              |
|--------------------|--------------------|--------------------|
| Integer division   | 7 / 2 → 3          | 7 // 2 → 3         |
| True division      | 7.0 / 2.0 → 3.5    | 7 / 2 → 3.5        |
| Exponent           | Math.pow(2, 10)    | 2 ** 10            |
| Negative modulo    | -7 % 3 → -1        | -7 % 3 → 2         |
| Increment          | i++                | i += 1             |
| Boolean AND        | &&                 | and                |
| Boolean OR         | ||                 | or                 |
| Boolean NOT        | !                  | not                |
| Ternary            | c ? a : b          | a if c else b      |
| Octal literal      | 017                | 0o17               |
"""

if __name__ == "__main__":
    print("\n✓ All examples executed successfully!")
