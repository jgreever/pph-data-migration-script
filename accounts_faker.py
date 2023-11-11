import random
import pandas as pd
from faker import Faker

accounts_fake = Faker()

def create_accounts_entry(id, start_date, end_date, types, binary, fake):
    isdeleted = 0
    account_type_choice = random.choice(types)
    name = random.choice(account_type[account_type_choice])
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

    if (account_type_choice == 'Household'):
        new_name = new_name[0] + ' and ' + new_name[1]
        informal_salutation = str(name[0].split(' ', 1)) + ' and ' + str(name[1].split(' ', 4))

    elif (account_type_choice == 'Individual'):
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
        'type': [account_type_choice],
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

fictional_corporations = [
    "Weyland-Yutani Corporation",
    "Umbrella Corporation",
    "Tyrell Corporation",
    "Initech",
    "Buy N Large (BNL)",
    "Soylent Corporation",
    "Omni Consumer Products (OCP)",
    "Skynet",
    "Cyberdyne Systems",
    "Hooli",
    "Wayne Enterprises",
    "Oscorp Industries",
    "LexCorp",
    "Virtucon",
    "Encom",
    "The Network",
    "Massive Dynamic",
    "Monsters, Inc.",
    "The Galactic Empire",
    "The Galactic Federation",
    "Zorg Industries",
    "The Ministry of Magic",
    "Bluth Company",
    "Warbucks Corporation",
    "Spacely Space Sprockets",
    "Mr. Robot Corporation",
    "The Umbrella Academy",
    "Ouroboros Corporation",
    "Cortex Pharmaceuticals",
    "FrobozzCo International",
]

fictional_nonprofits = [
    "Hope Haven Foundation",
    "GlobeSavers",
    "Charity Champions",
    "Kindness Matters Initiative",
    "Unity for All Foundation",
    "Caring Hearts Alliance",
    "Empowerment for Change",
    "Community Upliftment Network",
    "Healing Hands Society",
    "Visionary Dreams Foundation"
]

fictional_schools = [
    "Hogwarts School of Witchcraft and Wizardry",
    "Xavier's School for Gifted Youngsters",
    "Springfield Elementary School",
    "Sunnydale High School",
    "Gryffindor House",
    "Starfleet Academy",
    "Rydell High School",
    "South Harmon Institute of Technology",
    "Hillman College",
    "Hogwarts School of Muggle Art and Music" ]

fictional_businesses = [
    "TechMasters Innovations",
    "GreenLeaf EcoCafe",
    "StarNova Space Travel",
    "Frosty Delights Ice Cream Shop",
    "The Paper Trail Bookstore",
    "Paws and Play Pet Grooming",
    "AquaWave Surf Shop",
    "Mystic Potions Apothecary",
    "SunnySide Bakery & Cafe",
    "Galactic Gear Emporium"
]

fictional_foundations = [
    "Legacy of Light Foundation",
    "EcoGuardian Foundation",
    "Hope Renewal Foundation",
    "Artistic Horizons Foundation",
    "DreamBuilders Legacy Foundation",
    "Cultural Unity Foundation",
    "Infinite Wellness Foundation",
    "Community Empowerment Foundation",
    "Harmony Haven Foundation",
    "Science for Humanity Foundation"
]

account_type = {
    'Individual': [accounts_fake.name()],
    'Household': [[accounts_fake.name(), accounts_fake.name()]],
    'Buisness': fictional_businesses,
    'Corporation': fictional_corporations,
    'Nonproft': fictional_nonprofits ,
    'School': fictional_schools,
    'Foundation': fictional_foundations
    }
