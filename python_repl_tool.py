import os
from typing import Dict,Optional
from base_tool import BaseTool
from python_repl import PythonREPL

class PythonREPLTool(BaseTool):
    """A tool for running python code in a REPL."""

    name = "Python REPL"
    description = (
        "A Python shell. Use this to execute python commands. "
        "Input should be a valid python command. "
        "If you want to see the output of a value, you should print it out "
        "with `print(...)`."
    )
    python_repl: PythonREPL = PythonREPL()
    sanitize_input: bool = True

    def _run(self, query: str) -> str:
        """Use the tool."""
        if self.sanitize_input:
            query = query.strip().strip("```")
            print( "query", query )
            output = self.python_repl.run(query)
            print ( "output", output )
        return self.python_repl.run(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("PythonReplTool does not support async")