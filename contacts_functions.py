import hashlib

def getContactColums():
    contacts_columns = ['Id',
    'IsDeleted',
    'MasterRecordId',
	'AccountId',	
    'Salutation',	
    'FirstName',	
    'LastName',	
    'RecordTypeId',	
    'OtherStreet',	
    'OtherCity',	
    'OtherState',
    'OtherPostalCode',	
    'OtherCountry',	
    'OtherLatitude',	
    'OtherLongitude',	
    'OtherGeocodeAccuracy',
    'MailingStreet',
    'MailingCity',
    'MailingState',	
    'MailingPostalCode',	
    'MailingCountry',
    'MailingLatitude',	
    'MailingLongitude',	
    'MailingGeocodeAccuracy',	
    'Phone',
    'Fax',
    'MobilePhone',	
    'HomePhone',
    'OtherPhone',
    'AssistantPhone',	
    'ReportsToId',
    'Email',
    'Title',
    'Department',	
    'AssistantName',	
    'LeadSource',
    'Birthdate',
    'Description',	
    'OwnerId',
    'HasOptedOutOfEmail',	
    'HasOptedOutOfFax',
    'DoNotCall',
    'CreatedDate',	
    'CreatedById',	
    'LastModifiedDate',	
    'LastModifiedById',
    'SystemModstamp',
    'LastActivityDate',	
    'LastCURequestDate',	
    'LastCUUpdateDate',
    'EmailBouncedReason',	
    'EmailBouncedDate',
    'Jigsaw',
    'JigsawContactId',	
    'IndividualId',
    'Pronouns',
    'GenderIdentity',	
    'PatronDonate__Date_Entered__c',	
    'PatronDonate__Deceased__c',	
    'PatronDonate__Do_Not_Mail__c',	
    'PatronDonate__Donor_Recognition__c',	
    'PatronDonate__External_ID__c',
    'PatronDonate__Formal_Address_Name__c',	
    'PatronDonate__Formal_Salutation__c',
    'PatronDonate__Head_Of_Household__c',
    'PatronDonate__Informal_Address_Name__c',	
    'PatronDonate__Informal_Salutation__c',
    'PatronDonate__Level__c',
    'PatronDonate__Marital_Status__c',	
    'PatronDonate__Philanthropic_Interests__c',	
    'PatronDonate__Spouse_Name__c',
    'PatronDonate__Volunteer_Interests__c,',	
    'PatronDonate__Other_Email__c',
    'PatronDonate__Company__c',
    'PatronSignup__SignupStatus__c',	
    'PatronSignup__SignupSource__c',	
    'PatronDonate__MiddleName__c',	
    'PatronDonate__Suffix__c',	
    'PatronSignup__ContactOrigin__c',	
    'PatronSignup__TargetId__c',
    'PatronSignup__EmailStatus__c',	
    'PatronSignup__ContactForm__c',	
    'PatronTicket__TemporaryPortalPassword__c',	
    'PatronTicket__ActiveBenefits__c',
    'Current_Season_Subscriber__c',
    'Email_Lists__c',
    'X17_18_Subscriber__c',	
    'Board_Member__c',
    'Seating_Accomodation__c',	
    'Reserved_Seating__c',
    'Attending_Next_Dinner__c',	
    'Chocolate_and_Card__c',
    'Legacy_Membership_Circle__c',	
    'Vax_Card__c',
    'PatronTicket__CurrentOrMostRecentBenefitLevel__c',	
    'PatronTicket__LatestBenefitExpiration__c',
    'PatronTicket__MemberRole__c',
    'Email_List_Notes__c'
    ]

    return contacts_columns

