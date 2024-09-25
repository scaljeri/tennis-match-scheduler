# Tennis Match Scheduler

A Python tool that schedules tennis matches for groups of players while considering their availability and gender requirements. The tool can randomly select players for matches, ensuring that the selected groups are mixed doubles (2 male and 2 female players) if desired.

## Features

- **Random Scheduling**: Schedule 4 players randomly for tennis matches.
- **Gender Mix**: Ensure that scheduled matches consist of 2 male and 2 female players for mixed doubles.
- **Availability Handling**: Exclude players who have indicated they cannot play on specific dates.
- **Restrictions**: Consider players that cannot play together.

## Requirements

- Python 3.10 or higher
- Pandas (for handling CSV files)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Input Files

### Players CSV
The `players.csv` file should contain the following columns:

- `Name`: The name of the player.
- `Unavailable Dates`: Comma-separated list of dates the player cannot play.
- `Cannot Play With`: The name of the player they cannot play with.

**Example**:
```csv
Name,Unavailable Dates,Cannot Play With
Alice,2024-09-20,Charlie
Bob,2024-09-21,Diana
Charlie,2024-09-22,Alice
Diana,2024-09-21,Bob
```

### Dates CSV
The `match_dates.csv` file should list the available dates for playing tennis:

	- `Dates`: The date when the tennis field is available.

**Example**:
```csv
Date
2024-09-20
2024-09-21
2024-09-22
```

## Usage

To use the scheduler, run the Python script with the input CSV files:

```bash
python scheduler.py players.csv match_dates.csv --mixed
```
Use the --mixed flag to enforce the 2 male and 2 female players rule for mixed doubles. If you want to schedule randomly without gender constraints, simply omit the --mixed flag.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Lucas Calje