import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="นับจำนวนบรรทัดในไฟล์")
    parser.add_argument("input_file", help="ไฟล์ที่ต้องการอ่าน")
    return parser.parse_args()


def main():
    args = parse_args()

    path = Path(args.input_file)

    # check file exists first
    if not path.exists():
        print(f"[ERROR] cannot find file path: {path}")
        raise SystemExit(1)

    try:
        text = path.read_text(encoding="utf-8")

    except UnicodeDecodeError:
        print("[ERROR] cannot read file, please check encoding")
        raise SystemExit(1)

    # count lines safely
    lines = text.splitlines()

    print(f"จำนวนบรรทัด = {len(lines)}")
    print(f"file :{path}")
    print(f"line: {len(lines)}")
    print(f"characters: {len(text)}")


if __name__ == "__main__":
    main()