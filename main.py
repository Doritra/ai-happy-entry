import os
import shutil

src = os.path.join(os.path.dirname(__file__), "entry.png")
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
dst = os.path.join(output_dir, "entry.png")

shutil.copyfile(src, dst)
