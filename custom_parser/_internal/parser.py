from tokenizer import extract
from resolver import resolve_nested

def parse(self, text: str):
    tokens = extract(self, text)
    result = ""

    for typ, val in tokens:
        if typ == "text":
            result += val

        elif typ == "var":

            if "|" in val:

                val, default = val.split("|", 1)

            else:

                default = None

            if "." in val:

                base, path = val.split(".", 1)

            else:

                base, path = val, None

            if base in self.rules:

                value = self.rules[base]()

                if path:
                    value = resolve_nested(value, path)

                result += str(
                    value if value is not None else default or "{" + val + "}"
                )

            else:

                result += str(default) if default is not None else "{" + val + "}"

    return result