import os
import zipfile

dist_dir = r"C:\Smart-India-hackathon\frontend\dist"
zip_path = r"C:\Smart-India-hackathon\dist.zip"

if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, dist_dir)
            forward_slash_path = rel_path.replace("\\", "/")
            zipf.write(full_path, forward_slash_path)
            print(f"Added: {forward_slash_path}")

print("dist.zip successfully created with forward slashes!")
