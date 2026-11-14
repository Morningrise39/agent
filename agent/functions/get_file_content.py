from config import MAX_CHARS
import os
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            raise Exception(f'Cannot list "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file):
            raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
        with open(target_file, "r") as file:
            data = file.read(MAX_CHARS)
            if file.read(1):
                data += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return data
    except Exception as e:
        print(f"Error: {e}")

