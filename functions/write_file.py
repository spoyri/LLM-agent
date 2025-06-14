import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_dir, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error writing to file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'