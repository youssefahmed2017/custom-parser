import re

def resolve_nested(value, path):
    parts = path.split(".")

    for part in parts:

        match = re.match(r"(\w+)\[(.+)\]$", part)

        if match:
            key = match.group(1)
            index = match.group(2)

            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None

            if isinstance(value, list):

                if ":" in index:
                    start, end = index.split(":", 1)
                    start = int(start) if start else None
                    end = int(end) if end else None
                    value = value[slice(start, end)]
                else:
                    i = int(index)
                    value = value[i] if 0 <= i < len(value) else None

            else:
                return None

        else:
            if isinstance(value, list):
                value = [
                    v.get(part) if isinstance(v, dict) else None
                    for v in value
                ]

            elif isinstance(value, dict) and part in value:
                value = value[part]

            else:
                return None

    return value