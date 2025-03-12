import magic
import filetype

def detect_file_type(file_path):
    kind = filetype.guess(file_path)
    if kind:
        return kind.extension
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)
