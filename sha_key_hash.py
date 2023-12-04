#This file uses SHA256 to hash all of the string IDs from the Salesforce database containing the Portland Playhouse data.
#A file hash dictionary is used to iterate through each of the column ids to hash. This is done
#in order to convert the Salesforce IDs to simpler string datatypes while maitaining the join relationships of the
#original data.

import pandas as pd
import hashlib

#Dictionary of the tables and their corresponding column ids to hash.


file_hash_dictionary = {
    'Accounts.csv':         ['id', 'last_modified_by_id'],
    'Contacts.csv':         ['contact_id', 'account_id', 'created_by_id', 'last_modified_by_id'],
    'Events.csv':           ['event_id', 'owner_id'],
    'Notes.csv':            ['id', 'contact_id', 'account_id'],
    'TicketOrderItems.csv': ['ticket_order_item_name', 'ticket_order_item_id','ticket_order_id',
                            'account_id', 'contact_id', 'event_id',
                            'price_level_id' , 'discount_code_id'],
    'TicketOrders.csv':     ['ticket_order_id', 'account_id', 'contact_id'],
    'Transactions.csv':     ['transaction_id', 'patron_transaction_id', 'ticket_order_id',
                             'item_id', 'ticket_order_item_id'],
    'Opportunity.csv':      ['id', 'accountid', 'contactid', 'campaign_id', 'owner_id', 'donor_id'],
    'Record_type.csv':      ['id']
}

def hash_table_ids(file_hash_dictionary):
    for file_name in file_hash_dictionary:
        server_data = read_csv_file("Gold_tables/" + file_name)
        server_data = hash_columns_list(server_data, file_hash_dictionary[file_name])
        save_to_csv(server_data, "Import_tables/" + file_name)

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def read_csv_file(file_path):
    return pd.read_csv(file_path, header=0, encoding='latin-1')

def hash_columns_list(data_frame, list_of_columns):
    for i in list_of_columns:
        data_frame[i] = data_frame[i].apply(lambda x: hash_to_int(x))
    return data_frame

def hash_to_int(column_value, mod_value=2**32):
    # Create a SHA-256 hash of the column value
    hash_object = hashlib.sha256(str(column_value).encode())
    # Convert the hash to a hexadecimal string
    hex_hash = hash_object.hexdigest()
    # Convert the hexadecimal string to an integer and modulate it
    int_hash = int(hex_hash, 16) % mod_value
    return int_hash

def main():
    hash_table_ids(file_hash_dictionary)


if __name__ == "__main__":
    main()