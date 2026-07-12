import pandas as pd
from datetime import datetime

print("Starting automated validation...")

# Step 1: Read the data
df = pd.read_excel("raw_tickets.xlsx")

# Step 2: Validate - find problems automatically
issues_found = []

missing_issue_type = df[df["Issue_Type"] == ""]
if len(missing_issue_type) > 0:
    issues_found.append(f"{len(missing_issue_type)} tickets missing Issue_Type")

missing_status = df[df["Status"] == ""]
if len(missing_status) > 0:
    issues_found.append(f"{len(missing_status)} tickets missing Status")

bad_time = df[(df["Resolution_Time_Hours"] < 0) | (df["Resolution_Time_Hours"] > 24)]
if len(bad_time) > 0:
    issues_found.append(f"{len(bad_time)} tickets with unrealistic resolution time")

# Step 3: Clean the data automatically
df_clean = df.copy()
df_clean = df_clean[df_clean["Issue_Type"] != ""]
df_clean = df_clean[df_clean["Status"] != ""]
df_clean = df_clean[(df_clean["Resolution_Time_Hours"] >= 0) & (df_clean["Resolution_Time_Hours"] <= 24)]

# Step 4: Build a summary report automatically
summary = df_clean.groupby("Issue_Type")["Ticket_ID"].count().reset_index()
summary.columns = ["Issue_Type", "Ticket_Count"]

# Step 5: Save everything - clean data + report
with pd.ExcelWriter("automated_report.xlsx") as writer:
    df_clean.to_excel(writer, sheet_name="Clean_Data", index=False)
    summary.to_excel(writer, sheet_name="Summary_Report", index=False)

# Step 6: Write a log file - this is your "monitoring"
with open("automation_log.txt", "a") as log:
    log.write(f"\n--- Run at {datetime.now()} ---\n")
    log.write(f"Total records processed: {len(df)}\n")
    log.write(f"Clean records: {len(df_clean)}\n")
    log.write(f"Issues found: {len(issues_found)}\n")
    for issue in issues_found:
        log.write(f" - {issue}\n")

print(f"Done. {len(issues_found)} issues found and logged.")
print("Report saved as automated_report.xlsx")
print("Check automation_log.txt for details")