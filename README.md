# Candy Crush EDA

Exploratory Data Analysis on Candy Crush game data — analyzing player attempts, success rates, and level difficulty using Python, Pandas, Seaborn, and Matplotlib.

---

## Project Overview

This project explores a real-world Candy Crush dataset to uncover patterns in player behavior, level difficulty, and success rates across different game levels.

---

## Key Analysis Performed

- Distribution of numeric columns using histograms
- Count of attempts and successes per level
- Boxplots to compare attempt and success distribution across levels
- Correlation heatmap between numeric features
- Missing value and duplicate row checks

---

## Key Findings

- Significant variation in number of attempts across levels, indicating differences in level difficulty
- Some levels show consistently low success rates, pointing to higher difficulty
- Number of attempts and successes show a moderate positive correlation

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Visualizations |

---

## Project Structure

```
candy-crush-eda/
│
├── candycrush.py       # Main EDA script
├── candy_crush.csv     # Dataset
└── README.md
```

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/mahrukhmobin/candy-crush-eda.git

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Run the script
python candycrush.py
```

---

## Dataset Features

| Column | Description |
|--------|-------------|
| level | Game level number |
| num_attempts | Total attempts made by players |
| num_success | Total successful completions |

---

*Built by [Mahrukh Mobin](https://github.com/mahrukhmobin) — Computer Engineering Student @ UET Lahore*
