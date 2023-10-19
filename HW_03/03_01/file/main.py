import argparse
import sys
from pathlib import Path
from shutil import copyfile
import logging
import threading

def grabs_folder(path: Path) -> list[Path]:
    folders = []
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            inner_dir = grabs_folder(el)
            if len(inner_dir):
                folders = folders + inner_dir
    return folders

def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)
                sys.exit(1)

def copy_files_in_threads(folders):
    threads = []
    for folder in folders:
        thread = threading.Thread(target=copy_file, args=(folder,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")
    args = vars(parser.parse_args())
    source = Path(args.get("source"))
    output = Path(args.get("output"))

    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders = [source, *grabs_folder(source)]
    copy_files_in_threads(folders)

    print(f"Можна видаляти {source}")


