#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


import pandas as pd

# Sample dataset
data = {
    'client_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'revenue': [500.00, 1200.50, 750.00, 250.00, 1500.75, 900.00, 300.25, 1800.00, 600.00, 1100.50],
    'subscription_duration_months': [12, 24, 6, 3, 36, 18, 5, 48, 10, 20],
    'status': ['active', 'active', 'churned', 'churned', 'active', 'active', 'churned', 'active', 'active', 'active']
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to calculate KPIs
def calculate_kpis(df):
    """
    Calculates and prints key performance indicators (KPIs).
    """
    print("--- Client KPI Analysis Report ---")
    print("-" * 35)

    # 1. Total Clients
    total_clients = df['client_id'].nunique()
    print(f"Total Clients: {total_clients:,}")
    print("-" * 35)

    # 2. Total Revenue
    total_revenue = df['revenue'].sum()
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print("-" * 35)

    # 3. Average Revenue per Client
    avg_rev = total_revenue / total_clients
    print(f"Avg Revenue per Client: ${avg_rev:,.2f}")
    print("-" * 35)

    # 4. Churn Rate
    churned = df[df['status'] == 'churned'].shape[0]
    churn_rate = (churned / len(df)) * 100
    print(f"Churn Rate: {churn_rate:.2f}%")
    print("-" * 35)

    # 5. Avg Subscription Duration (Active Clients)
    active_clients = df[df['status'] == 'active']
    avg_duration = active_clients['subscription_duration_months'].mean()
    print(f"Avg Subscription Duration: {avg_duration:.1f} months")
    print("-" * 35)

    # 6. Top 5 Clients by Revenue
    top_clients = df.sort_values(by='revenue', ascending=False).head(5)
    print("Top 5 Clients by Revenue:")
    print(top_clients[['client_id', 'revenue', 'subscription_duration_months', 'status']])
    print("-" * 35)


# ✅ Call the function
calculate_kpis(df)


# In[11]:


top_clients = df.sort_values(by='revenue', ascending=False).head(5)
print("Top 5 Clients by Revenue:")
print(top_clients[['client_id', 'revenue', 'subscription_duration_months', 'status']])



# In[13]:


plt.figure(figsize=(10, 6))
sns.barplot(
    x='client_id', 
    y='revenue', 
    data=df.sort_values(by='revenue', ascending=False), 
    palette='viridis'
)
plt.title('Client Revenue Comparison', fontsize=16)
plt.xlabel('Client ID')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[14]:


plt.figure(figsize=(8, 8))
status_counts = df['status'].value_counts()
plt.pie(
    status_counts, 
    labels=status_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#4CAF50', '#FF5733']
)
plt.title('Client Status: Active vs. Churned', fontsize=16)
plt.axis('equal')
plt.show()


# In[15]:


plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='subscription_duration_months', 
    y='revenue', 
    hue='status', 
    data=df, 
    s=100, 
    style='status', 
    palette='coolwarm'
)
plt.title('Revenue vs. Subscription Duration', fontsize=16)
plt.xlabel('Subscription Duration (months)')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()


# In[ ]:




