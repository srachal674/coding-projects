import os

base_folder = os.getcwd()

for name in os.listdir(base_folder):
    old_path = os.path.join(base_folder, name)

    # only rename folders
    if os.path.isdir(old_path):
        new_name = name.lower()
        new_path = os.path.join(base_folder, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"{name} -> {new_name}")

print("Done.")
