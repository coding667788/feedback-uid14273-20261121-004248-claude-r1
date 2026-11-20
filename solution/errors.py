"""Structured error type carrying a locatable code and field position."""


class CaseError(Exception):
    """A structural or semantic problem in the input case.

    Attributes:
        code: machine readable error code, e.g. ``E_REF``.
        path: JSON-path-like field position, e.g. ``$.batches.B1.duration``.
        message: human readable explanation.
    """

    def __init__(self, code, path, message):
        super().__init__(f"{code} at {path}: {message}")
        self.code = code
        self.path = path
        self.message = message

    def to_dict(self):
        return {"code": self.code, "path": self.path, "message": self.message}
