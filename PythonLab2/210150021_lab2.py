#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
pd.options.display.max_colwidth = 500


# In[2]:


SCHOOL_NAME = 'Mehta Family School of Data Science & AI'
UG_STUDENT_COUNT = 52
PHD_STUDENT_COUNT = 11


# In[3]:


df = pd.read_csv("DA213_class_02_faculty_data.csv")


# In[4]:


col_names = list(df.columns)
faculty_count = len(df)


# In[5]:


faculty_pool = {}
keys = list(df.Name)

for key in keys:
    
    faculty_pool[key] = {}
    keys_faculty = ['Name', 'Research Interests', 'Association', 'Affiliation', 'email', 'phone', 'website', 'Research Interests']
    
    for key_faculty in keys_faculty:
        
        faculty_pool[key][key_faculty] = df.loc[df.Name == key][key_faculty].to_string(index = False)


# In[6]:


def home_screen():
    os.system('clear')
    
    print(f"Hello {username}! Following is some information about our school:\n")
    print(f"We have {faculty_count} faculty")
    print(f"We have {UG_STUDENT_COUNT} UG Students and {PHD_STUDENT_COUNT} PhD Students\n\n")

    ip = input("Please enter:\n1 - To See Faculty List\nq - To Exit\n")

    if ip=='1':
        faculty_list()
        
    elif ip=='q':
        exit()
        
    else:
        print("Please enter a valid input\n")
        input("Press any key to continue")
        home_screen()


# In[1]:


def faculty_list():
    os.system('clear')
    
    print(df.Name.sort_values().to_string(index = False))
    
    print("\n")
    
    print("Please enter:")
    ip = input("Faculty First Name to Know More\n2 - Go Home\nq - To Exit\n")
    
    Bool = False
    
    for i in range(len(keys)):
        if ip in keys[i]:
            Bool = True
            fac_name = keys[i]
            break
    
    if ip=='2':
        home_screen()
        
    elif ip=='q':
        exit()
        
    elif Bool==True:
        faculty_info(fac_name)
    
    else:
        print("Please enter a valid faculty name\n")
        input("Press any key to continue\n")
        faculty_list() 


# In[8]:


def faculty_info(fac_name):
    os.system('clear')
    
    print(f"Faculty Name: {fac_name}")
    print(f"Department: {faculty_pool[fac_name]['Affiliation']}")
    print(f"Phone Number: {faculty_pool[fac_name]['phone']}")
    print(f"Email: {faculty_pool[fac_name]['email']}")
    print(f"Research Interests: {faculty_pool[fac_name]['Research Interests']}\n")
    
    print("\nPlease enter:")
    ip = input("1 - To save the above information in a .txt file\n2 - Go Home\nq - To exit\n")
    
    if ip=='1':
        write_file(fac_name)
        
    elif ip=='2':
        home_screen()
        
    elif ip=='q':
        exit()
        
    else:
        print("Please enter a valid input\n")
        input("Press any key to continue\n")
        faculty_info(fac_name)


# In[9]:


def write_file(fac_name):

        filename = username
        full_name = fac_name.split()
        
        for i in range(len(full_name)):
            filename += "_"+full_name[i]
        
        filename+=".txt"
        file = open(filename, mode = "w")
        
        file.write(f"Faculty Name: {fac_name}\n")
        file.write(f"Department: {faculty_pool[fac_name]['Affiliation']}\n")
        file.write(f"Phone Number: {faculty_pool[fac_name]['phone']}\n")
        file.write(f"Email: {faculty_pool[fac_name]['email']}\n")
        file.write(f"Research Interests: {faculty_pool[fac_name]['Research Interests']}\n")
        
        file.close()
        
        print(f"\n\nFile saved as {filename}\n")
        print("Please enter:")
        
        ip = input("2 - Go Home\nq - To exit\n")
        
        if ip=='2':
            home_screen()
            
        elif ip=='q':
            exit()


# In[2]:


print("********Welcome to Nityam's Interface!********\n\n")
username = input("Please enter your name: ")

os.system('clear')
home_screen()


# In[ ]:




