#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# Exploring enron_data and features

# for key, val in enron_data.items():
#     print(key, val)

# # Counting Person of Interest POI

# cnt=0

# for key, val in enron_data.items():
#     if val['poi'] == True:
#         cnt += 1
# print(cnt)

# # # total stock value for  James Prentice

# print(enron_data['PRENTICE JAMES']['total_stock_value'])

# # How many email messages do we have from Wesley Colwell to persons of interest?

# print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# # What's the value of stock options exercised by Jeffrey K Skilling

# print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# # Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of 'total_payments' feature)?

# print(enron_data['SKILLING JEFFREY K']['total_payments'])
# print(enron_data['FASTOW ANDREW S']['total_payments'])
# print(enron_data['LAY KENNETH L']['total_payments'])

# # How many folks in this dataset have a quantified salary? What about a known email address?

# cnt_salary, cnt_email = 0, 0
# for key, val in enron_data.items():
#     if val['salary'] != 'NaN':
#         cnt_salary += 1
#     if val['email_address'] != 'NaN':
#         cnt_email += 1
# print(cnt_salary, cnt_email)

# Answering Optional Quizzes

# How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments? What percentage of people in the dataset as a whole is this?

# cnt = 0

# for key, val in enron_data.items():
#     if val['total_payments'] == 'NaN':
#         cnt += 1 

# print((cnt * 100)/len(enron_data))

# How many POIs in the E+F dataset have "NaN" for their total payments? What percentage of POI's as a whole is this?

cnt_nan, cnt_poi = 0, 0
for key, val in enron_data.items():
    if val['poi'] == True:
        cnt_poi += 1
        if val['total_payments'] == 'NaN':
            cnt_nan += 1
print(cnt_nan, cnt_poi)