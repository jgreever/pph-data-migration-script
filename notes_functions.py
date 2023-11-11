
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
        'Id': 'id',
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