# CustomParser

🚀 Create custom parsers without writing tokenizers, path resolvers, and parsing logic from scratch.

CustomParser turns hundreds of lines of parsing code into a simple, extensible API.

---

## Features

✅ Custom delimiters

```python
c.define("[VAR]", "[/VAR]")
```

✅ Variables

```text
[VAR]user[/VAR]
```

✅ Nested object access

```text
[VAR]user.name[/VAR]
```

✅ List indexing

```text
[VAR]user.skills[0][/VAR]
```

✅ List slicing

```text
[VAR]user.skills[0:2][/VAR]
```

✅ Mapping over slices

```text
[VAR]user.skills[0:2].name[/VAR]
```

✅ Default values

```text
[VAR]user.nickname|Unknown[/VAR]
```

✅ Custom rules

```python
c.rule("user", lambda: {...})
```

---

# Installation

> This is still not published on PyPI, but you can clone it on GitHub:
```bash
git clone https://github.com/youssefahmed2017/custom-parser
```

---

# Quick Start

```python
from custom_parser import CustomParser

c = CustomParser()

c.define("[VAR]", "[/VAR]")

c.rule("user", lambda: {
    "name": "Youssef",
    "age": 9,
    "skills": ["coding", "drawing"]
})

print(
    c.parse(
        "Hello [VAR]user.name[/VAR]! "
        "You are [VAR]user.age[/VAR] years old."
    )
)
```

Output:

```text
Hello Youssef! You are 9 years old.
```

---

# Nested Paths

CustomParser supports nested dictionary access.

```python
c.rule("user", lambda: {
    "profile": {
        "name": "Youssef"
    }
})

print(c.parse(
    "Hello [VAR]user.profile.name[/VAR]"
))
```

Output:

```text
Hello Youssef
```

---

# List Indexing

```python
c.rule("user", lambda: {
    "skills": [
        "coding",
        "drawing"
    ]
})

print(c.parse(
    "[VAR]user.skills[0][/VAR]"
))
```

Output:

```text
coding
```

---

# List Slicing

```python
c.rule("user", lambda: {
    "skills": [
        "coding",
        "drawing",
        "gaming"
    ]
})

print(c.parse(
    "[VAR]user.skills[0:2][/VAR]"
))
```

Output:

```python
['coding', 'drawing']
```

---

# Mapping Over Lists

```python
c.rule("user", lambda: {
    "items": [
        {"name": "Sword"},
        {"name": "Shield"},
        {"name": "Potion"}
    ]
})

print(
    c.parse(
        "[VAR]user.items[0:2].name[/VAR]"
    )
)
```

Output:

```python
['Sword', 'Shield']
```

---

# Default Values

Provide a fallback if a variable doesn't exist.

```python
print(
    c.parse(
        "Nickname: [VAR]user.nickname|Unknown[/VAR]"
    )
)
```

Output:

```text
Nickname: Unknown
```

---

# Custom Delimiters

You are not limited to `[VAR]` tags.

## Curly Braces

```python
c.define("{", "}")

print(
    c.parse(
        "Hello {user.name}"
    )
)
```

## Double Braces

```python
c.define("{{", "}}")

print(
    c.parse(
        "Hello {{user.name}}"
    )
)
```

## Custom Syntax

```python
c.define("<%", "%>")

print(
    c.parse(
        "Hello <%user.name%>"
    )
)
```

---

# Registering Rules

Rules are the source of data used by the parser.

```python
c.rule(
    "time",
    lambda: "12:00"
)

c.rule(
    "user",
    lambda: {
        "name": "Youssef"
    }
)
```

Usage:

```text
[VAR]time[/VAR]
[VAR]user.name[/VAR]
```

---

# Example

```python
from custom_parser import CustomParser

c = CustomParser()

c.define("[VAR]", "[/VAR]")

c.rule("user", lambda: {
    "name": "Youssef",
    "age": 9,
    "skills": [
        "coding",
        "drawing"
    ]
})

template = """
Hello [VAR]user.name[/VAR]!

Age: [VAR]user.age[/VAR]

Skills:
- [VAR]user.skills[0][/VAR]
- [VAR]user.skills[1][/VAR]
"""

print(c.parse(template))
```

Output:

```text
Hello Youssef!

Age: 9

Skills:
- coding
- drawing
```

---

# Why CustomParser?

Without CustomParser, you would need to build:

- A tokenizer
- A parser
- A path resolver
- List indexing logic
- Slice handling
- Variable replacement logic
- Default value handling

CustomParser provides all of that behind a simple API.

---

# Project Structure

```text
custom_parser/
├── __init__.py
├── base.py
└── _internal/
    ├── parser.py
    ├── resolver.py
    └── tokenizer.py
```

---

# License

MIT License

---

Made with ☕ and too many hours spent debugging tokenizers.
