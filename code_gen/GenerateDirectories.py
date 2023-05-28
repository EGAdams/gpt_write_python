import os

class GenerateDirectories:
    def __init__(self, base_directory):
        self.base_directory = base_directory

    def validate_directory_name(self, directory_name):
        # Check if directory name is not empty
        if not directory_name:
            return False
        # Check if directory name contains invalid characters
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        if any(char in directory_name for char in invalid_chars):
            return False
        # Check if directory already exists
        if os.path.exists(os.path.join(self.base_directory, directory_name)):
            print( "directory already exists, nothing to do..." )
            return True
        return True

    def create_directory(self, directory_name):
        if self.validate_directory_name(directory_name):
            os.makedirs(os.path.join(self.base_directory, directory_name), exist_ok=True)
            return f"Directory '{directory_name}' created successfully."
        else:
            return f"Failed to create directory '{directory_name}'. Invalid directory name or directory already exists."
    
    def list_directories(self):
        return [d for d in os.listdir(self.base_directory) if os.path.isdir(os.path.join(self.base_directory, d))]

# Test the class

# if main
if __name__ == "__main__":
    base_dir = 'code_gen'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    gd = GenerateDirectories(base_dir)
    print(gd.create_directory('test_dir'))
    print(gd.list_directories())