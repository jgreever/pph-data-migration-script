import pandas as pd
from datetime import datetime
from faker import Faker
import random
import notes_faker as nf
import accounts_faker as af

accounts = pd.read_csv("Gold_tables/Accounts.csv", header=0, encoding='latin-1')
contacts = pd.read_csv("Gold_tables/Contacts.csv", header=0, encoding='latin-1')
notes = pd.read_csv("Gold_tables/Notes.csv", header=0, encoding='latin-1')

fake=Faker()
start_date = datetime(2018,1,1)
end_date = datetime(2023,12,31)

fake_accounts = accounts.iloc[0:0]

#Fake Accounts

types = list(af.account_type.keys())
id = 0
contacts_id = 0
isdeleted = 0
fake_accounts_size = 90
binary = [0,1]

for i in range(fake_accounts_size):
    id = id + 1
    row_entry = af.create_accounts_entry(id, start_date, end_date, types, binary, fake)
    fake_accounts = pd.concat([fake_accounts, row_entry], ignore_index=True)

fake_accounts.to_csv("Faked_tables/fake_accounts.csv", index=False)

#Fakes notes
fake_notes_size = 300

fake_notes = notes.iloc[0:0]

titles = list(nf.email_categories.keys())
id = 0
 
for i in range(fake_notes_size):
    id = id + 1
    isdeleted = 0
    contactid = 0
    accountid = 0
    title = random.choice(titles)
    body = random.choice(nf.email_categories[title])
    created_date  = fake.date_time_between_dates(datetime_start = start_date, datetime_end = end_date)
    last_modified_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
   
    row_entry = pd.DataFrame.from_dict({
       "id": [id],
       "is_deleted": [0],
       "contact_id": [0],
       "account_id": [0],
       "title": [title],
       "body": [body],
       "created_date": [created_date],
       "last_modified_date": [last_modified_date]}
    )

    fake_notes = pd.concat([fake_notes, row_entry], ignore_index=True)

fake_notes.to_csv("Faked_tables/fake_notes.csv", index=False)

def create_contacts_entry(account_input_dictionary, contacts_id):
    contact_row_entry = pd.DataFrame.from_dict({
        'id': [contacts_id],
        'is_deleted' : [0],
        'account_id': [account_input_dictionary[id]],
        'salutation': [0], 
        'first_name': [0],
        'last_name': [0],
        'other_street': [0],	
        'other_city': [0],
        'other_state': [0],
        'other_postal_code': [0],
        'other_country': [0],
        'mailing_street': [0],
        'mailing_city': [0],
        'mailing_state': [0],
        'mailing_postal_code': [0],
        'mailing_country': [0],
        'phone': [0],
        'fax': [0],
        'mobile_phone': [0],
        'home_phone': [0],
        'other_phone': [0],
        'email': [0],
        'title': [0],
        'department': [0],
        'birthdate': [0],	
        'description': [0],
        'has_opted_out_of_email': [0],
        'has_opted_out_of_fax': [0],
        'do_not_call': [0],
        'created_date': [0],
        'created_by_id': [0],
        'last_modified_date': [0],
        'last_modified_by_id': [0],
        'system_mod_stamp': [0],
        'last_activity_date': [0],
        'email_bounce_reason': [0],
        'email_bounce_date': [0],
        'pronouns': [0],
        'gender_identity': [0],
        'donate_date_entered': [0],
        'deceased': [0],
        'do_not_mail': [0],
        'donor_recognition': [0],
        'formal_salutation': [0],
        'informal_address_name': [0],
        'informal_salutation': [0],
        'volunteer_interests': [0],
        'other_email': [0],
        'company': [0],
        'middle_name': [0],
        'suffix': [0],
        'contact_origin': [0],
        'email_status': [0],	
        'current_season_subscriber': [0],
        'email_lists': [0],
        'board_member': [0],
        'seating_accomodation': [0],
        'reserved_seating': [0],	
        'attending_next_dinner': [0],
        'chocolate_and_card': [0],
        'legacy_membership_circle': [0],
        'email_list_notes': [0]
    })