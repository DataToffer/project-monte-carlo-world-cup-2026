from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def read_csv(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(data: dict[str, Any], path: str | Path) -> None:
    Path(path).write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
