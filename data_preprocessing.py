# importing packages
import numpy as np
import pandas as pd

# reading the Dataset from csv file 
asd_data = pd.read_csv('./Datasets/Toddler_Autism_dataset.csv',index_col=0)

# Checking columns of the toddler dataset
print('Initial columns of the dataset',asd_data.columns)



# Checking unique attributes of Class Label
print('\nPrinting unique attributes of Class Label',asd_data.Class.unique())

# Changing attributes of class Label
# NO  --> 0
# YES --> 1
asd_data['Class'].replace('No',0,inplace=True)
asd_data['Class'].replace('Yes',1,inplace=True)




# Checking unique attributes of column (Sex)
print('\nPrinting unique attributes of column (Sex)',asd_data.Sex.unique())

# changing attributes
# male   --> 0
# Female --> 1 
asd_data['Sex'].replace('m',0,inplace=True)
asd_data['Sex'].replace('f',1,inplace=True)



# Checking unique attributes of column (Jaundice)
print('\nPrinting unique attributes of column (Jaundice)',asd_data.Jaundice.unique())

# Changing Attributes
# Yes --> 1
# No  --> 0
asd_data['Jaundice'].replace('no',0,inplace=True)
asd_data['Jaundice'].replace('yes',1,inplace=True)



# Checking unique attributes of column (family_member_with_asd)
print('\nPrinting unique attributes of column (family_member_with_asd)',asd_data.Family_mem_with_ASD.unique())

# changing Attributes
# Yes --> 1     
# No  --> 0
asd_data['Family_mem_with_ASD'].replace('no',0,inplace=True)
asd_data['Family_mem_with_ASD'].replace('yes',1,inplace=True)






# printing unique attributes of column (Ethnicity)
print('\nprinting unique attributes of column (Ethnicity)',asd_data.Ethnicity.unique())

# changing attributes
# middle eastern --> 1    
# White European --> 2   
# Hispanic       --> 3
# black          --> 4             
# asian          --> 5
# south asian    --> 6
# Native Indian  --> 7
# Others         --> 8
# Latino         --> 9
# mixed          --> 10
# Pacifica       --> 11
asd_data['Ethnicity'].replace('middle eastern',1,inplace=True)
asd_data['Ethnicity'].replace('White European',2,inplace=True)
asd_data['Ethnicity'].replace('Hispanic',3,inplace=True)
asd_data['Ethnicity'].replace('black',4,inplace=True)
asd_data['Ethnicity'].replace('asian',5,inplace=True)
asd_data['Ethnicity'].replace('south asian',6,inplace=True)
asd_data['Ethnicity'].replace('Native Indian',7,inplace=True)
asd_data['Ethnicity'].replace('Others',8,inplace=True)
asd_data['Ethnicity'].replace('Latino',9,inplace=True)
asd_data['Ethnicity'].replace('mixed',10,inplace=True)
asd_data['Ethnicity'].replace('Pacifica',11,inplace=True)





# printing unique attributes of column (Who_completed_the_test)
print('\nPrinting unique attributes of column (Who_completed_the_test)',asd_data.Who_completed_the_test.unique())

# dropping the below column because they wont be a useful parameter to decide the ASD 
asd_data.drop(['Who_completed_the_test'], axis=1, inplace=True)


print('\nFinal column of the dataset',asd_data.columns)
print('\n\n',asd_data.head())





# Grouping the datasets with respect to class label
data = asd_data.groupby('Class') 

# describing the dataset
df = data.describe()

# saving the described data to excel sheet
df.to_csv('Datasets\data_description.csv')


# saving a processed data to new excel sheet for further transactions
asd_data.to_csv('Datasets\clean_toddlers_data.csv')