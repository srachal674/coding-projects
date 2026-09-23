import os
import re
import shutil

# ============================================================
# SETTINGS
# ============================================================

# Leave True the first time so you can preview everything safely.
DRY_RUN = False

# Current folder where the script is located
BASE_FOLDER = os.getcwd()

# This script should not move itself
SCRIPT_NAME = "organize_python_files.py"

# Files to ignore
IGNORE_FILES = {
    SCRIPT_NAME.lower(),
    ".ds_store",
}

# Folders to leave alone
IGNORE_FOLDERS = {
    "__pycache__",
    ".git",
    "build",
    "dist",
    ".venv",
    "venv",
    "env",
}

# ============================================================
# HELPERS
# ============================================================

def clean_name(filename):
    """
    Convert filename to lowercase_with_underscores.
    Keeps the extension.
    """
    name, ext = os.path.splitext(filename)

    name = name.lower()
    name = name.replace(" ", "_")
    name = name.replace("-", "_")

    # Remove characters that are awkward in filenames
    name = re.sub(r"[^a-z0-9_]", "", name)

    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name).strip("_")

    return f"{name}{ext.lower()}"


def choose_folder(cleaned_filename):
    """
    Decide folder name based on words already in the filename.
    """
    name, _ = os.path.splitext(cleaned_filename)

    if name.startswith("art"):
        return "Art"
    if "argyle" in name:
        return "Argyle"
    if "spiral" in name:
        return "Spiral"
    if name.startswith("grade") or "grade" in name:
        return "Grade"

    return "Other"


def is_target_file(filename):
    """
    Only organize Python source files and spec files.
    """
    lower = filename.lower()
    return lower.endswith(".py") or lower.endswith(".spec")


def get_unique_path(path):
    """
    If destination exists, make a unique filename like _2, _3, etc.
    """
    if not os.path.exists(path):
        return path

    base, ext = os.path.splitext(path)
    counter = 2

    while True:
        new_path = f"{base}_{counter}{ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1


# ============================================================
# MAIN
# ============================================================

def main():
    print(f"\nWorking in: {BASE_FOLDER}")
    print(f"DRY_RUN = {DRY_RUN}\n")

    actions = []

    for item in os.listdir(BASE_FOLDER):
        src_path = os.path.join(BASE_FOLDER, item)

        # Skip folders completely
        if os.path.isdir(src_path):
            if item in IGNORE_FOLDERS:
                print(f"Skipping folder: {item}")
            else:
                print(f"Leaving folder alone: {item}")
            continue

        # Skip ignored files
        if item.lower() in IGNORE_FILES:
            print(f"Skipping file: {item}")
            continue

        # Only organize .py and .spec
        if not is_target_file(item):
            print(f"Skipping non-target file: {item}")
            continue

        cleaned_name = clean_name(item)
        folder_name = choose_folder(cleaned_name)
        folder_path = os.path.join(BASE_FOLDER, folder_name)

        dest_path = os.path.join(folder_path, cleaned_name)
        dest_path = get_unique_path(dest_path)

        actions.append((src_path, folder_path, dest_path))

    if not actions:
        print("No .py or .spec files found to organize.")
        return

    print("\nPlanned changes:\n")
    for src, folder_path, dest in actions:
        print(f"{os.path.basename(src)}")
        print(f"  -> {os.path.basename(folder_path)}/{os.path.basename(dest)}\n")

    if DRY_RUN:
        print("Preview only. No files were changed.")
        print("If it looks right, change DRY_RUN = False and run it again.")
        return

    print("Applying changes...\n")

    for src, folder_path, dest in actions:
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(src, dest)
        print(f"Moved: {os.path.basename(src)} -> {dest}")

    print("\nDone.")


if __name__ == "__main__":
    main()
