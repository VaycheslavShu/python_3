import json
from collections import defaultdict


def load_purchase_log(file_path: str) -> dict:

    result = defaultdict(list)

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                item = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Пропущена строка {line_num}: {e}")
                continue

            user_id = item.get("user_id")
            category = item.get("category")

            if user_id == "user_id" and category == "category":
                continue

            if user_id is None or category is None:
                continue

            result[user_id].append(category)

    return dict(result)


if __name__ == "__main__":
    data = load_purchase_log("purchase_log.txt")
    print(data)