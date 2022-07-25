import pandas as pd

# read csv file as data frame
ecom = pd.read_csv("ecom.csv")

# Check the head of the DataFrame
ecom.head()

# How many rows and columns are there?
ecom.info()

# What is the average Purchase Price?
ecom['Purchase Price'].mean()

# What were the highest and lowest purchase prices?
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

# How many people have English 'en' as their 
# Language of choice on the website?
ecom[ecom['Language'] == 'en']['Language'].count()

# How many people have the job title of "Lawyer" ?
ecom[ecom['Job'] == 'Lawyer']['Job'].count()

# How many people made the purchase during the AM 
# and how many people made the purchase during PM ?
time_of_day = ecom.groupby('AM or PM')
time_of_day['AM or PM'].count()

# What are the 5 most common Job Titles?
ecom['Job'].value_counts().head(5)

# Someone made a purchase that came from Lot: "90 WT" , 
# what was the Purchase Price for this transaction?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']

# What is the email of the person with the following 
# Credit Card Number: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']

# How many people have American Express as their Credit Card Provider
# *and* made a purchase above $95 ?
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()

# Hard: How many people have a credit card that expires in 2025?
expiry_dates = ecom['CC Exp Date'].tolist()

def expiry_check(dates):
    count = 0
    for d in dates:
        if '/25' in d:
            count = count + 1
    
    return count

expiry_check(expiry_dates)

# better way of doing this
ecom[ecom['CC Exp Date'].apply(lambda exp: exp.split('/')[1] == '25')]['Credit Card'].count()

# Hard: What are the top 5 most popular email providers/hosts
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
