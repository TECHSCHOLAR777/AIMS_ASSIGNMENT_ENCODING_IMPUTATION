import pandas as pd
import numpy as np
def sep():
    print("-"*120)
def encode_again(first_enc_dataframe):
    try:
        sep()
        print("We are encoding this csv file:")
        sep()
        print(first_enc_dataframe.head())
        raw_data=first_enc_dataframe
        object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
        sep()
        print(f"So your provided csv file contains these {len(object_cols)} categorical columns which requires encoding:")
        for col in object_cols:
            print(f">>> {col}")
        sep()
        enc_col_ch=input("Enter the proper name of the categorical column you want to encode:")
        if enc_col_ch in object_cols:
            unique_values=raw_data[enc_col_ch].unique()
            raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
            enc_col_df=raw_data[enc_col_ch]
            enc_col_array=np.array(enc_col_df)
            enc_col_py_list=list(enc_col_array)
            ohenc_dict={}
            ohenc_dict_keys=[]
            #print(unique_values)
            for element in unique_values:
                key=enc_col_ch+"_"+element
                ohenc_dict_keys.append(key)
            #print(ohenc_dict_keys)
            #print(enc_col_py_list)
            #print(unique_values)
            ohenc_dict_values=[]
            for value in unique_values:
                ele_list=[]
                for key in enc_col_py_list:
                    if value==key:
                        ele_list.append(1)
                    else:
                        ele_list.append(0)
                ohenc_dict_values.append(ele_list)
            #print(ohenc_dict_values)
            for n in range(len(ohenc_dict_keys)):
                ohenc_dict[ohenc_dict_keys[n]]=ohenc_dict_values[n]
            #print(ohenc_dict)
            encd_col_df=pd.DataFrame(ohenc_dict)
            #print(encd_col_df)
            encd_col_df.index=raw_enc_col_excl_data.index
            final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
            sep()
            print(f"Here is your {enc_col_ch} one hot encoded dataframe: ")
            sep()
            print(final_encoded_df)
            return final_encoded_df
        else:
            sep()
            print("Either your entered column is not a categorical column or it doesn't exist! ")
    except:
        print()


raw_data_path_default="D:\\RISHI_GARG_SKILL_STACK\\PYTHON WORKSPACE\\AIMS ASSIGNMENT WEF 20 OCTOBER 2025\\RAW_DATA.csv"
sep()
print("Welcome to One Hot Encoder Script ")
sep()
try:
    raw_data_path=input("Enter the absolute path of your csv record file in which you want to one hot encode the missing values:")
    if raw_data_path != "" :
        raw_data=pd.read_csv(raw_data_path)
        object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
        sep()
        print(f"So your provided csv file contains these {len(object_cols)} categorical columns which requires encoding:")
        for col in object_cols:
            print(f">>> {col}")
        sep()
        enc_col_ch=input("Enter the proper name of the categorical column you want to encode:")
        if enc_col_ch in object_cols:
            unique_values=raw_data[enc_col_ch].unique()
            raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
            enc_col_df=raw_data[enc_col_ch]
            enc_col_array=np.array(enc_col_df)
            enc_col_py_list=list(enc_col_array)
            ohenc_dict={}
            ohenc_dict_keys=[]
            #print(unique_values)
            for element in unique_values:
                key=enc_col_ch+"_"+element
                ohenc_dict_keys.append(key)
            #print(ohenc_dict_keys)
            #print(enc_col_py_list)
            #print(unique_values)
            ohenc_dict_values=[]
            for value in unique_values:
                ele_list=[]
                for key in enc_col_py_list:
                    if value==key:
                        ele_list.append(1)
                    else:
                        ele_list.append(0)
                ohenc_dict_values.append(ele_list)
            #print(ohenc_dict_values)
            for n in range(len(ohenc_dict_keys)):
                ohenc_dict[ohenc_dict_keys[n]]=ohenc_dict_values[n]
            #print(ohenc_dict)
            encd_col_df=pd.DataFrame(ohenc_dict)
            #print(encd_col_df)
            encd_col_df.index=raw_enc_col_excl_data.index
            final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
            sep()
            print(f"Here is your {enc_col_ch} one hot encoded dataframe: ")
            sep()
            print(final_encoded_df)
            object_cols.remove(enc_col_ch)
            while True:
                if len(object_cols)>=1:
                    sep()
                    enc_again_ch=input("Do you want to encode the remaining categorical columns(Y/N):")
                    if enc_again_ch.lower() in ["y"]:
                        object_cols.pop()
                        final_encoded_df=encode_again(final_encoded_df)
                        sep()
                        print("The updated dataframe:");sep()
                        print(final_encoded_df)
                    else:
                        break
                else:
                    print("You have reached to the end of the program, your dataframe is now free with the problem of categorical columns")
                    break
        else:
            sep()
            print("Either your entered column is not a categorical column or it doesn't exist! ")
    else:
        print("So you have chosen the default csv file to test this one hot encoding script")
        raw_data=pd.read_csv(raw_data_path_default)
        object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
        sep()
        print(f"So your provided csv file contains these {len(object_cols)} categorical columns which requires encoding:")
        for col in object_cols:
            print(f">>> {col}")
        sep()
        enc_col_ch=input("Enter the proper name of the categorical column you want to encode:")
        if enc_col_ch in object_cols:
            unique_values=raw_data[enc_col_ch].unique()
            raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
            enc_col_df=raw_data[enc_col_ch]
            enc_col_array=np.array(enc_col_df)
            enc_col_py_list=list(enc_col_array)
            ohenc_dict={}
            ohenc_dict_keys=[]
            #print(unique_values)
            for element in unique_values:
                key=enc_col_ch+"_"+element
                ohenc_dict_keys.append(key)
            #print(ohenc_dict_keys)
            #print(enc_col_py_list)
            #print(unique_values)
            ohenc_dict_values=[]
            for value in unique_values:
                ele_list=[]
                for key in enc_col_py_list:
                    if value==key:
                        ele_list.append(1)
                    else:
                        ele_list.append(0)
                ohenc_dict_values.append(ele_list)
            #print(ohenc_dict_values)
            for n in range(len(ohenc_dict_keys)):
                ohenc_dict[ohenc_dict_keys[n]]=ohenc_dict_values[n]
            #print(ohenc_dict)
            encd_col_df=pd.DataFrame(ohenc_dict)
            #print(encd_col_df)
            encd_col_df.index=raw_enc_col_excl_data.index
            final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
            sep()
            print(f"Here is your {enc_col_ch} one hot encoded dataframe: ")
            sep()
            print(final_encoded_df)
            object_cols.remove(enc_col_ch)
            while True:
                if len(object_cols)>=1:
                    sep()
                    enc_again_ch=input("Do you want to encode the remaining categorical columns(Y/N):")
                    if enc_again_ch.lower() in ["y"]:
                        object_cols.pop()
                        final_encoded_df=encode_again(final_encoded_df)
                        sep()
                        print("The updated dataframe:");sep()
                        print(final_encoded_df)
                    else:
                        break
                else:
                    print("You have reached to the end of the program, your dataframe is now free with the problem of categorical columns")
                    break
        else:
            sep()
            print("Either your entered column is not a categorical column or it doesn't exist! ")              
except Exception as e:
    print("Some error has occured,",e)
