import hashlib

def getTicketOrderColumns():
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
        'LastActivityDate',
        'PatronTicket__CartId__c',
        'PatronTicket__CheckNumber__c',
        'PatronTicket__City__c',
        'PatronTicket__Comments__c',
        'PatronTicket__Contact__c',  # IMPORTANT. THIS CONNECTS TO THE CONTACTS TABLE
        'PatronTicket__Country__c',
        'PatronTicket__CreditCardCVV2__c',
        'PatronTicket__CreditCardExpirationMonth__c',
        'PatronTicket__CreditCardExpirationYear__c',
        'PatronTicket__CreditCardLastFour__c',
        'PatronTicket__CreditCardNumber__c',
        'PatronTicket__CreditCardType__c',
        'PatronTicket__DeliveryMethod__c',
        'PatronTicket__DonationAmount__c',
        'PatronTicket__Donation__c',
        'PatronTicket__EmailOptIn__c',
        'PatronTicket__Fee3Rule__c',
        'PatronTicket__Email__c',
        'PatronTicket__ErrorMessage__c',
        'PatronTicket__ExternalId__c',
        'PatronTicket__Fees__c',
        'PatronTicket__FirstName__c',
        'PatronTicket__LastName__c',
        'PatronTicket__OrderOrigin__c',
        'PatronTicket__OrderStatus__c',
        'PatronTicket__OtherPhone__c',
        'PatronTicket__PaymentMethod__c',
        'PatronTicket__PaymentTransactionId__c',
        'PatronTicket__Phone__c',
        'PatronTicket__PostalCode__c',
        'PatronTicket__RefundTransactionId__c',
        'PatronTicket__Salutation__c',
        'PatronTicket__ShippingCity__c',
        'PatronTicket__ShippingCountry__c',
        'PatronTicket__ShippingFee__c',
        'PatronTicket__ShippingFirstName__c',
        'PatronTicket__ShippingLastName__c',
        'PatronTicket__ShippingPostalCode__c',
        'PatronTicket__ShippingSalutation__c',
        'PatronTicket__ShippingState__c',
        'PatronTicket__ShippingStreetAddress__c',
        'PatronTicket__State__c',
        'PatronTicket__StreetAddress__c',
        'PatronTicket__SubscriptionStatus__c',
        'PatronTicket__Type__c',
        'PatronTicket__Subtotal__c',
        'PatronTicket__OrderSource__c',
        'PatronTicket__Account__c',  # IMPORTANT. THIS CONNECTS TO ACCOUNT!!!
        'PatronTicket__AmountPaid__c',
        'PatronTicket__LastTransactionID__c',
        'PatronTicket__SeatUpgradeRequested__c',
        'PatronTicket__QualificationMethod__c',
        'PatronTicket__ExchangeFee__c',
        'PatronTicket__SalesTax__c',
        'PatronTicket__EntryMethod__c',
        'PatronTicket__UserAgent__c',
        'PatronTicket__LastPaymentAmount__c',
        'PatronTicket__SemanticVersion__c',
        'PatronTicket__Fee3Waived__c',
        'PatronTicket__Fee3__c',
        'PatronTicket__Fee4Rule__c',
        'PatronTicket__Fee4Waived__c',
        'PatronTicket__Fee4__c',
        'PatronTicket__Fee5Rule__c',
        'PatronTicket__Fee5Waived__c',
        'PatronTicket__Fee5__c',
        'PatronTicket__FeesRule__c',
        'PatronTicket__FeesWaived__c',
        'PatronTicket__ItemFeesWaived__c',
        'PatronTicket__SalesTaxOrderLevel__c',
        'PatronTicket__ShippingFeeRule__c',
        'PatronTicket__ShippingFeeWaived__c',
        'PatronTicket__AuthorizationCode__c',
        'PatronTicket__LastPaymentGatewaySettings__c',
        'PatronTicket__EntryNote__c',
        'PatronTicket__PendingRenewalSeatAssignments__c',
        'PatronTicket__CreditCardBIN__c',
        'PatronTicket__DunningEmailSentTime__c',
        'PatronTicket__CartExpiration__c',
        'Are_you_with_a_group__c',
        'PatronTicket__AnonymousPurchase__c',
        'PatronTicket__UpdateContactRecord__c',
        'PatronTicket__SendConfirmationEmail__c',
        'Request_an_accommodation__c'
    ]

    return columns


