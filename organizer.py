import os
import shutil

def organize_file(source_dir):
    file_types = {
        ".pdf": "Documents",
        ".jpg": "Images",
        ".py": "Scripts"
    }

    for filename in os.listdir(source_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in file_types:
            target_dir = os.path.join(source_dir, file_types[file_ext])
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(
                os.path.join(source_dir, filename),
                os.path.join(target_dir, filename)
            )
            print(f"✅ Arquivo {filename} movido para {target_dir}")

if __name__ == "_main_":
    organize_file("C:\\Users\\erick\\Downloads")  # Caminho Windows