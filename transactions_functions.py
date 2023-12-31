import hashlib

def getPaymentTransactionsColumns():
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
        'PatronTrx__BuyerFeeLineItemSubtotal__c',
        'PatronTrx__BuyerOrderFee__c',
        'PatronTrx__CaptureTransactionId__c',
        'PatronTrx__ClearedDate__c',
        'PatronTrx__DiscountAmount__c',
        'PatronTrx__DonationAmount__c',
        'PatronTrx__ExternalTransactionID__c',
        'PatronTrx__FirstName__c',
        'PatronTrx__LastName__c',
        'PatronTrx__OrderId__c',
        'PatronTrx__OrderName__c',
        'PatronTrx__OrderOrigin__c',
        'PatronTrx__OrganizationId__c',
        'PatronTrx__OrganizationName__c',
        'PatronTrx__PatronTechFeeLineItemSubtotal__c',
        'PatronTrx__PatronTechOrderFee__c',
        'PatronTrx__PaymentMethod__c',
        'PatronTrx__ReferenceTransaction__c',
        'PatronTrx__ShippingFee__c',
        'PatronTrx__Status__c',
        'PatronTrx__TransactionDate__c',
        'PatronTrx__TransactionFee__c',
        'PatronTrx__TransactionId__c',
        'PatronTrx__TransactionTotal__c',
        'PatronTicket__TicketOrder__c',
        'PatronTrx__CurrencyCode__c',
        'PatronTrx__CreditCardType__c',
        'PatronTrx__CreditCardTransactionFee__c',
        'PatronTrx__ExchangeFee__c',
        'PatronTrx__Opportunity__c',
        'PatronTrx__PaymentProcessor__c',
        'PatronTrx__SalesTaxLineItemSubtotal__c',
        'PatronTrx__StoredPaymentMethod__c',
        'PatronTicket__BatchCreationDate__c',
        'PatronTicket__ExchangeType__c',
        'PatronTrx__Fee3__c',
        'PatronTrx__Fee4__c',
        'PatronTrx__Fee5__c',
        'PatronTrx__SalesTaxOrderLevel__c',
        'PatronTicket__EntryMethod__c',
        'PatronTrx__AuthorizationCode__c',
        'PatronTrx__BatchDate__c',
        'PatronTrx__PaymentGatewaySettings__c',
        'PatronTrx__AmountTendered__c',
        'PatronTrx__NameOnCard__c',
        'PatronTrx__CreditCardBIN__c',
        'PatronTrx__GiftCardNumber__c',
        'PatronTrx__CreditRefundType__c',
        'PatronTrx__CreditCardEntryMethod__c',
        'PatronTrx__CreditCardLastFour__c'
    ]

    return columns

