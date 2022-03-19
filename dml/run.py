from .encoder import decode
from .fileutils import decode_file

__all__ = ("run_file", "run")


def run(dml: str) -> None:
    exec("".join(decode(dml)))


def run_file(fp: str) -> None:
    exec("".join(decode_file(fp)))
