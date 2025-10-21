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
            #print(unique_values)
            sep()
            print("How do you want to do the Ordinal Encodng?")
            print("1). Alphabetical order(lexicographical order)\n2). Will provide the order for all the unique values in the column" )
            sep()
            enc_style=input("Enter the serial number of the ordinal encoding method(1/2):")
            if enc_style=="1":
                sorted_uni_val=sorted(unique_values,key=str.lower)
                enc_dict={}
                for element in sorted_uni_val:
                    enc_dict[element]=sorted_uni_val.index(element)
                #print(enc_dict)
                raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
                enc_col_df=raw_data[enc_col_ch]
                enc_col_array=np.array(enc_col_df)
                enc_col_py_list=list(enc_col_array)
                #print(enc_col_py_list)
                for element in enc_col_py_list:
                    enc_col_py_list[enc_col_py_list.index(element)]=enc_dict[element]
                #print(enc_col_py_list)
                new_col_name="Encoded_"+enc_col_ch
                encd_col_df=pd.DataFrame({new_col_name:enc_col_py_list})
                #print(encd_col_df)
                encd_col_df.index=raw_enc_col_excl_data.index
                final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
                sep()
                print(f"Here is your {enc_col_ch} encoded dataframe: ")
                sep()
                print(final_encoded_df)
                return final_encoded_df
            elif enc_style=="2":
                sorted_uni_val=sorted(unique_values,key=str.lower)
                print(f"These are the unique values in the column {enc_col_ch} : {sorted_uni_val}")
                user_enc_order=eval(input("Enter the list of unique values in the order you want them to be encoded:"))
                enc_dict={}
                for element in user_enc_order:
                    enc_dict[element]=user_enc_order.index(element)
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
                print(f"Here is your {enc_col_ch} encoded dataframe: ")
                sep()
                print(final_encoded_df)
                return final_encoded_df
            else:
                print("Entered number does not correspond with any of the ordinal encoding technique")
        else:
            print("Entered column name is not a categorical column")
    except Exception as e:
        print("Some error has occured",e)



raw_data_path_default="D:\\RISHI_GARG_SKILL_STACK\\PYTHON WORKSPACE\\AIMS ASSIGNMENT WEF 20 OCTOBER 2025\\RAW_DATA.csv"
sep()
print("Welcome to Ordinal Encoder Script ")
sep()
try:
    raw_data_path=input("Enter the absolute path of your csv record file in which you want to ordinal encode the missing values:")
    if raw_data_path != "" :
        raw_data=pd.read_csv(raw_data_path)
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
            enc_style=input("Enter the serial number of the ordinal encoding method(1/2):")
            if enc_style=="1":
                sorted_uni_val=sorted(unique_values,key=str.lower)
                enc_dict={}
                for element in sorted_uni_val:
                    enc_dict[element]=sorted_uni_val.index(element)
                #print(enc_dict)
                raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
                enc_col_df=raw_data[enc_col_ch]
                enc_col_array=np.array(enc_col_df)
                enc_col_py_list=list(enc_col_array)
                #print(enc_col_py_list)
                for element in enc_col_py_list:
                    enc_col_py_list[enc_col_py_list.index(element)]=enc_dict[element]
                #print(enc_col_py_list)
                new_col_name="Encoded_"+enc_col_ch
                encd_col_df=pd.DataFrame({new_col_name:enc_col_py_list})
                #print(encd_col_df)
                encd_col_df.index=raw_enc_col_excl_data.index
                final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
                sep()
                print(f"Here is your {enc_col_ch} encoded dataframe: ")
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
            elif enc_style=="2":
                sorted_uni_val=sorted(unique_values,key=str.lower)
                print(f"These are the unique values in the column {enc_col_ch} : {sorted_uni_val}")
                user_enc_order=eval(input("Enter the list of unique values in the order you want them to be encoded:"))
                enc_dict={}
                for element in user_enc_order:
                    enc_dict[element]=user_enc_order.index(element)
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
                print(f"Here is your {enc_col_ch} encoded dataframe: ")
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
                print("Entered number does not correspond with any of the ordinal encoding technique")
        else:
            print("Entered column name is not a categorical column")
    else:
        print("So you have chosen the default csv file to test this ordinal encoding script")
        raw_data=pd.read_csv(raw_data_path_default)
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
            enc_style=input("Enter the serial number of the ordinal encoding method(1/2):")
            if enc_style=="1":
                sorted_uni_val=sorted(unique_values,key=str.lower)
                enc_dict={}
                for element in sorted_uni_val:
                    enc_dict[element]=sorted_uni_val.index(element)
                #print(enc_dict)
                raw_enc_col_excl_data=raw_data.drop(enc_col_ch,axis=1)
                enc_col_df=raw_data[enc_col_ch]
                enc_col_array=np.array(enc_col_df)
                enc_col_py_list=list(enc_col_array)
                #print(enc_col_py_list)
                for element in enc_col_py_list:
                    enc_col_py_list[enc_col_py_list.index(element)]=enc_dict[element]
                #print(enc_col_py_list)
                new_col_name="Encoded_"+enc_col_ch
                encd_col_df=pd.DataFrame({new_col_name:enc_col_py_list})
                #print(encd_col_df)
                encd_col_df.index=raw_enc_col_excl_data.index
                final_encoded_df=pd.concat([raw_enc_col_excl_data,encd_col_df],axis=1)
                sep()
                print(f"Here is your {enc_col_ch} encoded dataframe: ")
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
            elif enc_style=="2":
                sorted_uni_val=sorted(unique_values,key=str.lower)
                print(f"These are the unique values in the column {enc_col_ch} : {sorted_uni_val}")
                user_enc_order=eval(input("Enter the list of unique values in the order you want them to be encoded:"))
                enc_dict={}
                for element in user_enc_order:
                    enc_dict[element]=user_enc_order.index(element)
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
                print(f"Here is your {enc_col_ch} encoded dataframe: ")
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
                print("Entered number does not correspond with any of the ordinal encoding technique")
        else:
            print("Entered column name is not a categorical column")
except Exception as e:
    sep()
    print("Some error has occured,",e)