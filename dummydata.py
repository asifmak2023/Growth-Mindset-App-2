import pandas as pd

# Create dummy data
quotes_data = {
    "Quote": ["The only limit is your imagination.", "Embrace challenges and grow."],
    "Author": ["Unknown", "Carol Dweck"]
}

goals_data = {
    "Goal": ["Learn Python", "Read 10 books"],
    "Progress (%)": [75, 50]
}

# Save to Excel
with pd.ExcelWriter("growth_mindset_data.xlsx") as writer:
    pd.DataFrame(quotes_data).to_excel(writer, sheet_name="Quotes", index=False)
    pd.DataFrame(goals_data).to_excel(writer, sheet_name="Goals", index=False)