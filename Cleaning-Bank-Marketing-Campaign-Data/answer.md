Step-by-step Plan
Read the bank_marketing.csv dataset into a DataFrame.

Subset and clean the DataFrame according to the requirements specified in the notebook.

Reformat the cleaned data into three separate DataFrames as required.

Save each of the three DataFrames into separate files.

To achieve the task of cleaning, subsetting, and saving the bank_marketing.csv dataset into three separate CSV files (client.csv, campaign.csv, and economics.csv), we will follow a structured approach. Here's a step-by-step guide to accomplish this:

Step 1: Load the Dataset
First, we need to load the dataset into a Pandas DataFrame.

python
Copy Code
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("bank_marketing.csv")
Step 2: Subset and Clean the Data
We will create three separate DataFrames: client, campaign, and economics, each containing specific columns and applying the necessary cleaning and formatting.

2.1 Create the client DataFrame
Columns: client_id, age, job, marital, education, credit_default, mortgage
Cleaning:
Replace . with _ in job and education.
Replace unknown with np.NaN in education.
Convert credit_default and mortgage to boolean.
python
Execute
Copy Code
client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']].copy()

# Clean the data
client['job'] = client['job'].str.replace('.', '_', regex=False)
client['education'] = client['education'].str.replace('.', '_', regex=False).replace('unknown', np.NaN)
client['credit_default'] = client['credit_default'].apply(lambda x: 1 if x == 'yes' else 0).astype(bool)
client['mortgage'] = client['mortgage'].apply(lambda x: 1 if x == 'yes' else 0).astype(bool)
2.2 Create the campaign DataFrame
Columns: client_id, number_contacts, contact_duration, previous_campaign_contacts, previous_outcome, campaign_outcome, last_contact_date
Cleaning:
Convert previous_outcome and campaign_outcome to boolean.
Create last_contact_date from day, month, and a new year column set to 2022.
python
Execute
Copy Code
campaign = df[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'day', 'month']].copy()

# Clean the data
campaign['previous_outcome'] = campaign['previous_outcome'].apply(lambda x: 1 if x == 'success' else 0).astype(bool)
campaign['campaign_outcome'] = campaign['campaign_outcome'].apply(lambda x: 1 if x == 'yes' else 0).astype(bool)

# Create last_contact_date
month_map = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
           'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}
campaign['month'] = campaign['month'].map(month_map)
campaign['year'] = 2022
campaign['last_contact_date'] = pd.to_datetime(campaign[['year', 'month', 'day']].astype(str).agg('-'.join, axis=1))

# Drop the temporary columns
campaign.drop(columns=['day', 'month', 'year'], inplace=True)
2.3 Create the economics DataFrame
Columns: client_id, cons_price_idx, euribor_three_months
Cleaning: No additional cleaning required.
python
Execute
Copy Code
economics = df[['client_id', 'cons_price_idx', 'euribor_three_months']].copy()
Step 3: Save the DataFrames to CSV Files
Finally, save each DataFrame to a CSV file without the index.

python
Execute
Copy Code
client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)
This process will create three cleaned and formatted CSV files: client.csv, campaign.csv, and economics.csv, ready for use in a PostgreSQL database.

Execution Error: FileNotFoundError                         Traceback (most recent call last)

Cell In[3], line 5
2 import numpy as np
4 # Load the dataset
----> 5 df = pd.read_csv("bank_marketing.csv")

...

FileNotFoundError: [Errno 2] No such file or directory: 'bank_marketing.csv'