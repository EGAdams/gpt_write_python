class PythonREPL:
    """A class for running Python code in a REPL."""

    def __init__(self, _globals: Optional[Dict] = None, _locals: Optional[Dict] = None):
        self._globals = _globals if _globals is not None else {}
        self._locals = _locals if _locals is not None else {}

    def run(self, code: str) -> str:
        exec(code, self._globals, self._locals)
        return str(self._locals)