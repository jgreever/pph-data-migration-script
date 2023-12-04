import pandas as pd
from datetime import datetime
from faker import Faker
import random
import notes_faker as nf
import accounts_faker as af

accounts = pd.read_csv("Database_Munge/accounts.csv", header=0, encoding='latin-1')
contacts = pd.read_csv("Database_Munge/contacts.csv", header=0, encoding='latin-1')
notes = pd.read_csv("Database_Munge/notes.csv", header=0, encoding='latin-1')

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
    isdeleted = 0
    account_type = random.choice(types)
    name = random.choice(af.account_type[account_type])
    shipping_street = fake.building_number() + ' ' + fake.street_name() + ' ' + fake.street_suffix()
    shipping_city = fake.city()
    shipping_state = fake.state()
    shipping_postal_code = fake.zipcode()
    shipping_country = fake.country()
    
    phone = fake.phone_number()
    fax = fake.phone_number()
    website = fake.url()
    created_date  = fake.date_time_between_dates(datetime_start = start_date, datetime_end = end_date)
    last_modified_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
    last_modified_by_id = 0
    last_activity_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
    
    do_not_call = random.choice(binary)
    do_not_mail = random.choice(binary)
    donor_recognition = random.choice([name, 'Anonymous', ''])
    donor_email = fake.email()
    has_opted_out_of_email = random.choice(binary)
    informal_address_name = ''
    new_name = name

    if (account_type == 'Household'):
        new_name = new_name[0] + ' and ' + new_name[1]
        informal_salutation = str(name[0].split(' ', 1)) + ' and ' + str(name[1].split(' ', 4))
    elif (account_type == 'Individual'):
        informal_salutation = str(name[0].split(' ', 1))
    else:
        informal_salutation = ''

    attn = ''
    grant_size = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,10000,50000])
    will_give_to = random.choice(['Arts, Culture and Humanities', 'Education', 'Charity', '' , '', '' ,'','',''])
    first_donation_date = fake.date_time_between_dates(datetime_start = start_date, datetime_end = end_date)
    last_donation_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
    lifetime_donation_history_amount = random.randint(0, 600000)

    if (lifetime_donation_history_amount > 0):
        lifetime_donation_number = random.randint(0,100)
        this_year_donation_history_amount = random.randint(0,100000)
        amount_donated_this_fiscal_year = this_year_donation_history_amount
        last_donation_amount = random.randint(0,10000)
    else: 
        lifetime_donation_number = 0
        this_year_donation_history_amount = 0
        amount_donated_this_fiscal_year = 0
        last_donation_amount = 0
    
    lifetime_single_ticket_amount = random.choice([random.randint(0,10000),0])
    lifetime_subscription_amount = random.choice([random.randint(0,10000)])                                         
    board_member = 0
    show_sponsor = 0
    seating_accomodation = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,1])
    grant_size = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,10000,50000,100000])

    remainder = lifetime_donation_history_amount
    amount_donated_FY18 = random.randint(0, lifetime_donation_history_amount)
    remainder = remainder - amount_donated_FY18
    amount_donated_FY19 = random.randint(0, remainder)
    remainder = remainder - amount_donated_FY19
    amount_donated_FY20 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY20
    amount_donated_FY21 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY21
    amount_donated_FY22 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY22
    amount_donated_FY23 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY23
    amount_donated_FY24 = 0
    amount_donated_last_fiscal_year = amount_donated_FY23
    largest_donation_date = fake.date_time_between_dates(datetime_start = first_donation_date, datetime_end = end_date)
    lifedtime_donations_included_pledged = lifetime_donation_history_amount
    first_donationdate_incl_pledged = first_donation_date
    first_donation_amount = random.randint(0,lifetime_donation_history_amount)
    
    account_row_entry = pd.DataFrame.from_dict({
        'id': [id],
        'is_deleted': [isdeleted],
        'name': [new_name],
        'type': [account_type],
        'shipping_street': [shipping_street],
        'shipping_city': [shipping_city],
        'shipping_state': [shipping_state],
        'shipping_postal_code': [shipping_postal_code],
        'shipping_country': [shipping_country],
        'phone': [phone],
        'fax': [fax],
        'website': [website],
        'created_date': [created_date],
        'last_modified_date': [last_modified_date],
        'last_modified_by_id': [last_modified_by_id],
        'last_activity_date': [last_activity_date],
        'do_not_call': [do_not_call],
        'do_not_mail': [do_not_mail],
        'donor_recognition': [new_name],
        'donor_email': [donor_email],
        'has_opted_out_of_email': [has_opted_out_of_email],
        'informal_address_name': [informal_address_name],
        'attn': [attn],
        'grant_size': [grant_size],
        'will_give_to': [will_give_to],
        'first_donation_date': [first_donation_date],
        'last_donation_date': [last_donation_date],
        'lifetime_donation_history_amount': [lifetime_donation_history_amount/100],
        'lifetime_donation_number': [lifetime_donation_number],
        'this_year_donation_history_amount': [this_year_donation_history_amount/100],
        'amount_donated_this_fiscal_year': [amount_donated_this_fiscal_year/100],
        'last_donation_amount': [last_donation_amount],
        'lifetime_single_ticket_amount': [lifetime_single_ticket_amount],
        'lifetime_subscription_amount': [lifetime_subscription_amount],
        'board_member': [board_member],	
        'show_sponsor': [show_sponsor],	
        'seating_accomodation' : [seating_accomodation],
        'amount_donated_CY20' : [amount_donated_FY20/100],
        'amount_donated_CY18' : [amount_donated_FY18/100],
        'sort_name': [name],
        'amount_donated_last_fiscal_year': [amount_donated_last_fiscal_year/100],
        'amount_donated_CY21': [amount_donated_FY21/100],	
        'amount_donated_CY19': [amount_donated_FY19/100],
        'amount_donated_FY20': [amount_donated_FY20/100],
        'amount_donated_FY19': [amount_donated_FY19/100],
        'amount_donated_FY18': [amount_donated_FY18/100],
        'lifetime_donations_included_pledged': [lifedtime_donations_included_pledged/100],
        'first_donation_date_incl_pledged': [first_donationdate_incl_pledged],
        'amount_donated_FY21': [amount_donated_FY21/100],
        'first_donation_amount': [first_donation_amount/100],
        'largest_donation_date': [largest_donation_date],
        'amount_donated_FY22': [amount_donated_FY22/100],	
        'amount_Donated_FY23': [amount_donated_FY23/100],
        'amount_Donated_FY24': [amount_donated_FY24/100]
    })

    fake_accounts = pd.concat([fake_accounts, row_entry], ignore_index=True)

