import csv
import hashlib
import sys


def calculate_hash(fields):
    """Recreate the SHA-256 hash used by the GALI ledger."""
    payload = "|".join(fields)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def verify_ledger(filename):
    previous_hash = None
    record_count = 0
    chain_count = 0

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        for line_number, row in enumerate(reader, start=1):
            if len(row) != 7:
                print(f"FAIL: row {line_number} has {len(row)} fields")
                return False

            data_fields = row[:6]
            stored_hash = row[6]
            previous_hash_field = row[5]

            # Verify this record's hash
            expected_hash = calculate_hash(data_fields)

            if expected_hash != stored_hash:
                print(f"FAIL: hash mismatch on row {line_number}")
                return False

            # Verify chain linkage
            if previous_hash_field == "GENESIS":
                chain_count += 1
            elif previous_hash_field != previous_hash:
                print(f"FAIL: broken chain on row {line_number}")
                return False

            previous_hash = stored_hash
            record_count += 1

    print("Ledger verified successfully.")
    print(f"Records: {record_count}")
    print(f"Chains: {chain_count}")

    return True


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "ledger.csv"
    verify_ledger(filename)