def getPaymentTransactionsDictionary():

    dictionary = {
    'Id' : 'transaction_id',
    # 'OwnerId',
    # 'IsDeleted',
    # 'Name',
    # 'CreatedDate',
    # 'CreatedById',
    # 'LastModifiedDate',
    # 'LastModifiedById',
    # 'SystemModstamp',
    'PatronTrx__BuyerFeeLineItemSubtotal__c' : 'buyer_fee_line_item_sub_total',
    # 'PatronTrx__BuyerOrderFee__c',
    'PatronTrx__CaptureTransactionId__c' : 'capture_transaction_id',
    # 'PatronTrx__ClearedDate__c',
    'PatronTrx__DiscountAmount__c' : 'discount_amount',
    'PatronTrx__DonationAmount__c' : 'donation_amount',
    # 'PatronTrx__ExternalTransactionID__c',
    'PatronTrx__FirstName__c' : 'first_name',
    'PatronTrx__LastName__c' : 'last_name',
    # 'PatronTrx__OrderId__c',
    # 'PatronTrx__OrderName__c',
    'PatronTrx__OrderOrigin__c' : 'order_origin',
    # 'PatronTrx__OrganizationId__c',
    # 'PatronTrx__OrganizationName__c',
    'PatronTrx__PatronTechFeeLineItemSubtotal__c' : 'patron_tech_fee_line_item_sub_total',
    # 'PatronTrx__PatronTechOrderFee__c',
    'PatronTrx__PaymentMethod__c' : 'payment_method',
    # 'PatronTrx__ReferenceTransaction__c',
    'PatronTrx__ShippingFee__c' : 'shipping_fee',
    'PatronTrx__Status__c' : 'status',
    'PatronTrx__TransactionDate__c' : 'transaction_date',
    # 'PatronTrx__TransactionFee__c',
    # 'PatronTrx__TransactionId__c',
    'PatronTrx__TransactionTotal__c' : 'transaction_total',
    'PatronTicket__TicketOrder__c' : 'ticket_order_id',  # CONNECTS TO TICKETORDER TABLE
    # 'PatronTrx__CurrencyCode__c',
    # 'PatronTrx__CreditCardType__c',
    # 'PatronTrx__CreditCardTransactionFee__c',
    'PatronTrx__ExchangeFee__c' : 'exchange_fee',
    # 'PatronTrx__Opportunity__c',
    'PatronTrx__PaymentProcessor__c' : 'payment_processor',
    # 'PatronTrx__SalesTaxLineItemSubtotal__c',
    # 'PatronTrx__StoredPaymentMethod__c',
    # 'PatronTicket__BatchCreationDate__c',
    'PatronTicket__ExchangeType__c' : 'exchange_type',
    # 'PatronTrx__Fee3__c',
    # 'PatronTrx__Fee4__c',
    # 'PatronTrx__Fee5__c',
    # 'PatronTrx__SalesTaxOrderLevel__c',
    'PatronTicket__EntryMethod__c' : 'entry_method',
    # 'PatronTrx__AuthorizationCode__c',
    # 'PatronTrx__BatchDate__c',
    # 'PatronTrx__PaymentGatewaySettings__c',
    'PatronTrx__AmountTendered__c' : 'amount_tendered',
    'PatronTrx__NameOnCard__c' : 'name_on_card',
    # 'PatronTrx__CreditCardBIN__c',
    # 'PatronTrx__GiftCardNumber__c',
    # 'PatronTrx__CreditRefundType__c',
    'PatronTrx__CreditCardEntryMethod__c' : 'credit_card_entry_method',
    'PatronTrx__CreditCardLastFour__c' : 'credit_card_last_four'
    }

    return dictionary


def getPaymentTransactionItemsColumns():
    columns = [
        'Id',
        'IsDeleted',
        'Name',
        'CreatedDate',
        'CreatedById',
        'LastModifiedDate',
        'LastModifiedById',
        'SystemModstamp',
        'PatronTrx__PaymentTransaction__c',
        'PatronTrx__BuyerUnitFee__c',
        'PatronTrx__BuyerUnitPrice__c',
        'PatronTrx__GrossUnitPrice__c',
        'PatronTrx__ItemName__c',
        'PatronTrx__ItemNumber__c',
        'PatronTrx__ItemType__c',
        'PatronTrx__PatronTechUnitFee__c',
        'PatronTrx__Quantity__c',
        'PatronTicket__TicketOrderItem__c',
        'PatronTrx__FullBuyerCost__c',
        'PatronTrx__FullGrossAmount__c',
        'PatronTrx__TotalItemQuantity__c',
        'PatronTrx__SalesTax__c',
        'PatronTicket__SubscriptionBuyerSelectionLink__c',
        'PatronTicket__TicketPriceLevel__c',
        'PatronTrx__UnitFee2__c',
        'PatronTrx__UnitFee3__c',
        'PatronTrx__UnitFee4__c',
        'PatronTrx__UnitFee5__c',
        'PatronTrx__TaxDeductibleAmount__c',
        'PatronTrx__TaxDeductibleDonation__c'
    ]

    return columns

