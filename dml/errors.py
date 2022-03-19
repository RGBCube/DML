__all__ = ("DottedMarkupLanguageException", "DecodeError")


class DottedMarkupLanguageException(Exception):
    """Base class for all exceptions in this module."""
    pass


class DecodeError(DottedMarkupLanguageException):
    """Raised when there is an error decoding a string."""
    pass