def get_merging_dictionary():
    mergDict = {
    'Id': 'contact_id',
    'IsDeleted': 'is_deleted',
#    'MasterRecordId': None,
	'AccountId': 'account_id',	
    'Salutation': 'salutation',	
    'FirstName': 'first_name',	
    'LastName': 'last_name',
#    'RecordTypeId': '',	
    'OtherStreet': 'other_street',	
    'OtherCity': 'other_city',	
    'OtherState': 'other_state',
    'OtherPostalCode': 'other_postal_code',	
    'OtherCountry': 'other_country',	
#    'OtherLatitude',	
#    'OtherLongitude',	
#    'OtherGeocodeAccuracy',
    'MailingStreet': 'mailing_street',
    'MailingCity': 'mailing_city',
    'MailingState': 'mailing_state',	
    'MailingPostalCode': 'mailing_postal_code',	
    'MailingCountry': 'mailing_country',
#    'MailingLatitude',	
#    'MailingLongitude',	
#    'MailingGeocodeAccuracy',	
    'Phone': 'phone',
    'Fax': 'fax',
    'MobilePhone': 'mobile_phone',	
    'HomePhone': 'home_phone',
    'OtherPhone': 'other_phone',
#    'AssistantPhone': 'assistantphone',	
#    'ReportsToId',
    'Email': 'email',
    'Title': 'title',
    'Department': 'department',	
#    'AssistantName',	
#    'LeadSource',
    'Birthdate':'birth_date',
    'Description' : 'description',
#    'OwnerId',
    'HasOptedOutOfEmail': 'has_opted_out_of_email',	
    'HasOptedOutOfFax': 'has_opted_out_of_fax',
    'DoNotCall': 'do_not_call',
    'CreatedDate': 'created_date',	
    'CreatedById': 'created_by_id',	
    'LastModifiedDate': 'last_modified_date',	
    'LastModifiedById': 'last_modified_by_id',
    'SystemModstamp': 'system_modstamp',
    'LastActivityDate': 'las_tactivity_date',	
#    'LastCURequestDate',	
#    'LastCUUpdateDate',
    'EmailBouncedReason': 'email_bounce_reason',	
    'EmailBouncedDate': 'email_bounce_date',
#    'Jigsaw',
#    'JigsawContactId',	
#    'IndividualId',
    'Pronouns': 'pronouns',
    'GenderIdentity': 'gender_identity',	
    'PatronDonate__Date_Entered__c': 'donate_date_entered',	
    'PatronDonate__Deceased__c': 'deceased',	
    'PatronDonate__Do_Not_Mail__c': 'do_not_mail',	
    'PatronDonate__Donor_Recognition__c': 'donor_recognition',	
#    'PatronDonate__External_ID__c',
#    'PatronDonate__Formal_Address_Name__c',	
    'PatronDonate__Formal_Salutation__c': 'formal_salutation',
#    'PatronDonate__Head_Of_Household__c': ,
    'PatronDonate__Informal_Address_Name__c': 'informal_address_name',	
    'PatronDonate__Informal_Salutation__c': 'informal_salutation',
#    'PatronDonate__Level__c',
#    'PatronDonate__Marital_Status__c',	
#    'PatronDonate__Philanthropic_Interests__c',	
#    'PatronDonate__Spouse_Name__c',
    'PatronDonate__Volunteer_Interests__c' : 'volunteer_interests',	
    'PatronDonate__Other_Email__c': 'other_email',
    'PatronDonate__Company__c': 'company',
#    'PatronSignup__SignupStatus__c': 'signupstatus',	
#    'PatronSignup__SignupSource__c',	
    'PatronDonate__MiddleName__c': 'middle_name',	
    'PatronDonate__Suffix__c': 'suffix',	
    'PatronSignup__ContactOrigin__c': 'contact_origin',	
#    'PatronSignup__TargetId__c',
    'PatronSignup__EmailStatus__c': 'email_status',	
#    'PatronSignup__ContactForm__c',	
#    'PatronTicket__TemporaryPortalPassword__c',	
#    'PatronTicket__ActiveBenefits__c': 'activebenefits',
    'Current_Season_Subscriber__c': 'current_season_subscriber',
    'Email_Lists__c': 'email_lists',
#    'X17_18_Subscriber__c',	
    'Board_Member__c': 'board_member',
    'Seating_Accomodation__c': 'seating_accomodation',	
    'Reserved_Seating__c' : 'reserved_seating',
    'Attending_Next_Dinner__c': 'attending_next_dinner',	
    'Chocolate_and_Card__c': 'chocolate_and_card',
    'Legacy_Membership_Circle__c': 'legacy_membership_circle',	
#    'Vax_Card__c',
#    'PatronTicket__CurrentOrMostRecentBenefitLevel__c',	
#    'PatronTicket__LatestBenefitExpiration__c',
#    'PatronTicket__MemberRole__c',
    'Email_List_Notes__c': 'email_list_notes'
    }
    return mergDict

def GetNewColumnsOrder(df):

    # Apply hashing to the 'id' column
    df['contact_id'] = df['contact_id'].apply(lambda x: hash_to_int(x))
    df['account_id'] = df['account_id'].apply(lambda x: hash_to_int(x))
    df['created_by_id'] = df['created_by_id'].apply(lambda x: hash_to_int(x))
    df['last_modified_by_id'] = df['last_modified_by_id'].apply(lambda x: hash_to_int(x))

    # Define the new column order with logical grouping and comments for readability
    new_column_order = [
        # Personal Information
        'contact_id', 'account_id', 'is_deleted', 'salutation', 'first_name', 'middle_name', 'last_name', 'suffix',
        'pronouns', 'gender_identity', 'birth_date',

        # Contact Information
        'email', 'other_email', 'phone', 'mobile_phone', 'home_phone', 'other_phone', 'fax',

        # Address Information
        'mailing_street', 'mailing_city', 'mailing_state', 'mailing_postal_code', 'mailing_country',
        'other_street', 'other_city', 'other_state', 'other_postal_code', 'other_country',

        # Professional Information
        'title', 'department', 'company',

        # Donation and Volunteer Information
        'donate_date_entered', 'donor_recognition', 'formal_salutation', 'informal_salutation',
        'informal_address_name', 'volunteer_interests',

        # Communication Preferences
        'has_opted_out_of_email', 'has_opted_out_of_fax', 'do_not_call', 'do_not_mail', 'email_status',
        'email_list_notes', 'email_lists',

        # System Information
        'created_date', 'created_by_id', 'last_modified_date', 'last_modified_by_id',
        'system_modstamp', 'las_tactivity_date', 'email_bounce_reason', 'email_bounce_date',

        # Membership and Participation
        'current_season_subscriber', 'board_member', 'seating_accomodation', 'reserved_seating',
        'attending_next_dinner', 'chocolate_and_card', 'legacy_membership_circle', 'contact_origin'
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