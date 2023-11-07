def getTicketableEventsColumns():
    columns = [
        'Id',
        'OwnerId',
        'IsDeleted',
        'Name',
        'CreatedDate',
        'CreatedById',
        'LastModifiedDate',
        'LastModifiedById',
        'SystemModstamp',
        'PatronTicket__Active__c',
        'PatronTicket__Description__c',
        'PatronTicket__Detail__c',
        'PatronTicket__SortOrder__c', 'PatronTicket__Type__c',
        'PatronTicket__ActiveInstances__c',
        'PatronTicket__TotalInstances__c',
        'PatronTicket__EventCategory__c',
        'PatronTicket__NoLongerOnSaleMessage__c',
        'PatronTicket__SoldOutMessage__c',
        'PatronTicket__GeneralLedgerCode__c',
        'PatronTicket__FormattedName__c',
        'PatronTicket__NonTaxable__c',
        'PatronTicket__PrintAtHomeDetail__c',
        'PatronTicket__PrintAtHomeTicketAd__c',
        'PatronTicket__CustomOrderConfirmationTemplate__c',
        'PatronTicket__NotYetOnSaleMessage__c',
        'PatronTicket__SupportedDeliveryMethods__c',
        'PatronTicket__CustomAwaitingFulfillmentConfTemplate__c',
        'PatronTicket__AllowQuokkaSubscriptionItems__c',
        'PatronTicket__POSWatermark__c',
        'PatronTicket__EventTrackingCode__c',
        'PatronTicket__InternalDescription__c',
        'Season__c',
        'PatronTicket__PostShowEmailAttendeesOnly__c',
        'PatronTicket__PostShowEmailMinutes__c',
        'PatronTicket__PostShowEmailTemplateId__c',
        'PatronTicket__PostShowEmailTemplateName__c',
        'PatronTicket__PrePostShowEmailDisabled__c',
        'PatronTicket__PreShowEmailCutoffMinutes__c',
        'PatronTicket__PreShowEmailMinutes__c',
        'PatronTicket__PreShowEmailTemplateId__c',
        'PatronTicket__PreShowEmailTemplateName__c',
        'PatronTicket__RunTime__c',
        'PatronTicket__LargeImage__c',
        'PatronTicket__SmallImage__c',
        'First_Performance_Date__c',
        'PatronTicket__OrderFeeExempt__c',
        'PatronTicket__SubscriberBadge__c',
        'PatronTicket__LargeImageAltText__c',
        'PatronTicket__SmallImageAltText__c'
    ]
    return columns

def get_merging_dictionary():
    dictionary = {
        'Id': 'ticketable_event_id',
        'OwnerId': 'owner_id',
        # 'IsDeleted',
        'Name': 'name',
        'CreatedDate': 'create_date',
        # 'CreatedById',
        'LastModifiedDate': 'last_modified_date',
        # 'LastModifiedById',
        # 'SystemModstamp',
        'PatronTicket__Active__c': 'active_flag',
        'PatronTicket__Description__c': 'description',
        'PatronTicket__Detail__c': 'detail',
        # 'PatronTicket__SortOrder__c' ,
        # 'PatronTicket__Type__c' ,
        # 'PatronTicket__ActiveInstances__c' ,
        # 'PatronTicket__TotalInstances__c',
        'PatronTicket__EventCategory__c' : 'event_category',
        # 'PatronTicket__NoLongerOnSaleMessage__c',
        # 'PatronTicket__SoldOutMessage__c',
        # 'PatronTicket__GeneralLedgerCode__c',
        # 'PatronTicket__FormattedName__c',
        # 'PatronTicket__NonTaxable__c',
        # 'PatronTicket__PrintAtHomeDetail__c',
        # 'PatronTicket__PrintAtHomeTicketAd__c',
        # 'PatronTicket__CustomOrderConfirmationTemplate__c',
        # 'PatronTicket__NotYetOnSaleMessage__c',
        # 'PatronTicket__SupportedDeliveryMethods__c',
        # 'PatronTicket__CustomAwaitingFulfillmentConfTemplate__c',
        # 'PatronTicket__AllowQuokkaSubscriptionItems__c',
        # 'PatronTicket__POSWatermark__c',
        # 'PatronTicket__EventTrackingCode__c',
        # 'PatronTicket__InternalDescription__c',
        'Season__c' : 'season',
        # 'PatronTicket__PostShowEmailAttendeesOnly__c',
        # 'PatronTicket__PostShowEmailMinutes__c',
        # 'PatronTicket__PostShowEmailTemplateId__c',
        # 'PatronTicket__PostShowEmailTemplateName__c',
        'PatronTicket__PrePostShowEmailDisabled__c' : 'pre_post_show_email_flag',
        'PatronTicket__PreShowEmailCutoffMinutes__c' : 'pre_show_email_cutoff_minutes',
        'PatronTicket__PreShowEmailMinutes__c' : 'pre_show_email_minutes',
        # 'PatronTicket__PreShowEmailTemplateId__c',
        # 'PatronTicket__PreShowEmailTemplateName__c',
        'PatronTicket__RunTime__c' : 'run_time',
        # 'PatronTicket__LargeImage__c',
        # 'PatronTicket__SmallImage__c',
        'First_Performance_Date__c' : 'performance_date',
        # 'PatronTicket__OrderFeeExempt__c',
        # 'PatronTicket__SubscriberBadge__c',
        # 'PatronTicket__LargeImageAltText__c',
        # j'PatronTicket__SmallImageAltText__c'
    }
    return dictionary

def getNewColumnsOrder(df):
    # Define the new column order with logical grouping and comments for readability
    new_column_order = [
        # Event Identifiers
        'ticketable_event_id',
        'owner_id',

        # Event Basic Info
        'name',
        'create_date',
        'last_modified_date',

        # Event Status
        'active_flag',

        # Event Descriptions
        'description',
        'detail',
        'event_category',

        # Event Timing and Category
        'season',
        'performance_date',

        # Event Email Communication Flags
        'pre_post_show_email_flag',
        'pre_show_email_cutoff_minutes',
        'pre_show_email_minutes',

        # Event Specifics
        'run_time',
    ]
    return df[new_column_order]