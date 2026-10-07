# GALI Energy Data System

GALI is an experimental renewable energy data system exploring how sunlight measurements can be converted into structured digital records.

This repository currently contains a Python simulation prototype that generates solar intensity readings, converts them into energy tokens, and records the results in a CSV ledger.

## Features

- Simulates sunlight intensity readings
- Converts readings into digital energy tokens
- Tracks cumulative token totals
- Stores timestamped readings in a CSV ledger
- Provides a foundation for future physical sensor integration

## How It Works

Each simulated sunlight reading is converted into tokens using:

```text
tokens = intensity / 100

## Hardware Prototype Data

The `data/first_hardware_test.csv` dataset contains measurements collected during early GALI hardware experiments.

Each record includes sensor measurements, calculated token values, and cryptographic hashes linking records together.

This creates a tamper-evident measurement history where each record references the hash of the previous record.

The dataset is preserved as an original experimental artifact and is not overwritten by the simulation.