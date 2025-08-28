# Client KPI Analysis
This is a straightforward, Python-powered client Key Performance Indicators (KPIs) analysis tool. It's for data analysts, freelancers, or small organizations that need to rapidly compute and report on critical client metrics from a formatted dataset. The project is highly extensible, such that you can simply include additional new KPIs and support alternative data sources.

✨ Features
KPI Calculation: Automatically calculates key metrics such as Total Revenue, Average Revenue per Client (ARPC), and Churn Rate.

Top Client Identification: Identifies and lists top-performing clients through revenue ranking.

Data Visualization: Creates and stores key charts, such as bar chart for revenue comparison, pie chart for client status, and scatter plot for revenue vs. duration.

Easy Data Input: Reads directly from a client_data.csv file, and you can easily substitute in your own datasets.

Clean Reporting: Outputs a clean and readable report in the console and saves visualizations for easy sharing.

🚀 Getting Started
These instructions will get the project set up and running on your local machine.

Prerequisites
You should have Python 3.6 or later installed.

1. Clone the Repository
git clone https://github.com/your-username/client-kpi-analysis.git
cd client-kpi-analysis

2. Set Up a Virtual Environment
It's a good practice to use a virtual environment to manage dependencies.

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install Dependencies
Install the required libraries using the requirements.txt file.

pip install -r requirements.txt

4. Run the Analysis
Place your client data in the data/client_data.csv file, then run the main script.

python src/kpi_calculator.py

The script will print the report to your terminal and save the visualizations in the newly created viz/ directory.

📊 Sample Output
Once you've executed the script, you will have a report like this in your terminal:

--- Client KPI Analysis Report ---
-----------------------------------
Total Number of Clients: 10
-----------------------------------
Total Revenue: $10,101.00
-----------------------------------
Average Revenue per Client (ARPC): $1,010.10
-----------------------------------
Churn Rate: 30.00%
-----------------------------------
Average Subscription Duration (Active Clients): 22.0 months
-----------------------------------
Top 5 Clients by Revenue:
   client_id  revenue  subscription_duration_months   status
7        108  1800.00                            48   active
4    105  1500.75                            36   active
1        102  1200.50                            24   active
9        110  1100.50                            20   active
5        106   900.00                            18   active
-----------------------------------

🤝 Contribute
We welcome contributions! If you have some ideas or would like to implement a new feature, feel free to open an issue or propose a pull request.