def get_merging_dictionary():
    dictionary = {
        'Id': 'ticket_order_id',
        # 'OwnerId',
        # 'IsDeleted',
        'Name': 'ticket_order_name',
        'CreatedDate': 'create_date',
        # 'CreatedById',
        'LastModifiedDate': 'last_modified_date',
        # 'LastModifiedById',
        # 'SystemModstamp',
        # 'LastActivityDate',
        # 'PatronTicket__CartId__c': 'cart_id',
        # 'PatronTicket__CheckNumber__c',
        'PatronTicket__City__c': 'city',
        'PatronTicket__Comments__c': 'comments',
        'PatronTicket__Contact__c': 'contact_id',  # !!! IMPORTANT. THIS CONNECTS TO THE CONTACTS TABLE
        'PatronTicket__Country__c': 'country',
        # 'PatronTicket__CreditCardCVV2__c',
        # 'PatronTicket__CreditCardExpirationMonth__c',
        # 'PatronTicket__CreditCardExpirationYear__c',
        # 'PatronTicket__CreditCardLastFour__c',
        # 'PatronTicket__CreditCardNumber__c',
        # 'PatronTicket__CreditCardType__c',
        'PatronTicket__DeliveryMethod__c': 'delivery_method',
        'PatronTicket__DonationAmount__c': 'donation_amount',
        'PatronTicket__Donation__c': 'donation_id',
        'PatronTicket__EmailOptIn__c': 'email_opt_in',
        # 'PatronTicket__Fee3Rule__c',
        'PatronTicket__Email__c': 'email',
        # 'PatronTicket__ErrorMessage__c',
        'PatronTicket__ExternalId__c': 'external_id',
        'PatronTicket__Fees__c': 'fees',
        # 'PatronTicket__FirstName__c': 'first_name',
        # 'PatronTicket__LastName__c': 'last_name',
        'PatronTicket__OrderOrigin__c': 'order_origin',
        'PatronTicket__OrderStatus__c': 'order_status',
        'PatronTicket__OtherPhone__c': 'other_phone',
        'PatronTicket__PaymentMethod__c': 'payment_method',
        # 'PatronTicket__PaymentTransactionId__c',
        'PatronTicket__Phone__c': 'phone',
        'PatronTicket__PostalCode__c': 'postal_code',
        # 'PatronTicket__RefundTransactionId__c',
        'PatronTicket__Salutation__c': 'salutation',
        'PatronTicket__ShippingCity__c': 'shipping_city',
        'PatronTicket__ShippingCountry__c': 'shipping_country',
        # 'PatronTicket__ShippingFee__c',
        'PatronTicket__ShippingFirstName__c': 'shipping_first_name',
        'PatronTicket__ShippingLastName__c': 'shipping_last_name',
        'PatronTicket__ShippingPostalCode__c': 'shipping_postal_code',
        'PatronTicket__ShippingSalutation__c': 'shipping_salutation',
        'PatronTicket__ShippingState__c': 'shipping_state',
        'PatronTicket__ShippingStreetAddress__c': 'shipping_stress_address',
        'PatronTicket__State__c': 'state',
        'PatronTicket__StreetAddress__c': 'street_address',
        'PatronTicket__SubscriptionStatus__c': 'subscription_status',
        'PatronTicket__Type__c': 'type',
        # 'PatronTicket__Subtotal__c',
        'PatronTicket__OrderSource__c': 'order_source',
        'PatronTicket__Account__c': 'account_id',  # !! IMPORTANT. THIS CONNECTS TO ACCOUNT!!!
        'PatronTicket__AmountPaid__c': 'amount_paid',
        # 'PatronTicket__LastTransactionID__c',
        # 'PatronTicket__SeatUpgradeRequested__c',
        # 'PatronTicket__QualificationMethod__c',
        'PatronTicket__ExchangeFee__c': 'exchange_fee',
        # 'PatronTicket__SalesTax__c',
        # 'PatronTicket__EntryMethod__c',
        # 'PatronTicket__UserAgent__c',
        # 'PatronTicket__LastPaymentAmount__c',
        # 'PatronTicket__SemanticVersion__c',
        # 'PatronTicket__Fee3Waived__c',
        # 'PatronTicket__Fee3__c',
        # 'PatronTicket__Fee4Rule__c',
        # 'PatronTicket__Fee4Waived__c',
        # 'PatronTicket__Fee4__c',
        # 'PatronTicket__Fee5Rule__c',
        # 'PatronTicket__Fee5Waived__c',
        # 'PatronTicket__Fee5__c',
        # 'PatronTicket__FeesRule__c',
        # 'PatronTicket__FeesWaived__c',
        # 'PatronTicket__ItemFeesWaived__c',
        # 'PatronTicket__SalesTaxOrderLevel__c',
        # 'PatronTicket__ShippingFeeRule__c',
        # 'PatronTicket__ShippingFeeWaived__c',
        # 'PatronTicket__AuthorizationCode__c',
        # 'PatronTicket__LastPaymentGatewaySettings__c',
        'PatronTicket__EntryNote__c': 'notes',
        # 'PatronTicket__PendingRenewalSeatAssignments__c',
        # 'PatronTicket__CreditCardBIN__c',
        # 'PatronTicket__DunningEmailSentTime__c',
        # 'PatronTicket__CartExpiration__c',
        # 'Are_you_with_a_group__c',
        'PatronTicket__AnonymousPurchase__c': 'anonymous_purchase_flag',
        'PatronTicket__UpdateContactRecord__c': 'update_contact_record',
        'PatronTicket__SendConfirmationEmail__c': 'send_confirmation_email_flag',
        'Request_an_accommodation__c': 'request_accommodation'
    }

    return dictionary

