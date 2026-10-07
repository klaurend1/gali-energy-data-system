import csv
import hashlib
import random
import time
from datetime import datetime

from verify_ledger import verify_ledger

CSV_FILE = "ledger.csv"
NUM_READINGS = 10


def generate_intensity():
    return random.randint(100, 1000)


def calculate_tokens(intensity):
    return round(intensity / 100, 2)


def calculate_hash(fields):
    payload = "|".join(str(value) for value in fields)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def run_simulation():
    total_tokens = 0.0
    previous_hash = "GENESIS"

    # Start a fresh simulation ledger
    open(CSV_FILE, "w").close()

    print("GALI Solar Tokenizer Starting...\n")

    for _ in range(NUM_READINGS):
        intensity = generate_intensity()
        solar_value = round(intensity / 100, 3)

        tokens = calculate_tokens(intensity)
        total_tokens = round(total_tokens + tokens, 3)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        record = [
            timestamp,
            intensity,
            solar_value,
            tokens,
            total_tokens,
            previous_hash
        ]

        current_hash = calculate_hash(record)

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(record + [current_hash])

        print(
            f"[{timestamp}] "
            f"Intensity: {intensity} | "
            f"Minted: {tokens} ST | "
            f"Total: {total_tokens}"
        )

        previous_hash = current_hash
        time.sleep(1)

    print(f"\nSimulation complete. Data saved to {CSV_FILE}\n")

    print("Verifying ledger...")
    verify_ledger(CSV_FILE)


if __name__ == "__main__":
    run_simulation()