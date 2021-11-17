import os


def get_transcripts(files_dir):
    all_files = []
    for root, dirs, files in os.walk(files_dir):
        for file in files:
            if file.endswith('.pdf'):
                all_files.append(file)
    print(all_files)
    return all_files
