# Expressions

Regex is a sequence of characters that forms a search pattern. It’s commonly used for tasks like validating inputs (email, phone numbers, etc.), searching for specific patterns in data, or modifying strings.

# regexes

regexes is just a pattern it's quite common in programming to want to use pattern to match on some kind of data, often user input. For example if user types in email or password, whether to your program, or a website, or an app on your phone. And you want to validate that they did indeed type in an email address and not something completely different.

# re library

its called succinctly R-E. its for define and check for and even replace patterns, like pattern for an email address, and then use some built-in function to actually validate a user's inout against that pattern or even use these patterns to change user's inputs or extract partial information.

'docs.python.org/3library/re.html'

# Special Symbols in Regex:

    .: Matches any character except a newline.
    *: Matches 0 or more repetitions of the preceding character.
    +: Matches 1 or more repetitions of the preceding character.
    ?: Matches 0 or 1 repetition of the preceding character.
    {m}: Matches exactly m repetitions of the preceding character.
    {m,n}: Matches between m and n repetitions of the preceding character.
    ^: Matches the start of a string.
    $: Matches the end of a string.
    []: Matches any character inside the brackets.
    [^]: Matches any character not in the brackets.
    \d: Matches any decimal digit.
    \D: Matches any non-digit character.
    \s: Matches any whitespace character (spaces, tabs, newlines).
    \S: Matches any non-whitespace character.
    \w: Matches any word character (letters, digits, underscore).
    \W: Matches any non-word character.
    A|B: Matches either A or B.
    (...): Defines a group for capturing.
    (?:...): Defines a non-capturing group.

# Flags:

    re.IGNORECASE: Makes the pattern case-insensitive.
    re.MULTILINE: Makes the ^ and $ anchors match the start and end of each line, not just the start and end of the string.
    re.DOTALL: Makes the dot . match newlines as well.

# re.search(pattern, string, flags=0)

re.search(pattern, string, flags=0): Scans through a string, looking for any location where the pattern matches.

```python
result = re.search(r'\d+', 'Order 123')
if result:
    print(result.group())  # Outputs: 123
```

# re.match(pattern, string, flags=0)#

re.match(pattern, string, flags=0): Checks for a match only at the beginning of the string.

```python
result = re.match(r'Order \d+', 'Order 123')
if result:
    print(result.group())  # Outputs: Order 123
```

# re.sub(pattern, string, count=0, flags=0)

re.sub(pattern, replacement, string, count=0, flags=0): Replaces occurrences of the pattern with a replacement string.

```python
result = re.sub(r'\d+', '###', 'Order 123')
print(result)  # Outputs: Order ###
```

# := valrus operator 

The walrus operator (:=) is a new Python feature introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression (in-line assignment), which can simplify your code, especially in conditional statements.

```python
if matches := re.search(r"^(.+), ?(.+)$", "Doe, John"):
    print(matches.groups())  # Outputs: ('Doe', 'John')
```

Here, matches is assigned the result of re.search(), and at the same time, we check if the result is truthy (i.e., if a match was found).

By using regex with the re library, you can create powerful tools for validating and transforming string data, making it an essential tool for text manipulation in programming.