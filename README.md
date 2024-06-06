# CleanLife: Life Insurance Data Cleaning Project

This project focuses on cleaning a messy dataset related to life insurance policies. The dataset contains various issues such as missing values, inconsistent formats, and invalid data entries. The goal is to clean and standardize the data for further analysis or modeling.

## Dataset Description

The dataset contains the following fields:

- `policy_id`: Unique identifier for each policy (6 characters, starting with 'L' followed by 5 random digits).
- `policy_holder_name`: First name of the policy holder.
- `last_name`: Last name of the policy holder.
- `age`: Age of the policy holder.
- `date_of_birth`: Date of birth of the policy holder.
- `email`: Email address of the policy holder.
- `phone`: Phone number of the policy holder.
- `address`: Address of the policy holder.
- `policy_amount`: Amount of the policy.
- `policy_term`: Term of the policy in years.
- `policy_start_date`: Start date of the policy.
- `policy_status`: Status of the policy (active, inactive, lapsed, surrendered).
- `beneficiary_name`: Name of the beneficiary.

## Steps to Clean the Data

### 1. Load the Data

Load the dataset into a pandas DataFrame.

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_dataset.csv')
