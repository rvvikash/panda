find second max salary from each department using panda? 

import pandas as pd

# Sample data
data = {'Name': ['John', 'Emma', 'Peter', 'Sophia', 'Liam', 'Alex', 'Emily', 'Daniel'],
        'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'HR', 'IT'],
        'Salary': [5000, 6000, 4500, 7000, 5500, 6200, 4800, 5300]}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by department and find the second maximum salary in each group
second_max_salaries = df.groupby('Department')['Salary'].apply(lambda x: x.nlargest(2).iloc[-1])

print(second_max_salaries)


import pandas as pd

# Sample data
data = {'Name': ['John', 'Emma', 'Peter', 'Sophia', 'Liam', 'Alex', 'Emily', 'Daniel'],
        'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'HR', 'IT'],
        'Salary': [5000, 6000, 4500, 7000, 5500, 6200, 4800, 5300]}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by department and get top 2 salaries in each group
top_2_salaries = df.groupby('Department')['Salary'].nlargest(2)

# Get the second maximum salary from each group
second_max_salaries = top_2_salaries.groupby(level=0).nth(-1)

print(second_max_salaries)


top_6_salaries
import pandas as pd

# Sample data
data = {'Name': ['John', 'Emma', 'Peter', 'Sophia', 'Liam', 'Alex', 'Emily', 'Daniel'],
        'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'HR', 'IT'],
        'Salary': [5000, 6000, 4500, 7000, 5500, 6200, 4800, 5300]}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by department and get top 6 salaries in each group
top_6_salaries = df.groupby('Department')['Salary'].nlargest(6)

# Get the 6th maximum salary from each group
sixth_max_salaries = top_6_salaries.groupby(level=0).nth(5)

print(sixth_max_salaries)


