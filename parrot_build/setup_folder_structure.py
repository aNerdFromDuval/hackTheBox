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
        type=list,
        help="List of parent directories to create",
        required=True,
    )
    parser.add_argument(
        "--children-dirs",
        type=list,
        help="List of child directories to create",
        required=True,
    )
    args: List[str] = parser.parse_args()

    htb_dir = os.path.abspath(args.htb_dir)
    parent_dirs: List[str] = list(args.parent_dirs)
    children_dirs: List[str] = list(args.children_dirs)

    if not os.path.exists(htb_dir):
        print("HackTheBox directory does not exist")
        os.mkdir(htb_dir)

    for parent_dir in parent_dirs:
        parent_dir_path = os.path.join(htb_dir, parent_dir)
        if not os.path.exists(parent_dir_path):
            os.mkdir(parent_dir_path)

        for child_dir in children_dirs:
            child_dir_path = os.path.join(parent_dir_path, child_dir)
            if not os.path.exists(child_dir_path):
                os.mkdir(child_dir_path)


if __name__ == "__main__":
    main()
