import pandas as pd
import numpy as np
import math as m

raw_data_path_default="D:\\RISHI_GARG_SKILL_STACK\\PYTHON WORKSPACE\\AIMS ASSIGNMENT WEF 20 OCTOBER 2025\\RAW_DATA.csv"
def sep():
    print("*"*120)
def imp_again(first_imp_dataframe):
    try:
        sep()
        print("You are imputing the missing values in the following dataframe:")
        sep()
        print(first_imp_dataframe.head())
        raw_data=first_imp_dataframe
        object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
        int_cols=[col for col in raw_data.columns if raw_data[col].dtype=='int']
        float_cols=[col for col in raw_data.columns if raw_data[col].dtype=='float']
        sep()
        print(f"Your provided csv file contains {len(int_cols)} integer datatype columns, {len(float_cols)} float datatype columns")
        sep()
        print(f"You can impute the following columns as they contain some missing values:")
        print("")
        imp_req_col=[]
        for col in int_cols:
            if raw_data[col].isnull().any():
                print(">>>",col)
                imp_req_col.append(col)
        for col in float_cols:
            if raw_data[col].isnull().any():
                print(">>>",col)
                imp_req_col.append(col)
        sep()
        imp_col_ch=input("Enter the correct name(in every sense) of column in which you want to impute:")
        print("")
        if imp_col_ch in imp_req_col:
            print("Here are some common imputing techniques:")
            print("1). Mean Imputation")
            print("2). Median Impution")
            print("3). Most Frequent Imputation")
            sep()
            print("Choose the imputation technique wisely and put the serial number of the imputation technique ")
            sep()
            imp_teq=int(input("Enter the Imputation technique serial number:"))
            if imp_teq==1:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                imp_value=sum(icpl_ne)/len(icpl_ne)
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of mean imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                return final_imp_result_df
            elif imp_teq==3:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                freq = {}
                for element in icpl_ne:
                     freq[element] = freq.get(element, 0) + 1
                #most_frequent = max(freq, key=freq.get)
                most_frequent=0
                max_frequency=0
                for diff_ele in freq.keys():
                     if freq[diff_ele]>max_frequency:
                          most_frequent=diff_ele
                          max_frequency=freq[diff_ele]
                     else:
                         continue
                #print(most_frequent,max_frequency)  
                imp_value=most_frequent
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of most frequent imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)                
                return final_imp_result_df
            elif imp_teq==2:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                icpl_ne_sort=sorted(icpl_ne)
                if len(icpl_ne_sort)%2!=0:
                    median_value=icpl_ne_sort[((len(icpl_ne_sort)+1)//2)-1]
                else:
                    median_value=(icpl_ne_sort[((len(icpl_ne_sort))//2)-1]+icpl_ne_sort[((len(icpl_ne_sort))//2)+1-1])/2
                imp_value=median_value
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of median imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                return final_imp_result_df
            else:
                print("You have enetered a wrong serial number")
        else:
                print("Your entered column name either does not exist or doesn't have any missing value")
    except Exception as e:
        print("Some error has occured",e)    

sep()
print("Welcome to Imputer Script")
sep()
try:
    raw_data_path=input("Enter the absolute path of your csv record file in which you want to impute the missing values:")
    if raw_data_path != "" :
        raw_data=pd.read_csv(raw_data_path)
        object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
        int_cols=[col for col in raw_data.columns if raw_data[col].dtype=='int']
        float_cols=[col for col in raw_data.columns if raw_data[col].dtype=='float']
        sep()
        print(f"Your provided csv file contains {len(int_cols)} integer datatype columns, {len(float_cols)} float datatype columns")
        sep()
        print(f"You can impute the following columns as they contain some missing values:")
        print("")
        imp_req_col=[]
        for col in int_cols:
            if raw_data[col].isnull().any():
                print(">>>",col)
                imp_req_col.append(col)
        for col in float_cols:
            if raw_data[col].isnull().any():
                print(">>>",col)
                imp_req_col.append(col)
        sep()
        imp_col_ch=input("Enter the correct name(in every sense) of column in which you want to impute:")
        print("")
        if imp_col_ch in imp_req_col:
            print("Here are some common imputing techniques:")
            print("1). Mean Imputation")
            print("2). Median Impution")
            print("3). Most Frequent Imputation")
            sep()
            print("Choose the imputation technique wisely and put the serial number of the imputation technique ")
            sep()
            imp_teq=int(input("Enter the Imputation technique serial number:"))
            if imp_teq==1:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                imp_value=sum(icpl_ne)/len(icpl_ne)
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of mean imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                imp_req_col.remove(imp_col_ch)
                while True:
                    if len(imp_req_col)>=1:
                        sep()
                        imp_again_ch=input("Do you want to impute the missing values in remaining columns(Y/N):")
                        if imp_again_ch.lower() in ["y"]:
                            imp_req_col.pop()
                            final_imp_result_df=imp_again(final_imp_result_df)
                            sep()
                            print("The updated dataframe:");sep()
                            print(final_imp_result_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of missing values in numerical columns")
                        break
            elif imp_teq==3:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                freq = {}
                for element in icpl_ne:
                     freq[element] = freq.get(element, 0) + 1
                #most_frequent = max(freq, key=freq.get)
                most_frequent=0
                max_frequency=0
                for diff_ele in freq.keys():
                     if freq[diff_ele]>max_frequency:
                          most_frequent=diff_ele
                          max_frequency=freq[diff_ele]
                     else:
                         continue
                print(most_frequent,max_frequency)  
                imp_value=most_frequent
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of most frequent imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                imp_req_col.remove(imp_col_ch)
                while True:
                    if len(imp_req_col)>=1:
                        sep()
                        imp_again_ch=input("Do you want to impute the missing values in remaining columns(Y/N):")
                        if imp_again_ch.lower() in ["y"]:
                            imp_req_col.pop()
                            final_imp_result_df=imp_again(final_imp_result_df)
                            sep()
                            print("The updated dataframe:");sep()
                            print(final_imp_result_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of missing values in numerical columns")
                        break
            elif imp_teq==2:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                icpl_ne_sort=sorted(icpl_ne)
                if len(icpl_ne_sort)%2!=0:
                    median_value=icpl_ne_sort[((len(icpl_ne_sort)+1)//2)-1]
                    print(icpl_ne_sort)
                    print(median_value)
                else:
                    median_value=(icpl_ne_sort[((len(icpl_ne_sort))//2)-1]+icpl_ne_sort[((len(icpl_ne_sort))//2)+1-1])/2
                imp_value=median_value
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of median imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                imp_req_col.remove(imp_col_ch)
                while True:
                    if len(imp_req_col)>=1:
                        sep()
                        imp_again_ch=input("Do you want to impute the missing values in remaining columns(Y/N):")
                        if imp_again_ch.lower() in ["y"]:
                            imp_req_col.pop()
                            final_imp_result_df=imp_again(final_imp_result_df)
                            sep()
                            print("The updated dataframe:");sep()
                            print(final_imp_result_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of missing values in numerical columns")
                        break
            else:
                print("You have entered a wrong serial number for imputation technique")

        else:
                print("Your entered column name either does not exist or doesn't have any missing value")
    else:
        print("So you have chosen the default csv file to test this imputation script")
        raw_data=pd.read_csv(raw_data_path_default)
        object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
        int_cols=[col for col in raw_data.columns if raw_data[col].dtype=='int']
        float_cols=[col for col in raw_data.columns if raw_data[col].dtype=='float']
        sep()
        print(f"Your provided csv file contains {len(int_cols)} integer datatype columns, {len(float_cols)} float datatype columns")
        sep()
        print(f"You can impute the following columns as they contain some missing values:")
        print("")
        imp_req_col=[]
        for col in int_cols:
            if raw_data[col].isnull().any():
                print(">>>",col)
                imp_req_col.append(col)
        for col in float_cols:
            if raw_data[col].isnull().any():
                print(">>>",col)
                imp_req_col.append(col)
        sep()
        imp_col_ch=input("Enter the correct name(in every sense) of column in which you want to impute:")
        print("")
        if imp_col_ch in imp_req_col:
            print("Here are some common imputing techniques:")
            print("1). Mean Imputation")
            print("2). Median Impution")
            print("3). Most Frequent Imputation")
            sep()
            print("Choose the imputation technique wisely and put the serial number of the imputation technique ")
            sep()
            imp_teq=int(input("Enter the Imputation technique serial number:"))
            if imp_teq==1:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                imp_value=sum(icpl_ne)/len(icpl_ne)
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of mean imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                imp_req_col.remove(imp_col_ch)
                while True:
                    if len(imp_req_col)>=1:
                        sep()
                        imp_again_ch=input("Do you want to impute the missing values in remaining columns(Y/N):")
                        if imp_again_ch.lower() in ["y"]:
                            imp_req_col.pop()
                            final_imp_result_df=imp_again(final_imp_result_df)
                            sep()
                            print("The updated dataframe:");sep()
                            print(final_imp_result_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of missing values in numerical columns")
                        break
            elif imp_teq==3:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                freq = {}
                for element in icpl_ne:
                     freq[element] = freq.get(element, 0) + 1
                #most_frequent = max(freq, key=freq.get)
                most_frequent=0
                max_frequency=0
                for diff_ele in freq.keys():
                     if freq[diff_ele]>max_frequency:
                          most_frequent=diff_ele
                          max_frequency=freq[diff_ele]
                     else:
                         continue
                print(most_frequent,max_frequency)  
                imp_value=most_frequent
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of most frequent imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                imp_req_col.remove(imp_col_ch)
                while True:
                    if len(imp_req_col)>=1:
                        sep()
                        imp_again_ch=input("Do you want to impute the missing values in remaining columns(Y/N):")
                        if imp_again_ch.lower() in ["y"]:
                            imp_req_col.pop()
                            final_imp_result_df=imp_again(final_imp_result_df)
                            sep()
                            print("The updated dataframe:");sep()
                            print(final_imp_result_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of missing values in numerical columns")
                        break
            elif imp_teq==2:
                raw_imp_col_excl_data=raw_data.drop(imp_col_ch,axis=1)
                imp_col_data=raw_data[imp_col_ch]
                imp_col_data_array=np.array(imp_col_data)
                imp_col_py_list=imp_col_data_array.tolist()
                icpl_ne=[ element for element in imp_col_py_list if not m.isnan(element) ] # m.isnan(element) returns true and false
                #icpl_nane=[ element for element in imp_col_py_list if m.isnan(element) ]
                icpl_ne_sort=sorted(icpl_ne)
                if len(icpl_ne_sort)%2!=0:
                    median_value=icpl_ne_sort[((len(icpl_ne_sort)+1)//2)-1]
                    print(icpl_ne_sort)
                    print(median_value)
                else:
                    median_value=(icpl_ne_sort[((len(icpl_ne_sort))//2)-1]+icpl_ne_sort[((len(icpl_ne_sort))//2)+1-1])/2
                imp_value=median_value
                sep()
                print(f"Program is imputing this value to every missing value in the column '{imp_col_ch}':{imp_value}")
                sep()
                imp_result_col_py_list=[]
                for element in imp_col_py_list:
                    if m.isnan(element):
                        imp_result_col_py_list.append(imp_value)
                    else:
                        imp_result_col_py_list.append(element)
                imp_result_col_df_only=pd.DataFrame(data={imp_col_ch:imp_result_col_py_list})
                imp_result_col_df_only.index=raw_data.index
                final_imp_result_df=pd.concat([raw_imp_col_excl_data,imp_result_col_df_only],axis=1)
                print("Here is the result of median imputation on the provided dataframe")
                sep()
                print(final_imp_result_df)
                imp_req_col.remove(imp_col_ch)
                while True:
                    if len(imp_req_col)>=1:
                        sep()
                        imp_again_ch=input("Do you want to impute the missing values in remaining columns(Y/N):")
                        if imp_again_ch.lower() in ["y"]:
                            imp_req_col.pop()
                            final_imp_result_df=imp_again(final_imp_result_df)
                            sep()
                            print("The updated dataframe:");sep()
                            print(final_imp_result_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of missing values in numerical columns")
                        break
        else:
                print("Your entered column name either does not exist or doesn't have any missing value")
except Exception as e:
    print("Some Error has occured",e)    


