# Expressions
# regexes

regexes is just a pattern it's quite common in programming to want to use pattern to match on some kind of data, often user input. For example if user types in email or password, whether to your program, or a website, or an app on your phone. And you want to validate that they did indeed type in an email address and not something completely different.

# re library

its called succinctly R-E. its for define and check for and even replace patterns, like pattern for an email address, and then use some built-in function to actually validate a user's inout against that pattern or even use these patterns to change user's inputs or extract partial information.

'docs.python.org/3library/re.html'

specials symbols:

    . any character except a newline
    * 0 or more repetitions
    + 1 or more repetitions
    ? 0 or 1 repettition
    {m} m repetitions # be it 1, or 2, or 3, or 300
    {m, n} m-n repetitions # if you want few repetitions or this many characters...
    ^ matches the start of the string
    $ matches the end of the string or just before the new line at the end of the string.
    [] set of characters
    [^] complementing the set
    \d decimal digit
    \D not a decimal digit
    \s whitespace characters
    \S not a whitespace character
    \w word character .. as well as numbers and the underscore
    \W not a word character
    re.IGNORECASE
    re.MULTILINE
    re.DOTALL
    A|B either A or B
    (...) a group
    (?:...) non-capturing version