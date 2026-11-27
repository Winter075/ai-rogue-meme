import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).with_name("entry.png")

assert SOURCE.is_file(), "draw_meme.py must produce entry.png first"

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, out / "entry.png")
assert (out / "entry.png").stat().st_size <= 1048576, "the gate caps images at 1 MiB"
