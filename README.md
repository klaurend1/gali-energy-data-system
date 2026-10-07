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