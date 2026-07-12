import pandas as pd
import random

# Create fake sample data - like a company would have
data = {
    "Ticket_ID": [f"T{1000+i}" for i in range(50)],
    "Customer": [f"Customer_{i}" for i in range(50)],
    "Issue_Type": [random.choice(["Login Error", "Payment Failed", "App Crash", "Slow Response", ""]) for _ in range(50)],
    "Status": [random.choice(["Open", "Closed", "Pending", ""]) for _ in range(50)],
    "Resolution_Time_Hours": [random.choice([2, 5, 8, -1, 100, None]) for _ in range(50)]
}

df = pd.DataFrame(data)
df.to_excel("raw_tickets.xlsx", index=False)
print("Sample data created: raw_tickets.xlsx")