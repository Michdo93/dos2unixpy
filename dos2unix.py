import os
import argparse

def convert_to_unix(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            content = file.read()
        with open(file_path, 'w', newline='\n', encoding='utf-8') as file:
            file.write(content)
        print(f"Datei {file_path} erfolgreich konvertiert.")
    except Exception as e:
        print(f"Fehler beim Konvertieren der Datei {file_path}: {e}")

def process_files_in_directory(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            convert_to_unix(file_path)

def main():
    parser = argparse.ArgumentParser(description='Konvertiert Dateien in einem Verzeichnis zu Unix-Zeilenumbrüchen.')
    parser.add_argument('--path', required=True, help='Der Pfad zum Verzeichnis mit den Dateien.')
    parser.add_argument('--extension', required=False, help='Die Dateiendung/Dateierweiterung der Dateien.')

    args = parser.parse_args()
    path = args.path
    extension = args.extension

    if extension and "." not in extension:
        extension = "." + extension

    process_files_in_directory(path, extension)

if __name__ == "__main__":
    main()
