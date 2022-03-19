import typing as t

from .errors import DecodeError
from .symbols import symbols as s

__all__ = ("encode", "decode")


def encode(text: t.Union[t.Generator, t.List[str], str], *, out: str = None) -> t.Optional[t.Generator[str, None, None]]:
    """Encodes text into Dotted Markup Language (DML)

    Arguments:
        text (Union[Generator, List[str], str]): The text to encode.
        out (str): The filepath to write the encoded file to. If not specified, the encoded text will be returned as a generator.

    Returns:
        Optional[Generator[str, None, None]]: The encoded text as a generator.
    """

    def inner() -> t.Generator[str, None, None]:
        for char_ in text:
            yield format(ord(char_), "b").replace("0", s["0"]).replace("1", s["1"]) + s["stop"]

    if out:
        out = out + ".dml" if not out.endswith(".dml") else out
        with open(out, "w") as f:
            for char in inner():
                f.write(char)
    else:
        return inner()


def decode(text: t.Union[t.Generator, t.List[str], str], *, out: str = None) -> t.Optional[t.Generator[str, None, None]]:
    """Decodes text from Dotted Markup Language (DML)

    Arguments:
        text (Union[Generator, List[str], str]): The text to decode.
        out (str): The filepath to write the decoded file to. If not specified, the decoded text will be returned as a generator.

    Returns:
        Optional[Generator[str, None, None]]: The decoded text as a generator.

    Raises:
        DecodeError: If the text is not valid DML.
    """

    def inner() -> t.Generator[str, None, None]:
        nonlocal text
        if isinstance(text, str):
            text = [e + s["stop"] for e in text.split(s["stop"]) if e]
        for char_ in text:
            if any(e not in s.values() for e in char_):
                raise DecodeError(f"Invalid character: '{char_}', expected {s['1']}, {s['0']} or {s['stop']}")
            yield chr(int(char_[:-1].replace(s['0'], "0").replace(s['1'], "1"), 2))

    if out:
        with open(out, "w") as f:
            for char in inner():
                f.write(char)
    else:
        return inner()
