# Import libraries
import pandas as pd

# Create a DataFrame with missing values
data = {'Country': ['USA', 'UK', 'Canada', None],
        'GDP': [21.43, 2.83, 1.74, 0.3]}
df = pd.DataFrame(data)

# Exercise 2: clean the missing values and sort by GDP
cleaned_df = df.dropna().sort_values(by='GDP', ascending=False)
print(cleaned_df)

# Exercise 3: calculate the total GDP
total_gdp = cleaned_df['GDP'].sum()
print("Total GDP:", total_gdp)