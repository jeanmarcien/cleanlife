import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('Life_Insurance_Data.csv')

# Inspect the dataset
print(df.info())
print(df.head())

# Handle missing values
missing_values = df.isnull().sum()
print(missing_values)

df_cleaned = df.dropna(subset=['policy_holder_name', 'last_name'])
df_cleaned['age'] = df_cleaned['age'].replace('unknown', pd.NA).fillna(df_cleaned['age'].mode()[0])
df_cleaned['email'] = df_cleaned['email'].fillna('unknown@example.com')
df_cleaned['phone'] = df_cleaned['phone'].fillna('000-000-0000')
df_cleaned['address'] = df_cleaned['address'].fillna('Unknown Address')
df_cleaned['policy_amount'] = df_cleaned['policy_amount'].replace('unknown', pd.NA).fillna(df_cleaned['policy_amount'].mode()[0])
df_cleaned['policy_term'] = df_cleaned['policy_term'].replace('unknown', pd.NA).fillna(df_cleaned['policy_term'].mode()[0])
df_cleaned['policy_status'] = df_cleaned['policy_status'].fillna('unknown')
df_cleaned['beneficiary_name'] = df_cleaned['beneficiary_name'].fillna('Unknown')

# Correct data types
df_cleaned['age'] = pd.to_numeric(df_cleaned['age'], errors='coerce').fillna(df_cleaned['age'].mode()[0])
df_cleaned['date_of_birth'] = pd.to_datetime(df_cleaned['date_of_birth'], errors='coerce')
df_cleaned['policy_start_date'] = pd.to_datetime(df_cleaned['policy_start_date'], errors='coerce')
df_cleaned['policy_amount'] = pd.to_numeric(df_cleaned['policy_amount'], errors='coerce').fillna(df_cleaned['policy_amount'].mode()[0])
df_cleaned['policy_term'] = pd.to_numeric(df_cleaned['policy_term'], errors='coerce').fillna(df_cleaned['policy_term'].mode()[0])

# Standardize data formats
df_cleaned['phone'] = df_cleaned['phone'].str.replace(r'[^0-9]', '', regex=True)
df_cleaned['phone'] = df_cleaned['phone'].apply(lambda x: f'{x[:3]}-{x[3:6]}-{x[6:]}')
df_cleaned['email'] = df_cleaned['email'].str.lower()

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Validate data
invalid_ages = df_cleaned[df_cleaned['age'] < 0]
invalid_policy_amounts = df_cleaned[df_cleaned['policy_amount'] < 0]

print(f"Invalid ages:\n{invalid_ages}")
print(f"Invalid policy amounts:\n{invalid_policy_amounts}")

df_cleaned = df_cleaned[df_cleaned['age'] >= 0]
df_cleaned = df_cleaned[df_cleaned['policy_amount'] >= 0]

# Save the cleaned data
df_cleaned.to_csv('cleaned_life_insurance_data.csv', index=False)
print("Cleaned data saved to 'cleaned_life_insurance_data.csv'")
