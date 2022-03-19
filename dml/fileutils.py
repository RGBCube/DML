import typing as t

from .encoder import encode, decode
from .errors import DecodeError
from .symbols import symbols as s

__all__ = ("decode_file", "encode_file")


def encode_file(fp: str, *, out: str = None) -> t.Optional[t.Generator[str, None, None]]:
    """Encodes a file to DML.

    Arguments:
        fp (str): The filepath to the file to encode.
        out (str): The filepath to write the encoded file to. If not specified, the encoded text will be returned as a generator.

    Returns:
        Optional[Generator[str, None, None]]: The encoded text as a generator.
    """

    def read_file() -> t.Generator[str, None, None]:
        with open(fp) as f_:
            while char_ := f_.read(1):
                yield char_

    if out:
        out = out + ".dml" if not out.endswith(".dml") else out
        with open(out, "w") as f:
            for char in encode(read_file()):
                f.write(char)
    else:
        return encode(read_file())


def decode_file(fp: str, *, out: str = None) -> t.Optional[t.Generator[str, None, None]]:
    """Decodes a file that has DML encoded in it.

    Arguments:
         fp (str): The filepath to the file to decode.
         out (str): The filepath to write the decoded file to. If not specified, the decoded text will be returned as a generator.

    Returns:
        Optional[Generator[str, None, None]]: The decoded text as a generator.

    Raises:
        DecodeError: If the file is not valid DML.
    """

    def read_file() -> t.Generator[str, None, None]:
        buffer = ""
        with open(fp) as f_:
            while char_ := f_.read(1):
                if char_ not in s.values():
                    raise DecodeError(f"Invalid character: '{char_}', expected {s['1']}, {s['0']} or {s['stop']}")
                elif char_ != s["stop"]:
                    buffer += char_
                else:
                    yield buffer + s["stop"]
                    buffer = ""

    if out:
        out = out + ".dml" if not out.endswith(".dml") else out
        with open(out, "w") as f:
            for char in decode(read_file()):
                f.write(char)
    else:
        return decode(read_file())