def getTicketOrdersNewColumnOrder(df):

    # Hash Salesforce ID columns first
    id_columns = ['ticket_order_id', 'account_id', 'contact_id']

    for col in id_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: hash_to_int(x))

    new_column_order = [
        # Key Identifiers
        'ticket_order_id',
        'account_id',
        'contact_id',

        # Basic Info
        'ticket_order_name',
        'type',
        'order_status',
        'subscription_status',

        # Contact Info
        'email',
        'phone',
        'other_phone',

        # Address Info
        'street_address',
        'city',
        'state',
        'postal_code',
        'country',

        # Shipping Info
        'shipping_first_name',
        'shipping_last_name',
        'shipping_stress_address',
        'shipping_city',
        'shipping_state',
        'shipping_postal_code',
        'shipping_country',

        # Order Details
        'order_origin',
        'order_source',
        'payment_method',
        'amount_paid',
        'fees',
        'exchange_fee',
        'donation_id',
        'donation_amount',

        # Preferences and Settings
        'delivery_method',
        'salutation',
        'shipping_salutation',
        'email_opt_in',
        'anonymous_purchase_flag',
        'update_contact_record',
        'send_confirmation_email_flag',
        'request_accommodation',

        # Additional Info
        'external_id',
        'comments',
        'notes',

        # Dates
        'create_date',
        'last_modified_date'
    ]

    # Reorder the DataFrame columns
    df = df[new_column_order]

    return df


def getTicketOrderItemsColumns():
    columns = [
        'Id',
        'IsDeleted',
        'Name',
        'CreatedDate',
        'CreatedById',
        'LastModifiedDate',
        'LastModifiedById',
        'SystemModstamp',
        'PatronTicket__TicketOrder__c',
        'PatronTicket__Contact__c',
        'PatronTicket__DiscountCode__c',
        'PatronTicket__EffectiveTicketPrice__c',
        'PatronTicket__Quantity__c',
        'PatronTicket__SeatAssignment__c',
        'PatronTicket__Status__c',
        'PatronTicket__SubscriptionOrderItem__c',
        'PatronTicket__TicketPriceLevel__c',
        'PatronTicket__TicketableEvent__c',
        'PatronTicket__UnitDiscountAmount__c',
        'PatronTicket__UnitDiscountType__c',
        'PatronTicket__UnitFee__c',
        'PatronTicket__UnitPrice__c',
        'PatronTicket__ExternalId__c',
        'PatronTicket__SubscriptionBuyerSelectionLink__c',
        'PatronTicket__LastEmailedDate__c',
        'PatronTicket__LastPrintedDate__c',
        'PatronTicket__EntryDate__c',
        'PatronTicket__EntryDevice__c',
        'PatronTicket__Account__c',
        'PatronTicket__AmountPaid__c',
        'PatronTicket__SeatNote__c',
        'PatronTicket__SalesTax__c',
        'PatronTicket__TicketNote__c',
        'PatronTicket__UnitFee2Rule__c',
        'PatronTicket__UnitFee2__c',
        'PatronTicket__UnitFee3Rule__c',
        'PatronTicket__UnitFee3__c',
        'PatronTicket__UnitFee4Rule__c',
        'PatronTicket__UnitFee4__c',
        'PatronTicket__UnitFee5Rule__c',
        'PatronTicket__UnitFee5__c',
        'PatronTicket__UnitFeeRule__c',
        'PatronTicket__DiscountCodeUsage__c',
        'Season__c',
        'PatronTicket__PostShowEmailSentTime__c',
        'PatronTicket__PreShowEmailSentTime__c',
        'PatronTicket__SeatKey__c',
        'PatronTicket__Passcode__c',
        'PatronTicket__CancelShowEmailSentTime__c',
        'PatronTicket__Barcode__c',
        'PatronTicket__FairMarketValue__c'
    ]

    return columns

