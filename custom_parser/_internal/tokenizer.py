def extract(self, text: str):
    tokens = []

    buffer = ""
    inside = False

    start_token = self.things["start"]
    end_token = self.things["end"]

    i = 0

    while i < len(text):

        if not inside and text.startswith(start_token, i):
            if buffer:
                tokens.append(("text", buffer))
                buffer = ""

            inside = True
            i += len(start_token)
            continue

        if inside and text.startswith(end_token, i):
            tokens.append(("var", buffer))
            buffer = ""

            inside = False
            i += len(end_token)
            continue

        buffer += text[i]
        i += 1

    if buffer:
        tokens.append(("text", buffer))

    return tokens