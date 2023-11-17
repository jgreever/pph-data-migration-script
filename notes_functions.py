import hashlib

def getNotesColumns():
    notes_columns = [
    'Id',
	'IsDeleted',
    'ParentId',
    'AccountId',
    'Title',
    'IsPrivate',
    'Body',	
    'OwnerId',
    'CreatedDate',
    'CreatedById',
    'LastModifiedDate',
    'LastModifiedById',
    'SystemModstamp'
    ]

    return notes_columns

def get_merging_dictionary():
    mergDict = {
        'Id': 'note_id',
	    'IsDeleted':'is_deleted',
        'ParentId':'contact_id',
        'AccountId':'account_id',
        'Title':'title',
    #    'IsPrivate':'IsPrivate',
        'Body':'body',	
    #    'OwnerId':'ownerid',
        'CreatedDate':'created_date',
    #    'CreatedById':'CreatedById',
        'LastModifiedDate':'last_modified_date',
    #    'LastModifiedById':'LastModifiedById',
    #    'SystemModstamp':'SystemModstamp'
    }
    return mergDict

def getNewColumnsOrder(df):
    # Hash ID columns first
    df['note_id'] = df['note_id'].apply(lambda x: hash_to_int(x))
    df['is_deleted'] = df['is_deleted'].apply(lambda x: hash_to_int(x))
    df['contact_id'] = df['contact_id'].apply(lambda x: hash_to_int(x))
    df['account_id'] = df['account_id'].apply(lambda x: hash_to_int(x))

    # Define the new column order with logical grouping
    new_column_order = [
        # Hashed Identifiers
        'note_id',
        'is_deleted',
        'contact_id',
        'account_id',

        # Other Columns
        'title',
        'body',
        'created_date',
        'last_modified_date'
        # Add other columns as needed
    ]

    # Reorder the DataFrame columns
    df = df[new_column_order]

    return df

def hash_to_int(column_value, mod_value=2**32):
    # Create a SHA-256 hash of the column value
    hash_object = hashlib.sha256(str(column_value).encode())
    # Convert the hash to a hexadecimal string
    hex_hash = hash_object.hexdigest()
    # Convert the hexadecimal string to an integer and modulate it
    int_hash = int(hex_hash, 16) % mod_value
    return int_hash