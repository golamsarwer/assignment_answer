import csv
import json
import pandas as pd


#Reading CSV arg as input from command line
data_cases_input = input("Input Data cases file name:")
disease_list_input = input("Input Disease list file name:")
destination_input = input("Input Output file name:")

# read csv arg from cmd


#checking if file is corrupted or not
try:
    # reading data_case csv files
    data_cases_csv = pd.read_csv(data_cases_input)
    #declared in new variable
    data_case = data_cases_csv
    # reading disease_list csv files
    disease_list_csv = pd.read_csv(disease_list_input)

except:
    # reading corrupted csv files
    data_cases_csv = pd.read_csv(data_cases_input, sep='/,', engine='python')
    # reading disease_list csv files
    disease_list_csv = pd.read_csv(disease_list_input)
    #splitting corrupted csv file by ',' separate
    d= data_cases_csv['uuid,datetime,species,number_morbidity,disease_id,number_mortality,total_number_cases,location'].str.split(',', expand=True)
    #Cleaning columns by eliminatng "ABB
    uuid = d[0].str.replace('"ABB', '')
    datetime = d[1].str.replace('"ABB', '')
    species = d[2].str.replace('"ABB', '')
    number_morbidity = d[3].str.replace('"ABB', '')
    #declaring other column names here
    disease_id = d[4]
    number_mortality = d[5]
    total_number_cases = d[6]
    location = d[7]
    extra1 = d[8]
    extra2 = d[9]
    extra3 = d[10]
    #Concat all the columns in dataframe
    dft = pd.concat(
        [uuid, datetime, species, number_morbidity, disease_id, number_mortality, total_number_cases, location, extra1,
         extra2, extra3], axis=1)
    #fillup missing values column with 'NAN'
    dff = dft.fillna('NaN')
    #assigning a list as dfs
    dfs = []
    #iterating each row of corrupted file for replacing values
    for index, dff in dff.iterrows():
        #checking if UUID length is 36 or not
        if len(dff[0]) < 36:
            #assigning initially i = 0
            i = 0
            #Itarating inside corrupted rows
            while i < 36:
                #adding UUID with Datetime for those uuid's part found in datetime column
                dff[0] = dff[0] + dff[1]
                #shifting left after cleaning one rows value.
                dff[1] = dff[1].replace(dff[1], dff[2])
                dff[2] = dff[2].replace(dff[2], dff[3])
                dff[3] = dff[3].replace(dff[3], dff[4])
                dff[4] = dff[4].replace(dff[4], dff[5])
                dff[5] = dff[5].replace(dff[5], dff[6])
                dff[6] = dff[6].replace(dff[6], dff[7])
                dff[7] = dff[7].replace(dff[7], dff[8])
                dff[8] = dff[8].replace(dff[8], dff[9])
                dff[9] = dff[9].replace(dff[9], dff[10])
                # decalaring i = lenght of UUID
                i = len(dff[0])
            # adding this values to dfs list
            dfs.append(dff)

        else:
            # For those don't have corrupted rows adding this values to dfs list
            dfs.append(dff)
    # assigning list data to dataframe
    data_case_qc = pd.DataFrame(dfs)
    # assigning column headers
    data_case_qc.columns = ['uuid', 'datetime', 'species', 'number_morbidity', 'disease_id', 'number_mortality', 'total_number_cases', 'location','extra1',
         'extra2', 'extra3']


    # converting object type to int for marge operation
    data_case_qc['disease_id'] = data_case_qc['disease_id'].astype(int)
    data_case_qc['number_mortality'] = data_case_qc['number_mortality'].astype(int)
    data_case_qc['number_morbidity'] = data_case_qc['number_morbidity'].astype(int)
    data_case_qc['total_number_cases'] = data_case_qc['total_number_cases'].astype(int)
    # assigning values
    data_case = data_case_qc
    print("CSV file were corrupted. It's already fixed by this program")

# using merge function to marge data_cases and disease_list
data_marge= pd.merge(data_case, disease_list_csv, left_on='disease_id', right_on='id')
# group by location
group_by_hospital = data_marge.groupby(['location'])['number_mortality'].sum()

# group by disease
group_by_disease = data_marge.groupby(['name'])['number_mortality'].sum()

# counting total number of case
sum_case = data_marge['total_number_cases'].sum()
# finding avarage of cat
cat_avr = data_marge.loc[data_marge['species'] == 'cat', 'number_morbidity'].mean()
# converting cat_avr value to two decimal value
cat_float = "{:.2f}".format(cat_avr)
#making data for idicator1.json file
indicator_data = {
    "total number of reported cases is": int(sum_case),
    "total number of deaths reported at each location": group_by_hospital.to_dict()
}
#making data for advance.json file
advance_data = {
    "Average number of sick cats reported in reports from villages up to two decimal points": str(cat_float),
    "total number of deaths from each disease": group_by_disease.to_dict()
}

#writing in specified output name from CMS as indicator.json file
with open(destination_input, "w") as outfile:
    json.dump(indicator_data, outfile, indent=1)
#writing in advance.json file
with open("indicators_advanced_1.json", "w") as outfile1:
    json.dump(advance_data, outfile1, indent=1)
