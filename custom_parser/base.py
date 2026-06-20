from ._internal import parser


class CustomParser:
    def __init__(self):
        self.things = {}
        self.rules = {}
        self.define("{", "}")

    def define(self, start_token: str, end_token: str):
        self.things["start"] = start_token
        self.things["end"] = end_token

    def rule(self, name: str, func):
        self.rules[name] = func

    def parse(self, text):
        return parser.parse(self=self, text=text)