def getPaymentTransactionItemDictionary():
    dictionary = {
        'Id' : 'transaction_item_id',
        # 'IsDeleted',
        'Name' : 'transaction_name',
        'CreatedDate' : 'create_date',
        # 'CreatedById',
        # 'LastModifiedDate',
        # 'LastModifiedById',
        # 'SystemModstamp',
        'PatronTrx__PaymentTransaction__c' : 'payment_transaction',
        'PatronTrx__BuyerUnitFee__c' : 'buyer_unit_fee',
        'PatronTrx__BuyerUnitPrice__c' : 'buyer_unit_price',
        'PatronTrx__GrossUnitPrice__c' : 'gross_unit_price',
        'PatronTrx__ItemName__c' : 'item_name',
        'PatronTrx__ItemNumber__c' : 'item_number',
        'PatronTrx__ItemType__c' : 'item_type',
        'PatronTrx__PatronTechUnitFee__c' : 'patron_tech_unit_fee',
        'PatronTrx__Quantity__c' : 'quantity',
        'PatronTicket__TicketOrderItem__c' : 'ticket_order_item',
        'PatronTrx__FullBuyerCost__c' : 'full_buyer_cost',
        'PatronTrx__FullGrossAmount__c' : 'full_gross_amount',
        'PatronTrx__TotalItemQuantity__c' : 'total_item_quantity',
        # 'PatronTrx__SalesTax__c',
        # 'PatronTicket__SubscriptionBuyerSelectionLink__c',
        # 'PatronTicket__TicketPriceLevel__c',
        'PatronTrx__UnitFee2__c' : 'unit_fee',
        # 'PatronTrx__UnitFee3__c',
        # 'PatronTrx__UnitFee4__c',
        # 'PatronTrx__UnitFee5__c',
        # 'PatronTrx__TaxDeductibleAmount__c',
        # 'PatronTrx__TaxDeductibleDonation__c'
    }
    return dictionary


def getTransactionsColumns():
    columns = [
    'Id_x',
    'OwnerId',
    'IsDeleted_x',
    'Name_x',
    'CreatedDate_x',
    'CreatedById_x',
    'LastModifiedDate_x',
    'LastModifiedById_x',
    'SystemModstamp_x',
    'PatronTrx__BuyerFeeLineItemSubtotal__c',
    'PatronTrx__BuyerOrderFee__c',
    'PatronTrx__CaptureTransactionId__c',
    'PatronTrx__ClearedDate__c',
    'PatronTrx__DiscountAmount__c',
    'PatronTrx__DonationAmount__c',
    'PatronTrx__ExternalTransactionID__c',
    'PatronTrx__FirstName__c',
    'PatronTrx__LastName__c',
    'PatronTrx__OrderId__c',
    'PatronTrx__OrderName__c',
    'PatronTrx__OrderOrigin__c',
    'PatronTrx__OrganizationId__c',
    'PatronTrx__OrganizationName__c',
    'PatronTrx__PatronTechFeeLineItemSubtotal__c',
    'PatronTrx__PatronTechOrderFee__c',
    'PatronTrx__PaymentMethod__c',
    'PatronTrx__ReferenceTransaction__c',
    'PatronTrx__ShippingFee__c',
    'PatronTrx__Status__c',
    'PatronTrx__TransactionDate__c',
    'PatronTrx__TransactionFee__c',
    'PatronTrx__TransactionId__c',
    'PatronTrx__TransactionTotal__c',
    'PatronTicket__TicketOrder__c',
    'PatronTrx__CurrencyCode__c',
    'PatronTrx__CreditCardType__c',
    'PatronTrx__CreditCardTransactionFee__c',
    'PatronTrx__ExchangeFee__c',
    'PatronTrx__Opportunity__c',
    'PatronTrx__PaymentProcessor__c',
    'PatronTrx__SalesTaxLineItemSubtotal__c',
    'PatronTrx__StoredPaymentMethod__c',
    'PatronTicket__BatchCreationDate__c',
    'PatronTicket__ExchangeType__c',
    'PatronTrx__Fee3__c',
    'PatronTrx__Fee4__c',
    'PatronTrx__Fee5__c',
    'PatronTrx__SalesTaxOrderLevel__c',
    'PatronTicket__EntryMethod__c',
    'PatronTrx__AuthorizationCode__c',
    'PatronTrx__BatchDate__c',
    'PatronTrx__PaymentGatewaySettings__c',
    'PatronTrx__AmountTendered__c',
    'PatronTrx__NameOnCard__c',
    'PatronTrx__CreditCardBIN__c',
    'PatronTrx__GiftCardNumber__c',
    'PatronTrx__CreditRefundType__c',
    'PatronTrx__CreditCardEntryMethod__c',
    'PatronTrx__CreditCardLastFour__c',
    'Id_y',
    'IsDeleted_y',
    'Name_y',
    'CreatedDate_y',
    'CreatedById_y',
    'LastModifiedDate_y',
    'LastModifiedById_y',
    'SystemModstamp_y',
    'PatronTrx__PaymentTransaction__c',
    'PatronTrx__BuyerUnitFee__c',
    'PatronTrx__BuyerUnitPrice__c',
    'PatronTrx__GrossUnitPrice__c',
    'PatronTrx__ItemName__c',
    'PatronTrx__ItemNumber__c',
    'PatronTrx__ItemType__c',
    'PatronTrx__PatronTechUnitFee__c',
    'PatronTrx__Quantity__c',
    'PatronTicket__TicketOrderItem__c',
    'PatronTrx__FullBuyerCost__c',
    'PatronTrx__FullGrossAmount__c',
    'PatronTrx__TotalItemQuantity__c',
    'PatronTrx__SalesTax__c',
    'PatronTicket__SubscriptionBuyerSelectionLink__c',
    'PatronTicket__TicketPriceLevel__c',
    'PatronTrx__UnitFee2__c',
    'PatronTrx__UnitFee3__c',
    'PatronTrx__UnitFee4__c',
    'PatronTrx__UnitFee5__c',
    'PatronTrx__TaxDeductibleAmount__c',
    'PatronTrx__TaxDeductibleDonation__c'
    ]

    return columns

