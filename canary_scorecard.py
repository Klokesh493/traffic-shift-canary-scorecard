import csv
import sys


def verdict(row):
    if float(row["error_rate_pct"]) > 1.0:
        return "rollback"
    if float(row["p95_latency_ms"]) > 500:
        return "pause"
    if int(row["saturation_pct"]) > 80:
        return "pause"
    if row["rollback_ready"].lower() != "yes":
        return "pause"
    return "advance"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['service']} {verdict(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
