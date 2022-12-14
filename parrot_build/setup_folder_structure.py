# pyre-strict

import os
import argparse
from typing import List


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--htb-dir",
        type=str,
        help="Path to the hackTheBox directory",
        required=True,
    )
    parser.add_argument(
        "--parent-dirs",
        type=str,
        help="List of parent directories to create",
        required=True,
    )
    parser.add_argument(
        "--children-dirs",
        type=str,
        help="List of child directories to create",
        required=True,
    )
    args: List[str] = parser.parse_args()

    htb_dir = os.path.abspath(args.htb_dir)
    parent_dirs: List[str] = [dir.strip() for dir in args.parent_dirs.split(",")]
    children_dirs: List[str] = [dir.strip() for dir in args.children_dirs.split(",")]
    operating_systems: List[str] = ["linux", "windows"]

    if not os.path.exists(htb_dir):
        print("HackTheBox directory does not exist")
        os.makedirs(htb_dir)

    os.chdir(htb_dir)

    for parent_dir in parent_dirs:
        for operating_system in operating_systems:
            parent_dir_path = os.path.join(htb_dir, parent_dir, operating_system)
            if not os.path.exists(parent_dir_path):
                os.makedirs(parent_dir_path)

            for child_dir in children_dirs:
                child_dir_path = os.path.join(parent_dir_path, child_dir)
                if not os.path.exists(child_dir_path):
                    os.makedirs(child_dir_path)


if __name__ == "__main__":
    main()
