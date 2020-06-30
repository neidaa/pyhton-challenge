#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies
import csv


# In[ ]:


# Files to load and output
file_to_load = "raw_data/budget_data_1.csv"
file_to_output = "anaylsis/budget_analysis_1.txt"


# In[ ]:


# Track various revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0


# In[ ]:


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:
        
        # Track the totals
        total_months = total_months + 1
        total_revenu = total_revenue +int(row["Revenue"])
        
        # Track the revenue change 
        revenue_change = int(row["Revenue"]) - prev_revenue 
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
        
        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
        
        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change


# In[ ]:


# Calculate the average revenue change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


#Generate Output summary 
output = (
    f"\nFinancial Analysis\n"
    f"----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Averager revenue change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]}(${greatest_decrease[1]})\n"
)


# In[ ]:


# Print the output 
print (output)


# In[ ]:


# Export the results to text file 
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

