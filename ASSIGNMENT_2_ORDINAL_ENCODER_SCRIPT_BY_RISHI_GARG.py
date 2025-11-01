import pandas as pd 
import numpy as np
def sep():
    print("-"*120)

def ordinal_encoder(raw_data):
    print("We are encoding this csv file:")
    sep()
    print(raw_data.head())
    object_cols=[col for col in raw_data.columns if raw_data[col].dtype=='object']
    sep()
    print(f"So your provided csv file contains these {len(object_cols)} categorical columns which requires encoding:")
    for col in object_cols:
        print(f">>> {col}")
    sep()
    enc_col_ch=input("Enter the proper name of the categorical column you want to encode:")
    if enc_col_ch in object_cols:
        unique_values=raw_data[enc_col_ch].unique()
        #print(unique_values)
        sep()
        print("How do you want to do the Ordinal Encodng?")
        print("1). Alphabetical order(lexicographical order)\n2). Will provide the order for all the unique values in the column" )
        sep()
        enc_style=int(input("Enter the serial number of the ordinal encoding method(1/2):"))
        sorted_uni_val=sorted(unique_values,key=str.lower)
        enc_dict=ord_enc_processing(enc_style,sorted_uni_val,enc_col_ch)
        raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
        enc_col_df=raw_data[enc_col_ch]
        enc_col_array=np.array(enc_col_df)
        enc_col_py_list=list(enc_col_array)
        for element in enc_col_py_list:
             enc_col_py_list[enc_col_py_list.index(element)]=enc_dict[element]
        new_col_name="Encoded_"+enc_col_ch
        encd_col_df=pd.DataFrame({new_col_name:enc_col_py_list})
        encd_col_df.index=raw_enc_col_excl_data.index
        final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
        sep()
        print(f"Here is your {enc_col_ch} encoded dataframe: ");        sep()
        print(final_encoded_df)
        object_cols.remove(enc_col_ch)
        enc_repeator(object_cols,final_encoded_df)
    else:
            print("Entered column name is not a categorical column")

def ord_enc_processing(enc_style,sorted_uni_val,enc_col_ch):
    if enc_style==1:
        enc_dict={}
        for element in sorted_uni_val:
             enc_dict[element]=sorted_uni_val.index(element)
        return enc_dict
    elif enc_style==2:
        print(f"These are the unique values in the column {enc_col_ch} : {sorted_uni_val}")
        user_enc_order=eval(input("Enter the list of unique values in the order you want them to be encoded:"))
        enc_dict={}
        for element in user_enc_order:
            enc_dict[element]=user_enc_order.index(element)
        return enc_dict
    else:
        print("Encoding style does not exist")
            
def enc_repeator(object_cols,final_encoded_df):
    while True:
                    if len(object_cols)>=0:
                        sep()
                        enc_again_ch=input("Do you want to encode the remaining categorical columns(Y/N):")
                        if enc_again_ch.lower() in ["y"]:
                            object_cols.pop()
                            final_encoded_df=encode_again(final_encoded_df)
                            sep()
                            if final_encoded_df==None:
                                sep()
                            else:
                                print("The updated dataframe:");sep()
                                print(final_encoded_df)
                        else:
                            break
                    else:
                        print("You have reached to the end of the program, your dataframe is now free with the problem of categorical columns")
                        break

def encode_again(first_enc_dataframe):
    try:
        sep()
        ordinal_encoder(first_enc_dataframe)
    except Exception as e:
        print("Some error has occured",e)

#STARTING OF THE PROGRAM
raw_data_path_default="D:\\RISHI_GARG_SKILL_STACK\\PYTHON WORKSPACE\\AIMS ASSIGNMENT WEF 20 OCTOBER 2025\\FIRST_MINI_PROJECT_(IMPUTATION_ENCODING)_LOCAL_REPOSITORY\\RAW_DATA.csv"
sep()
print("Welcome to Ordinal Encoder Script ")
sep()
try:
    raw_data_path=input("Enter the absolute path of your csv record file in which you want to ordinal encode the missing values:")
    if raw_data_path != "" :
        raw_data=pd.read_csv(raw_data_path)
        ordinal_encoder(raw_data)
    else:
        print("So you have chosen the default csv file to test this ordinal encoding script")
        raw_data=pd.read_csv(raw_data_path_default)
        ordinal_encoder(raw_data)
except Exception as e:
    sep()
    print("Some error has occured,",e)


