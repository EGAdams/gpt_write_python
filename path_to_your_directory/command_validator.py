class CommandValidator:
    def validate_command(self, command: str) -> bool:
        """Validate a command to ensure it is allowed

        Args:
            command (str): The command to validate

        Returns:
            bool: True if the command is allowed, False otherwise
        """
        tokens = command.split()

        if not tokens:
            return False

        if CFG.deny_commands and tokens[0] not in CFG.deny_commands:
            return False

        for keyword in CFG.allow_commands:
            if keyword in tokens:
                return True
        if CFG.allow_commands:
            return False

        return True