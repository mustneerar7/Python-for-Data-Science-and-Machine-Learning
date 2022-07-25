import pandas as pd

# Read Salaries.csv as a dataframe called sal
sal = pd.read_csv('salaries.csv')

# Check the head of the DataFrame
head = sal.head()

# Use the .info() method to find out 
# how many entries there are
info = sal.info()

# What is the average BasePay ?
avg_base_pay = sal['BasePay'].mean()

# What is the highest amount of OvertimePay in the dataset ?
highest_overtime = sal['OvertimePay'].max()

# What is the job title of  JOSEPH DRISCOLL ? 
# Note: Use all caps, otherwise you may get an answer 
# that doesn't match up (there is also a lowercase Joseph Driscoll).
name = 'JOSEPH DRISCOLL'
emp = sal[['EmployeeName', 'JobTitle', 'TotalPayBenefits']]
emp[emp['EmployeeName'] == name]['JobTitle']

# How much does JOSEPH DRISCOLL make (including benefits)?
emp[emp['EmployeeName'] == name]['TotalPayBenefits']

# What is the name of highest paid person (including benefits)?
highest_pay = sal['TotalPayBenefits'].max()
sal[sal['TotalPayBenefits'] == highest_pay]

# What is the name of lowest paid person (including benefits)? 
# Do you notice something strange about how much he or she is paid?
lowest_pay = sal['TotalPayBenefits'].min()
sal[sal['TotalPayBenefits'] == lowest_pay]

# the average (mean) BasePay of all employees per year (2011-2014)
yearly = sal.groupby('Year')
yearly['BasePay'].mean()

# How many unique job titles are there?
unique_job_titles = sal.groupby("JobTitle")
unique_job_titles.count()
# alternate (better) method
sal['JobTitle'].nunique()

# What are the top 5 most common jobs?
unique_job_titles['JobTitle'].count().sort_values(ascending=False).head(5)
# alternate (better) method
sal['JobTitle'].value_counts().head(5)

# How many Job Titles were represented by only one person in 2013? 
# (e.g. Job Titles with only one occurence in 2013?)
occurence = sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1
sum(occurence)

# How many people have the word Chief in their job title? (This is pretty tricky)
print(sal[sal['JobTitle'].apply(lambda jt: "chief" in jt.lower().split())]['JobTitle'].count())