
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
	    'IsDeleted':'isdeleted',
    #    'ParentId':'ParentId',
        'AccountId':'accountid',
        'Title':'title',
    #    'IsPrivate':'IsPrivate',
        'Body':'body',	
    #    'OwnerId':'ownerid',
        'CreatedDate':'createddate',
    #    'CreatedById':'CreatedById',
        'LastModifiedDate':'lastmodifieddate',
    #    'LastModifiedById':'LastModifiedById',
    #    'SystemModstamp':'SystemModstamp'
    }
    return mergDict