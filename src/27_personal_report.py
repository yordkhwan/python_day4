import argparse
import csv
from pathlib import Path
from datetime import datetime, date

DATE_FORMAT = "%d/%m/%Y"


def parse_args():
    parser = argparse.ArgumentParser(
        description="สรุปรายการงานตามกำหนดส่ง"
    )
    parser.add_argument(
        "input_file",
        help="ไฟล์ CSV รายการงาน"
    )
    parser.add_argument(
        "--output",
        default="output/report.txt"
    )
    return parser.parse_args()


def get_task_status(due_date_text):
    try:
        due_date = datetime.strptime(
            due_date_text,
            DATE_FORMAT
        ).date()

    except ValueError:
        return "invalid", None

    today = date.today()
    diff_days = (due_date - today).days

    if diff_days < 0:
        return "overdue", diff_days

    if diff_days == 0:
        return "due today", diff_days

    return "upcoming", diff_days


def read_tasks(path):
    tasks = []

    with path.open(
        "r",
        encoding="utf-8",
        newline=""
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            tasks.append(row)

    return tasks


def write_report(output_path, lines):
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    content = [
        f"Task Report - {timestamp}",
        "=" * 30
    ]

    content.extend(lines)

    output_path.write_text(
        "\n".join(content),
        encoding="utf-8"
    )


def main():
    args = parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output)

    try:
        tasks = read_tasks(input_path)

    except FileNotFoundError:
        print(f"[ERROR] ไม่พบไฟล์: {input_path}")
        raise SystemExit(1)

    lines = []

    for task in tasks:
        status, days = get_task_status(
            task.get("due_date", "")
        )

        title = task.get(
            "title",
            "ไม่ระบุชื่อ"
        )

        lines.append(
            f"{title}: {status} ({days})"
        )

    write_report(output_path, lines)

    print(f"สร้างรายงานแล้ว: {output_path}")


if __name__ == "__main__":
    main()