def getTicketOrderItemsDictionary():
    dictionary = {
        'Id' : 'ticket_order_item_id',
        # 'IsDeleted',
        'Name' : 'ticket_order_item_name',
        'CreatedDate' : 'create_date',
        # 'CreatedById',
        'LastModifiedDate' : 'last_modified_date',
        # 'LastModifiedById',
        # 'SystemModstamp',
        'PatronTicket__TicketOrder__c' : 'ticket_order_id',
        'PatronTicket__Contact__c' : 'contact_id',
        'PatronTicket__DiscountCode__c' : 'discount_code_id',
        'PatronTicket__EffectiveTicketPrice__c' : 'ticket_price',
        'PatronTicket__Quantity__c' : 'quantity',
        # 'PatronTicket__SeatAssignment__c',
        'PatronTicket__Status__c' : 'status',
        'PatronTicket__SubscriptionOrderItem__c' : 'subscription_order_item_id',
        'PatronTicket__TicketPriceLevel__c' : 'price_level_id',
        'PatronTicket__TicketableEvent__c' : 'event_id',
        'PatronTicket__UnitDiscountAmount__c' : 'discount_amount',
        'PatronTicket__UnitDiscountType__c' : 'discount_type',
        'PatronTicket__UnitFee__c' : 'unit_fee',
        'PatronTicket__UnitPrice__c' : 'unit_price',
        # 'PatronTicket__ExternalId__c',
        # 'PatronTicket__SubscriptionBuyerSelectionLink__c',
        # 'PatronTicket__LastEmailedDate__c',
        # 'PatronTicket__LastPrintedDate__c',
        'PatronTicket__EntryDate__c' : 'entry_date',
        # 'PatronTicket__EntryDevice__c',
        'PatronTicket__Account__c' : 'account_id',
        'PatronTicket__AmountPaid__c' : 'amount_paid',
        # 'PatronTicket__SeatNote__c' : 'seat_notes',
        'PatronTicket__SalesTax__c' : 'sales_tax',
        'PatronTicket__TicketNote__c' : 'ticket_notes',
        # 'PatronTicket__UnitFee2Rule__c' : 'unit_fee_2_rule',
        'PatronTicket__UnitFee2__c' : 'unit_fee',
        # 'PatronTicket__UnitFee3Rule__c' : 'unit_fee_3_rule',
        # 'PatronTicket__UnitFee3__c' : 'unit_fee_3',
        # 'PatronTicket__UnitFee4Rule__c' : 'unit_fee_4_rule',
        # 'PatronTicket__UnitFee4__c' : 'unit_fee_4',
        # 'PatronTicket__UnitFee5Rule__c' : 'unit_fee_5_rule',
        # 'PatronTicket__UnitFee5__c' : 'unit_fee_5',
        # 'PatronTicket__UnitFeeRule__c' : 'unit_fee_rule',
        # 'PatronTicket__DiscountCodeUsage__c' : 'discount_code_usage',
        'Season__c' : 'season',
        # 'PatronTicket__PostShowEmailSentTime__c',
        # 'PatronTicket__PreShowEmailSentTime__c',
        # 'PatronTicket__SeatKey__c',
        # 'PatronTicket__Passcode__c',
        # 'PatronTicket__CancelShowEmailSentTime__c',
        'PatronTicket__Barcode__c' : 'barcode'
        # 'PatronTicket__FairMarketValue__c'
    }

    return dictionary

def getTicketOrderItemsNewColumnOrder(df):

    # Salesforce ID columns that need to be hashed
    id_columns = ['ticket_order_item_id', 'ticket_order_id', 'account_id', 'contact_id',
                  'event_id', 'subscription_order_item_id', 'price_level_id', 'discount_code_id']

    # Hashing the specified columns
    for col in id_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: hash_to_int(x))

    new_column_order = [
        # Key Identifiers
        'ticket_order_item_id',
        'ticket_order_id',
        'account_id',
        'contact_id',

        # Basic Info
        'status',
        'season',

        # Ticket Details
        'event_id',
        'subscription_order_item_id',
        'price_level_id',
        'ticket_order_item_name',
        'quantity',
        'ticket_price',
        'unit_price',
        'amount_paid',
        'sales_tax',

        # Discounts and Fees
        'discount_code_id',
        'discount_amount',
        'discount_type',
        'unit_fee',

        # Additional Info
        'ticket_notes',
        'barcode',

        # Dates
        'create_date',
        'last_modified_date',
        'entry_date'
    ]

    # Reordering the DataFrame columns according to new_column_order
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

