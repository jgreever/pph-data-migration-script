# This Python script is for munging and migrating the PPH data from the Salesforce .csv dump
# into the PPH application server. The original csvs are read into pandas data frames. Then they
# each go through their respective filtering via dictionarys in the functions files. The new
# data frames are then contructed in the for loops and saved to the munged database folder.

import pandas as pd
import accounts_functions as af
import contacts_functions as cf
import notes_functions as nf
import ticketorders_functions as tof
import transactions_functions as tf
import events_functions as te

def read_csv_file(file_path):
    return pd.read_csv(file_path, header=0, encoding='latin-1')

def create_new_dataframe(old_df, merge_key):
    new_df = pd.DataFrame()
    for old_col, new_col in merge_key.items():
        new_df[new_col] = old_df[old_col] if old_col is not None else None
    return new_df

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def process_accounts():
    accounts = read_csv_file("Bronze_tables/Account.csv")
    newaccount = create_new_dataframe(accounts, af.get_merging_dictionary())
    save_to_csv(newaccount, "Gold_tables/Accounts.csv")

def process_contacts():
    contacts = read_csv_file("Bronze_tables/Contact.csv")
    newcontact = create_new_dataframe(contacts, cf.get_merging_dictionary())
    save_to_csv(newcontact, "Gold_tables/Contacts.csv")

def process_notes():
    notes = read_csv_file("Bronze_tables/Note.csv")
    newnotes = create_new_dataframe(notes, nf.get_merging_dictionary())
    save_to_csv(newnotes, "Gold_tables/Notes.csv")

def process_ticket_order_items():
    ticket_order_items = read_csv_file("Bronze_tables/PatronTicket__TicketOrderItem__c.csv")
    new_ticket_order_items = create_new_dataframe(ticket_order_items, tof.getTicketOrderItemsDictionary())
    save_to_csv(new_ticket_order_items, "Silver_tables/TicketOrderItems-Silver.csv")

    df_ticket_order_items = read_csv_file('Silver_tables/TicketOrderItems-Silver.csv')
    df_ticket_order_items_organized = tof.getTicketOrderItemsNewColumnOrder(df_ticket_order_items)
    save_to_csv(df_ticket_order_items_organized, 'Gold_tables/TicketOrderItems.csv')

def process_ticket_orders():
    ticketorders = read_csv_file("Bronze_tables/PatronTicket__TicketOrder__c.csv")
    newticketorders = create_new_dataframe(ticketorders, tof.get_merging_dictionary())
    save_to_csv(newticketorders, "Silver_tables/TicketOrders-Silver.csv")

    df = read_csv_file('Silver_tables/TicketOrders-Silver.csv')
    df_organized = tof.getTicketOrdersNewColumnOrder(df)
    save_to_csv(df_organized, 'Gold_tables/TicketOrders.csv')

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
    save_to_csv(df_organized, 'Gold_tables/Transactions.csv')

def process_events():
    ticketable_events = read_csv_file("Bronze_tables/PatronTicket__TicketableEvent__c.csv")
    new_ticketable_events = create_new_dataframe(ticketable_events, te.get_merging_dictionary())
    save_to_csv(new_ticketable_events, "Silver_tables/Events-Silver.csv")

    df_ticketable_events = read_csv_file('Silver_tables/Events-Silver.csv')
    df_ticketable_events_oragnized = te.getNewColumnsOrder(df_ticketable_events)
    save_to_csv(df_ticketable_events_oragnized, 'Gold_tables/Events.csv')

def main():
    process_accounts()
    process_contacts()
    process_notes()
    process_ticket_order_items()
    process_ticket_orders()
    process_transactions()
    process_events()

if __name__ == "__main__":
    main()
