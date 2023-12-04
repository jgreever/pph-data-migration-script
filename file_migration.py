# This Python script is for munging and migrating the PPH data from the Salesforce .csv dump
# into the PPH application server. The original csvs are read into pandas data frames. Then they
# each go through their respective filtering via dictionarys in the functions files. The new
# data frames are then constructed in the for loops and saved to the munged database folder.

import yaml
import pandas as pd
import accounts_functions as af
import contacts_functions as cf
import notes_functions as nf
import ticketorders_functions as tof
import transactions_functions as tf
import events_functions as te
import opportunites_function as of
import recordtypes_functions as rtf

def read_csv_file(file_path):
    return pd.read_csv(file_path, header=0, encoding='latin-1', low_memory=False)

def create_new_dataframe(old_df, merge_key):
    new_df = pd.DataFrame()
    for old_col, new_col in merge_key.items():
        new_df[new_col] = old_df[old_col] if old_col is not None else None
    return new_df

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def save_to_yaml(df, file_path):
    # Replace NaN values with None
    df = df.where(pd.notnull(df), None)

    # Convert the DataFrame to a list of dictionaries
    data_dict = df.to_dict(orient='records')

    # Write the YAML data to a file
    with open(file_path, 'w') as file:
        yaml.dump(data_dict, file, sort_keys=False, default_flow_style=False)

def process_accounts():
    accounts = read_csv_file("Bronze_tables/Account.csv")
    newaccount = create_new_dataframe(accounts, af.get_merging_dictionary())
    save_to_csv(newaccount, "Silver_tables/Accounts-Silver.csv")

    df_accounts = read_csv_file('Silver_tables/Accounts-Silver.csv')
    df_accounts_organized = af.GetNewColumnsOrder(df_accounts)
    save_to_csv(df_accounts_organized, 'Gold_tables/Accounts.csv')
    save_to_yaml(df_accounts_organized, 'Gold_tables/Accounts.yaml')

def process_contacts():
    contacts = read_csv_file("Bronze_tables/Contact.csv")
    newcontact = create_new_dataframe(contacts, cf.get_merging_dictionary())
    save_to_csv(newcontact, "Silver_tables/Contacts-Silver.csv")

    df_contacts = read_csv_file('Silver_tables/Contacts-Silver.csv')
    df_contacts_organized = cf.GetNewColumnsOrder(df_contacts)
    save_to_csv(df_contacts_organized, 'Gold_tables/Contacts.csv')
    save_to_yaml(df_contacts_organized, 'Gold_tables/Contacts.yaml')

def process_notes():
    notes = read_csv_file("Bronze_tables/Note.csv")
    newnotes = create_new_dataframe(notes, nf.get_merging_dictionary())
    save_to_csv(newnotes, "Silver_tables/Notes-Silver.csv")

    df_notes = read_csv_file('Silver_tables/Notes-Silver.csv')
    df_notes_organized = nf.getNewColumnsOrder(df_notes)
    save_to_csv(df_notes_organized, 'Gold_tables/Notes.csv')
    save_to_yaml(df_notes_organized, 'Gold_tables/Notes.yaml')


def process_ticket_order_items():
    ticket_order_items = read_csv_file("Bronze_tables/PatronTicket__TicketOrderItem__c.csv")
    new_ticket_order_items = create_new_dataframe(ticket_order_items, tof.getTicketOrderItemsDictionary())
    save_to_csv(new_ticket_order_items, "Silver_tables/TicketOrderItems-Silver.csv")

    df_ticket_order_items = read_csv_file('Silver_tables/TicketOrderItems-Silver.csv')
    df_ticket_order_items_organized = tof.getTicketOrderItemsNewColumnOrder(df_ticket_order_items)
    save_to_yaml(df_ticket_order_items_organized, 'Gold_tables/TicketOrderItems.yaml')

def process_ticket_orders():
    ticketorders = read_csv_file("Bronze_tables/PatronTicket__TicketOrder__c.csv")
    newticketorders = create_new_dataframe(ticketorders, tof.get_merging_dictionary())
    save_to_csv(newticketorders, "Silver_tables/TicketOrders-Silver.csv")

    df = read_csv_file('Silver_tables/TicketOrders-Silver.csv')
    df_organized = tof.getTicketOrdersNewColumnOrder(df)
    save_to_yaml(df_organized, 'Gold_tables/TicketOrders.yaml')