def get_merging_dictionary():
    dictionary = {
        'Id_x' : 'patron_transaction_id',
        # 'OwnerId',
        # 'IsDeleted_x',
        # 'Name_x',
        # 'CreatedDate_x',
        # 'CreatedById_x',
        # 'LastModifiedDate_x',
        # 'LastModifiedById_x',
        # 'SystemModstamp_x',
        'PatronTrx__BuyerFeeLineItemSubtotal__c' : 'buyer_fee_line_item_sub_total',
        # 'PatronTrx__BuyerOrderFee__c',
        'PatronTrx__CaptureTransactionId__c' : 'capture_transaction_id',
        # 'PatronTrx__ClearedDate__c',
        'PatronTrx__DiscountAmount__c' : 'discount_amount',
        'PatronTrx__DonationAmount__c' : 'donation_amount',
        # 'PatronTrx__ExternalTransactionID__c',
        'PatronTrx__FirstName__c' : 'first_name',
        'PatronTrx__LastName__c' : 'last_name',
        # 'PatronTrx__OrderId__c',
        # 'PatronTrx__OrderName__c',
        'PatronTrx__OrderOrigin__c' : 'order_origin',
        # 'PatronTrx__OrganizationId__c',
        # 'PatronTrx__OrganizationName__c',
        'PatronTrx__PatronTechFeeLineItemSubtotal__c' : 'patron_tech_fee_line_item_sub_total',
        # 'PatronTrx__PatronTechOrderFee__c',
        'PatronTrx__PaymentMethod__c' : 'payment_method',
        # 'PatronTrx__ReferenceTransaction__c',
        'PatronTrx__ShippingFee__c' : 'shipping_fee',
        'PatronTrx__Status__c' : 'status',
        'PatronTrx__TransactionDate__c' : 'transaction_date',
        # 'PatronTrx__TransactionFee__c',
        # 'PatronTrx__TransactionId__c',
        'PatronTrx__TransactionTotal__c' : 'transaction_total',
        'PatronTicket__TicketOrder__c' : 'ticket_order_id',
        # 'PatronTrx__CurrencyCode__c',
        # 'PatronTrx__CreditCardType__c',
        # 'PatronTrx__CreditCardTransactionFee__c',
        'PatronTrx__ExchangeFee__c' : 'exchange_fee',
        # 'PatronTrx__Opportunity__c',
        'PatronTrx__PaymentProcessor__c' : 'payment_processor',
        # 'PatronTrx__SalesTaxLineItemSubtotal__c',
        # 'PatronTrx__StoredPaymentMethod__c',
        # 'PatronTicket__BatchCreationDate__c',
        'PatronTicket__ExchangeType__c' : 'exchange_type',
        # 'PatronTrx__Fee3__c',
        # 'PatronTrx__Fee4__c',
        # 'PatronTrx__Fee5__c',
        # 'PatronTrx__SalesTaxOrderLevel__c',
        'PatronTicket__EntryMethod__c' : 'entry_method',
        # 'PatronTrx__AuthorizationCode__c',
        # 'PatronTrx__BatchDate__c',
        # 'PatronTrx__PaymentGatewaySettings__c',
        'PatronTrx__AmountTendered__c' : 'amount_tendered',
        'PatronTrx__NameOnCard__c' : 'name_on_card',
        # 'PatronTrx__CreditCardBIN__c',
        # 'PatronTrx__GiftCardNumber__c',
        # 'PatronTrx__CreditRefundType__c',
        'PatronTrx__CreditCardEntryMethod__c' : 'credit_card_entry_method',
        'PatronTrx__CreditCardLastFour__c' : 'credit_card_last_four',
        'Id_y' : 'transaction_item_id',
        # 'IsDeleted_y',
        'Name_y' : 'transaction_id',
        'CreatedDate_y' : 'create_date',
        # 'CreatedById_y',
        # 'LastModifiedDate_y',
        # 'LastModifiedById_y',
        # 'SystemModstamp_y',
        # 'PatronTrx__PaymentTransaction__c' : 'payment_transaction',
        'PatronTrx__BuyerUnitFee__c' : 'buyer_unit_fee',
        'PatronTrx__BuyerUnitPrice__c' : 'buyer_unit_price',
        'PatronTrx__GrossUnitPrice__c' : 'gross_unit_price',
        'PatronTrx__ItemName__c' : 'item_name',
        'PatronTrx__ItemNumber__c' : 'item_id',
        'PatronTrx__ItemType__c' : 'item_type',
        'PatronTrx__PatronTechUnitFee__c' : 'patron_tech_unit_fee',
        'PatronTrx__Quantity__c' : 'quantity',
        'PatronTicket__TicketOrderItem__c' : 'ticket_order_item_id',
        'PatronTrx__FullBuyerCost__c' : 'full_buyer_cost',
        'PatronTrx__FullGrossAmount__c' : 'full_gross_amount',
        'PatronTrx__TotalItemQuantity__c' : 'total_item_quantity',
        # 'PatronTrx__SalesTax__c',
        # 'PatronTicket__SubscriptionBuyerSelectionLink__c',
        # 'PatronTicket__TicketPriceLevel__c',
        'PatronTrx__UnitFee2__c' : 'unit_fee',
        # 'PatronTrx__UnitFee3__c',
        # 'PatronTrx__UnitFee4__c',
        # 'PatronTrx__UnitFee5__c',
        # 'PatronTrx__TaxDeductibleAmount__c',
        # 'PatronTrx__TaxDeductibleDonation__c'
    }
    return dictionary


