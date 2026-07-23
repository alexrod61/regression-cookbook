from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]

# Quarto may treat a chapter `_files` directory as rendered support output.
# Keep source-side simulation assets available after each render.
SOURCE_SUPPORT_DIRS = [
    (
        ROOT / "docs/book/04-gamma_files/simulations",
        ROOT / "book/04-gamma_files/simulations",
    ),
    (
        ROOT / "docs/book/14-multinomial-logistic_files/simulations",
        ROOT / "book/14-multinomial-logistic_files/simulations",
    )
]


def restore_support_dir(rendered_dir, source_dir):
    if not rendered_dir.exists():
        return

    source_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(rendered_dir, source_dir, dirs_exist_ok=True)


for rendered_dir, source_dir in SOURCE_SUPPORT_DIRS:
    restore_support_dir(rendered_dir, source_dir)