fake_accounts.to_csv("Database_Fake/fake_accounts.csv", index=False)

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

fake_notes.to_csv("Database_Fake/fake_notes.csv", index=False)

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

def create_accounts_entry(id, start_date, end_date, types, binary):

    isdeleted = 0
    account_type = random.choice(types)
    name = random.choice(af.account_type[account_type])
    shipping_street = fake.building_number() + ' ' + fake.street_name() + ' ' + fake.street_suffix()
    shipping_city = fake.city()
    shipping_state = fake.state()
    shipping_postal_code = fake.zipcode()
    shipping_country = fake.country()
    
    phone = fake.phone_number()
    fax = fake.phone_number()
    website = fake.url()
    created_date  = fake.date_time_between_dates(datetime_start = start_date, datetime_end = end_date)
    last_modified_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
    last_modified_by_id = 0
    last_activity_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
    
    do_not_call = random.choice(binary)
    do_not_mail = random.choice(binary)
    donor_recognition = random.choice([name, 'Anonymous', ''])
    donor_email = fake.email()
    has_opted_out_of_email = random.choice(binary)
    informal_address_name = ''
    new_name = name

    if (account_type == 'Household'):
        new_name = new_name[0] + ' and ' + new_name[1]
        informal_salutation = str(name[0].split(' ', 1)) + ' and ' + str(name[1].split(' ', 4))
    elif (account_type == 'Individual'):
        informal_salutation = str(name[0].split(' ', 1))
    else:
        informal_salutation = ''

    attn = ''
    grant_size = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,10000,50000])
    will_give_to = random.choice(['Arts, Culture and Humanities', 'Education', 'Charity', '' , '', '' ,'','',''])
    first_donation_date = fake.date_time_between_dates(datetime_start = start_date, datetime_end = end_date)
    last_donation_date = fake.date_time_between_dates(datetime_start = created_date, datetime_end = end_date)
    lifetime_donation_history_amount = random.randint(0, 600000)

    if (lifetime_donation_history_amount > 0):
        lifetime_donation_number = random.randint(0,100)
        this_year_donation_history_amount = random.randint(0,100000)
        amount_donated_this_fiscal_year = this_year_donation_history_amount
        last_donation_amount = random.randint(0,10000)
    else: 
        lifetime_donation_number = 0
        this_year_donation_history_amount = 0
        amount_donated_this_fiscal_year = 0
        last_donation_amount = 0
    
    lifetime_single_ticket_amount = random.choice([random.randint(0,10000),0])
    lifetime_subscription_amount = random.choice([random.randint(0,10000)])                                         
    board_member = 0
    show_sponsor = 0
    seating_accomodation = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,1])
    grant_size = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,10000,50000,100000])

    remainder = lifetime_donation_history_amount
    amount_donated_FY18 = random.randint(0, lifetime_donation_history_amount)
    remainder = remainder - amount_donated_FY18
    amount_donated_FY19 = random.randint(0, remainder)
    remainder = remainder - amount_donated_FY19
    amount_donated_FY20 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY20
    amount_donated_FY21 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY21
    amount_donated_FY22 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY22
    amount_donated_FY23 = random.randint(0,remainder)
    remainder = remainder - amount_donated_FY23
    amount_donated_FY24 = 0
    amount_donated_last_fiscal_year = amount_donated_FY23
    largest_donation_date = fake.date_time_between_dates(datetime_start = first_donation_date, datetime_end = end_date)
    lifedtime_donations_included_pledged = lifetime_donation_history_amount
    first_donationdate_incl_pledged = first_donation_date
    first_donation_amount = random.randint(0,lifetime_donation_history_amount)
    
    account_row_entry = pd.DataFrame.from_dict({
        'id': [id],
        'is_deleted': [isdeleted],
        'name': [new_name],
        'type': [account_type],
        'shipping_street': [shipping_street],
        'shipping_city': [shipping_city],
        'shipping_state': [shipping_state],
        'shipping_postal_code': [shipping_postal_code],
        'shipping_country': [shipping_country],
        'phone': [phone],
        'fax': [fax],
        'website': [website],
        'created_date': [created_date],
        'last_modified_date': [last_modified_date],
        'last_modified_by_id': [last_modified_by_id],
        'last_activity_date': [last_activity_date],
        'do_not_call': [do_not_call],
        'do_not_mail': [do_not_mail],
        'donor_recognition': [new_name],
        'donor_email': [donor_email],
        'has_opted_out_of_email': [has_opted_out_of_email],
        'informal_address_name': [informal_address_name],
        'attn': [attn],
        'grant_size': [grant_size],
        'will_give_to': [will_give_to],
        'first_donation_date': [first_donation_date],
        'last_donation_date': [last_donation_date],
        'lifetime_donation_history_amount': [lifetime_donation_history_amount/100],
        'lifetime_donation_number': [lifetime_donation_number],
        'this_year_donation_history_amount': [this_year_donation_history_amount/100],
        'amount_donated_this_fiscal_year': [amount_donated_this_fiscal_year/100],
        'last_donation_amount': [last_donation_amount],
        'lifetime_single_ticket_amount': [lifetime_single_ticket_amount],
        'lifetime_subscription_amount': [lifetime_subscription_amount],
        'board_member': [board_member],	
        'show_sponsor': [show_sponsor],	
        'seating_accomodation' : [seating_accomodation],
        'amount_donated_CY20' : [amount_donated_FY20/100],
        'amount_donated_CY18' : [amount_donated_FY18/100],
        'sort_name': [name],
        'amount_donated_last_fiscal_year': [amount_donated_last_fiscal_year/100],
        'amount_donated_CY21': [amount_donated_FY21/100],	
        'amount_donated_CY19': [amount_donated_FY19/100],
        'amount_donated_FY20': [amount_donated_FY20/100],
        'amount_donated_FY19': [amount_donated_FY19/100],
        'amount_donated_FY18': [amount_donated_FY18/100],
        'lifetime_donations_included_pledged': [lifedtime_donations_included_pledged/100],
        'first_donation_date_incl_pledged': [first_donationdate_incl_pledged],
        'amount_donated_FY21': [amount_donated_FY21/100],
        'first_donation_amount': [first_donation_amount/100],
        'largest_donation_date': [largest_donation_date],
        'amount_donated_FY22': [amount_donated_FY22/100],	
        'amount_Donated_FY23': [amount_donated_FY23/100],
        'amount_Donated_FY24': [amount_donated_FY24/100]
    })

    return account_row_entry