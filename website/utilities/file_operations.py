def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(rootdir, text):
    import os

    filename = "modified_transcription.txt"
    TMP_PATH = rootdir
    TMP_FOLDER = "tmp"
    path = os.path.join(TMP_PATH, TMP_FOLDER, filename)
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except:
            raise
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        raise

    return TMP_FOLDER, filename