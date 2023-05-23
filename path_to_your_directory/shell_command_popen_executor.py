class ShellCommandPopenExecutor:
    @command(
        "execute_shell_popen",
        "Execute Shell Command, non-interactive commands only",
        '"command_line": "<command_line>"',
        CFG.execute_local_commands,
        "You are not allowed to run local shell commands. To execute"
        " shell commands, EXECUTE_LOCAL_COMMANDS must be set to 'True' "
        "in your config. Do not attempt to bypass the restriction.",
    )
    def execute_shell_popen(self, command_line) -> str:
        """Execute a shell command with Popen and returns an english description
        of the event and the process id

        Args:
            command_line (str): The command line to execute

        Returns:
            str: Description of the fact that the process started and its id
        """
        validator = CommandValidator()
        if not validator.validate_command(command_line):
            logger.info(f"Command '{command_line}' not allowed")
            return "Error: This Shell Command is not allowed."

        current_dir = os.getcwd()
        # Change dir into workspace if necessary
        if CFG.workspace_path not in current_dir:
            os.chdir(CFG.workspace_path)

        logger.info(
            f"Executing command '{command_line}' in working directory '{os.getcwd()}'"
        )

        do_not_show_output = subprocess.DEVNULL
        process = subprocess.Popen(
            command_line, shell=True, stdout=do_not_show_output, stderr=do_not_show_output
        )

        # Change back to whatever the prior working dir was

        os.chdir(current_dir)

        return f"Subprocess started with PID:'{str(process.pid)}'"