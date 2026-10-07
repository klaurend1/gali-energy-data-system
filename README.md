# GALI Energy Data System

GALI is an experimental renewable energy data system exploring how sunlight measurements can be converted into structured, tamper-evident digital records.

The current prototype includes:

- Solar intensity simulation
- Energy token calculation
- CSV ledger generation
- SHA-256 hash chaining
- Independent ledger verification
- Preserved data from early hardware testing

## Features

- Generates simulated sunlight intensity readings
- Converts measurements into digital energy tokens
- Tracks cumulative token totals
- Links every record to the previous record using SHA-256
- Detects modified or broken ledger records
- Preserves original hardware experiment data

## Requirements

- Python 3.10 or newer

No external Python packages are required.

GALI currently uses only Python standard-library modules:

- `csv`
- `hashlib`
- `random`
- `time`
- `datetime`
- `sys`

## Project Structure

```text
gali-energy-data-system/
├── data/
│   └── first_hardware_test.csv
├── ledger.csv
├── main.py
├── verify_ledger.py
├── README.md
├── LICENSE
└── .gitignore
```

## Run GALI

Clone the repository:

```bash
git clone https://github.com/klaurend1/gali-energy-data-system.git
cd gali-energy-data-system
```

Run the simulation:

```bash
python3 main.py
```

The program generates ten simulated solar measurements and writes them to:

```text
ledger.csv
```

After generation, GALI automatically verifies the cryptographic integrity of the ledger.

Example:

```text
GALI Solar Tokenizer Starting...

[2026-10-07 03:13:24] Intensity: 788 | Minted: 7.88 ST | Total: 7.88

Simulation complete. Data saved to ledger.csv

Verifying ledger...
Ledger verified successfully.
Records: 10
Chains: 1
```

## Verify a Ledger

The verification tool can also be run independently:

```bash
python3 verify_ledger.py ledger.csv
```

To verify the preserved hardware experiment:

```bash
python3 verify_ledger.py data/first_hardware_test.csv
```

The original hardware dataset currently verifies:

```text
Ledger verified successfully.
Records: 151
Chains: 5
```

## Hash Chain

Each ledger record contains:

```text
timestamp
measurement
solar value
tokens minted
cumulative tokens
previous hash
current hash
```

The current hash is generated using SHA-256 from the record data and the hash of the previous record.

This creates a tamper-evident chain. Modifying a historical record breaks verification.

## Hardware Prototype Data

`data/first_hardware_test.csv` contains measurements collected during early GALI hardware experiments.

The dataset is preserved as an original experimental artifact and is never overwritten by the simulation.

## Project Direction

GALI is still in active development.

Future work includes:

- Live Arduino sensor ingestion
- Improved renewable-energy token models
- Real-time ledger validation
- Additional sensor metadata
- Smart contract experimentation
- Visualization and analytics

## Tech

Python  
SHA-256  
CSV  
Arduino hardware experimentation

## Author

Keith Laurendine Jr.

## License

MIT