def process_transactions():
    payment_transactions_df = read_csv_file("Bronze_tables/PatronTrx__PaymentTransaction__c.csv")
    payment_transaction_items_df = read_csv_file("Bronze_tables/PatronTrx__PaymentTransactionItem__c.csv")
    merged_df = pd.merge(payment_transactions_df, payment_transaction_items_df,
                         left_on='Id', right_on='PatronTrx__PaymentTransaction__c',
                         how='inner', on=None, validate="many_to_many")
    save_to_csv(merged_df, "Silver_tables/Transactions-Silver.csv")

    transactions = read_csv_file("Silver_tables/Transactions-Silver.csv")
    new_transactions = create_new_dataframe(transactions, tf.get_merging_dictionary())
    save_to_csv(new_transactions, "Silver_tables/Transactions-Silver.csv")

    df = read_csv_file('Silver_tables/Transactions-Silver.csv')
    df_organized = tf.organize_columns(df)
    save_to_yaml(df_organized, 'Gold_tables/Transactions.yaml')

def process_events():
    ticketable_events = read_csv_file("Bronze_tables/PatronTicket__TicketableEvent__c.csv")
    new_ticketable_events = create_new_dataframe(ticketable_events, te.get_merging_dictionary())
    save_to_csv(new_ticketable_events, "Silver_tables/Events-Silver.csv")

    df_ticketable_events = read_csv_file('Silver_tables/Events-Silver.csv')
    df_ticketable_events_oragnized = te.getNewColumnsOrder(df_ticketable_events)
    save_to_yaml(df_ticketable_events_oragnized, 'Gold_tables/Events.yaml')

def process_opportunities():
    opportunities = read_csv_file("Bronze_tables/Opportunity.csv")
    new_opportunities = create_new_dataframe(opportunities, of.get_merging_dictionary())
    save_to_csv(new_opportunities, "Silver_tables/Opportunity-Silver.csv")

    df_opportunities = read_csv_file('Silver_tables/Opportunity-Silver.csv')
    df_opportunities_organized = of.getNewOpportunityColumnsOrder(df_opportunities)
    save_to_yaml(df_opportunities_organized, 'Gold_tables/Opportunity.yaml')

def process_recordtypes():
    recordtypes = read_csv_file("Bronze_tables/RecordType.csv")
    new_recordtypes = create_new_dataframe(recordtypes, rtf.get_merging_dictionary())
    save_to_csv(new_recordtypes, "Silver_tables/RecordType-Silver.csv")

    df_recordtypes = read_csv_file('Silver_tables/RecordType-Silver.csv')
    df_recordtypes_organized = rtf.getNewColumnsOrder(df_recordtypes)
    save_to_yaml(df_recordtypes_organized, 'Gold_tables/RecordType.yaml')

def process_development_tables():
    # Processing Accounts
    df_accounts = read_csv_file('Development_tables/Accounts.csv')
    save_to_yaml(df_accounts, 'Development_tables/Accounts.yaml')

    # Processing Contacts
    df_contacts = read_csv_file('Development_tables/Contacts.csv')
    save_to_yaml(df_contacts, 'Development_tables/Contacts.yaml')

    # Processing Events
    df_events = read_csv_file('Development_tables/Events.csv')
    save_to_yaml(df_events, 'Development_tables/Events.yaml')

    # Processing Opportunity
    df_opportunity = read_csv_file('Development_tables/Opportunity.csv')
    save_to_yaml(df_opportunity, 'Development_tables/Opportunity.yaml')

    # Processing Transactions
    df_transactions = read_csv_file('Development_tables/Randomized_Transactions.csv')
    save_to_yaml(df_transactions, 'Development_tables/Transactions.yaml')

    # Processing RecordType
    df_recordtype = read_csv_file('Development_tables/RecordType.csv')
    save_to_yaml(df_recordtype, 'Development_tables/RecordType.yaml')

    # Processing TicketOrderItems
    df_ticketorderitems = read_csv_file('Development_tables/TicketOrderItems.csv')
    save_to_yaml(df_ticketorderitems, 'Development_tables/TicketOrderItems.yaml')

    # Processing TicketOrders
    df_ticketorders = read_csv_file('Development_tables/TicketOrders.csv')
    save_to_yaml(df_ticketorders, 'Development_tables/TicketOrders.yaml')

    # Processing Notes
    df_notes = read_csv_file('Development_tables/Notes.csv')
    save_to_yaml(df_notes, 'Development_tables/Notes.yaml')

def main():

    process_development_tables()

    #process_accounts()
    #process_contacts()
    #process_notes()
    #process_ticket_order_items()
    #process_ticket_orders()
    #process_transactions()
    #process_events()
    #process_opportunities()
    #process_recordtypes()


if __name__ == "__main__":
    main()
