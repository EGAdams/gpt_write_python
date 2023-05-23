class ShellCommandExecutor:
    @command(
        "execute_shell",
        "Execute Shell Command, non-interactive commands only",
        '"command_line": "<command_line>"',
        CFG.execute_local_commands,
        "You are not allowed to run local shell commands. To execute"
        " shell commands, EXECUTE_LOCAL_COMMANDS must be set to 'True' "
        "in your config file: .env - do not attempt to bypass the restriction.",
    )
    def execute_shell(self, command_line: str) -> str:
        """Execute a shell command and return the output

        Args:
            command_line (str): The command line to execute

        Returns:
            str: The output of the command
        """
        validator = CommandValidator()
        if not validator.validate_command(command_line):
            logger.info(f"Command '{command_line}' not allowed")
            return "Error: This Shell Command is not allowed."

        current_dir = Path.cwd()
        # Change dir into workspace if necessary
        if not current_dir.is_relative_to(CFG.workspace_path):
            os.chdir(CFG.workspace_path)

        logger.info(
            f"Executing command '{command_line}' in working directory '{os.getcwd()}'"
        )

        result = subprocess.run(command_line, capture_output=True, shell=True)
        output = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

        # Change back to whatever the prior working dir was

        os.chdir(current_dir)
        return output