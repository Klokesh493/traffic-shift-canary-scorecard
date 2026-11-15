import csv
import math
import sys


def verdict(row):
    try:
        errors = float(row["error_rate_pct"])
        latency = float(row["p95_latency_ms"])
        saturation = int(row["saturation_pct"])
    except (KeyError, TypeError, ValueError):
        return "pause"
    if (not math.isfinite(errors) or not math.isfinite(latency)
            or not 0 <= errors <= 100 or latency < 0 or not 0 <= saturation <= 100):
        return "pause"
    if errors > 1:
        return "rollback"
    if latency > 500 or saturation > 80 or (row.get("rollback_ready") or "").lower() != "yes":
        return "pause"
    return "advance"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['service']} {verdict(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
