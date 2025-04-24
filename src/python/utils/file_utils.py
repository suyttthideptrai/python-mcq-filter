

def get_file_content(file_path):
    """
    Read the content of a file and return it as a string.
    :param file_path: Path to the file to read.
    :return: Content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()