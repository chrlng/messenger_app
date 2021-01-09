import os 
import json
import pandas as pd 

def extract():
    """ Returns a dataframe of name, timestamp, content, participants, group chat name. 
    """
    cwd = os.getcwd() 
    inbox_dir = cwd + "/data/inbox"
    # go into inbox 
    os.chdir(inbox_dir)

    main_df = pd.DataFrame(columns = ['sender_name', 'timestamp_ms', 'content', 'num_participants', 'chat_name'])

    # iterate through each chat
    for chat_name in os.listdir(): 
        if chat_name == ".DS_Store":
            continue
        os.chdir(chat_name)
        # Get the json files in this chat 
        json_files = [i for i in os.listdir() if i[-4:] == 'json']
        path_to_json = os.getcwd()
        # iterate through the json files in this chat
        for js in json_files:
            with open(js) as json_file:
                # clean and extract data
                json_text = json.load(json_file)
                participants = json_text["participants"]
                msg_lst = json_text["messages"]
                df = pd.DataFrame.from_dict(msg_lst)
                ppl = pd.DataFrame.from_dict(participants)
                # adding in columns
                ppl_lst = list(ppl['name'])
                df["num_participants"] = len(ppl_lst)
                df["chat_name"] = chat_name
                # append this json file data to main df
                main_df = main_df.append(df, ignore_index = True)
        os.chdir(inbox_dir)

    # select columns of interest
    main_df = main_df[['sender_name', 'timestamp_ms', 'content', 'num_participants', 'chat_name']]

    return main_df

def clean_df(df):
    """ Clean the data frame. 
        1. Convert the timestamp_ms to datetime object.
        2. Add in month, day, year columns
    """
    df['timestamp'] = pd.to_datetime(df['timestamp_ms'], unit = 'ms')
    df['year'] = pd.DatetimeIndex(df['timestamp']).year
    df['month'] = pd.DatetimeIndex(df['timestamp']).month
    df['day'] = pd.DatetimeIndex(df['timestamp']).day
    return df 