def organize_columns(df):

    # Hash Salesforce ID columns first
    id_columns = ['transaction_id', 'patron_transaction_id', 'ticket_order_id',
                  'ticket_order_item_id', 'capture_transaction_id', 'item_id']

    for col in id_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: hash_to_int(x))

    organized_columns = [
        # Transaction Identifiers
        'transaction_id',
        'patron_transaction_id',
        'ticket_order_id',
        'item_id',
        'ticket_order_item_id',
        'capture_transaction_id',

        # Item Details
        'item_type',
        'item_name',

        # Payment Information
        'payment_method',
        'status',
        'payment_processor',

        # Exchange and Order Information
        'exchange_type',
        'order_origin',

        # Entry Methods
        'entry_method',
        'credit_card_entry_method',

        # Credit Card Information
        'credit_card_last_four',
        'name_on_card',

        # Patron Information
        'first_name',
        'last_name',

        # Dates
        'transaction_date',
        'create_date',

        # Quantity and Price
        'quantity',
        'buyer_unit_price',
        'gross_unit_price',

        # Fees
        'buyer_unit_fee',
        'patron_tech_unit_fee',
        'unit_fee',

        # Totals and Subtotals
        'total_item_quantity',
        'buyer_fee_line_item_sub_total',
        'patron_tech_fee_line_item_sub_total',

        # Additional Fees and Discounts
        'shipping_fee',
        'exchange_fee',
        'discount_amount',

        # Donation
        'donation_amount',

        # Final Amounts
        'full_buyer_cost',
        'full_gross_amount',
        'transaction_total',

        # Tendered Amount
        'amount_tendered'
    ]

    df = df[organized_columns]

    return df

def hash_to_int(column_value, mod_value=2**32):
    # Create a SHA-256 hash of the column value
    hash_object = hashlib.sha256(str(column_value).encode())
    # Convert the hash to a hexadecimal string
    hex_hash = hash_object.hexdigest()
    # Convert the hexadecimal string to an integer and modulate it
    int_hash = int(hex_hash, 16) % mod_value
    return int_hash