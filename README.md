# Wedding Seating Chart Generator & Table Calculator

This project includes two tools for planning a wedding or large event:

1. **Seating Chart Generator**  
   Automatically assigns guests to tables based on their tag (e.g., bride_family, groom_family, couple, friend), keeping couples together and grouping families and friends logically.

2. **Table Calculator**  
   Calculates all possible table configurations (round, rectangle, or mixed) to accommodate a given number of guests. Includes min/max seating ranges and extra values.

Requirements: 
Python 3.6+

No external dependencies

---

## 1. Seating Chart Generator

### Features
- Keeps couples seated together
- Groups guests by tags: `bride_family`, `groom_family`, `couple`, `friend`
- Avoids splitting families across multiple tables when possible
- Console-based and easy to configure
- Optional: can be integrated into a GUI (Tkinter)

---

## 2. Table Calculator

### Features
- Supports various round and rectangle table sizes:
- Round: 30", 48", 60", 72"
- Rectangle: 6' and 8'
- Calculates all possible combinations for a given guest count
- Includes min/max seating capacity and extra seat values
- Shows mixed layouts combining round and rectangle tables
- Sorted by most efficient (fewest tables) layout

### How to Run

```bash
python SeatingChartGenerator.py
python TableCalculator.py
