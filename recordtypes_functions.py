import hashlib

def getRecordTypeColumns():
    record_type_columns = [
        "Id",
        "Name",
        "ModuleNamespace",
        "Description",
        "BusinessProcessId",
        "SobjectType",
        "IsActive",
        "CreatedById",
        "CreatedDate",
        "LastModifiedById",
        "LastModifiedDate",
        "SystemModstamp",
        "IsDeleted"
    ]
    return record_type_columns


def get_merging_dictionary():
    mergeDict = {
        "Id": "record_type_id",
        "Name": "name",
        # "ModuleNamespace": "module_namespace",
        "Description": "description",
        # "BusinessProcessId": "business_process_id",
        "SobjectType": "sobject_type",
        "IsActive": "is_active",
        # "CreatedById": "created_by_id",
        "CreatedDate": "created_date",
        # "LastModifiedById": "last_modified_by_id",
        "LastModifiedDate": "last_modified_date",
        "SystemModstamp": "system_modstamp",
        "IsDeleted": "is_deleted"
    }
    return mergeDict

def getNewColumnsOrder(df):
    # Hash 'id' column
    df['record_type_id'] = df['record_type_id'].apply(lambda x: hash_to_int(x))

    # Define the new column order with logical grouping
    new_column_order = [
        # Primary Identifier
        'record_type_id',

        # Basic Info
        'name',
        'description',
        'sobject_type',

        # Status and Timestamps
        'is_active',
        'created_date',
        'last_modified_date',
        'system_modstamp',
        'is_deleted'
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