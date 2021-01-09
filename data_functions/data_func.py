import pandas as pd 

def get_total_msg_exchanged(df):
    """ Return the total amount of messages received and sent.
    """
    return df.shape[0]

def get_total_msg_sent(df, user_name):
    """ Return the total amount of messages the user sent.
    """
    # Get the rows with user name
    user_msg = df[df['sender_name'] == user_name]
    # Get the total count
    user_msg = user_msg.groupby(['sender_name']).count().reset_index()[['sender_name', 'chat_name']].rename(columns = {'chat_name' : 'count'})

    return user_msg['count'].iloc[0]

def get_total_msg_received(df, user_name):
    """ Return the total amount of messages the user received.
    """
    # Get the rows without the user name
    msg = df[df['sender_name'] != user_name]   
    # Get the total count
    msg_received = msg.groupby(['sender_name']).count().reset_index()[['sender_name', 'chat_name']].rename(columns = {'chat_name' : 'count'})

    return msg_received['count'].iloc[0]

def get_top_ppl_sent(df, user_name, num):
    """ Return a dictionary of top 'num' people who sent you the most messages. Excluding group chats.
    Key: name, Value: total messages that person sent you.
    """
    # Finding non group chats
    df = df[df['num_participants'] == 2]

    # Get the rows without the user name
    df = df[df['sender_name'] != user_name]  
    # Get total count 
    df = df.groupby(['sender_name']).count().reset_index()[['sender_name', 'content']].rename(columns = {'content' : 'count'})
    # Sort by descending count
    df = df.sort_values(by = ['count'], ascending = False)
    # Take top 'num' values
    df = df.head(num)
    dic = df.set_index('sender_name').to_dict()

    return dic 

def get_top_ppl_received(df, user_name, num):
    """ Return a dictionary of top 'num' people who you sent the most messages. Excluding group chats.
    Key: name, Value: total messages that you sent that person.
    """
    # Finding non group chats
    df = df[df['num_participants'] == 2]

    # Get the rows without the user name
    df = df[df['sender_name'] == user_name]  
    # Get total count 
    df = df.groupby(['chat_name']).count().reset_index()[['chat_name', 'content']].rename(columns = {'content' : 'count'})
    # Sort by descending count
    df = df.sort_values(by = ['count'], ascending = False)
    # Rename the weird looking chat name
    df['chat_name'] = df['chat_name'].apply(lambda row : row[:row.find("_")] if row.find("_") != -1 else row)
    # Take top 'num' values
    df = df.head(num)
    dic = df.set_index('sender_name').to_dict()

    return dic 

