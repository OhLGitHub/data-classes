# Part I: Create Data Classes for Orders, Invoices, Customers

# Part IIA: Override the comparison operators for > and >=
# to compare orders to other orders

# Part IIB: Override the comparison operators to compare
# invoices to other invoices

from dataclasses import dataclass, field
import dataclasses
from datetime import date, datetime

@dataclass
class Orders:
    """
    This is a class for orders.
    """
    orderID: int
    customerID: int
    salesperson_personID: int
    pickedby_personID: int
    contact_personID: int
    backorder_orderID: int
    orderdate: date
    expected_deliverydate: date
    customerpurchase_ordernumber: str
    is_undersupplybackordered: bool
    comments: str
    deliveryinstructions: str
    internalcomments: str
    pickingcompletedwhen: datetime
    lastedited_by: int
    lastedited_when: datetime

    def __gt__(self,other):
        if self.orderID > other.orderID:
            return self.orderID > other.orderID
        else:
            return False
    
    def __ge__(self,other):
        if self.orderID >= other.orderID:
            return self.orderID >= other.orderID
        else:
            return False

@dataclass
class Invoices:
    """
    This is a class for invoices.
    """
    invoiceID: int
    customerID: int
    billto_customerID: int
    orderID: int
    deliverymethodID: int
    contact_personID: int
    accounts_personID: int
    salesperson_personID: int
    packedby_personID: int
    invoicedate: date
    customerpurchase_ordernumber: str
    is_creditnote: bool
    creditnotereason: str
    comments: str
    deliveryinstructions: str
    internalcomments: str
    total_dryitems: int
    total_chilleritems: int
    deliveryrun: str
    runposition: str
    returned_deliverydata: str
    confirmed_deliverytime: datetime
    confirmed_receivedby: str
    lastedited_by: int
    lastedited_when: datetime

    def __gt__(self,other):
        if (self.total_dryitems + self.total_chilleritems) > (other.total_dryitems + other.total_chilleritems):
            return self.invoiceID > other.invoiceID
        else:
            return False
    
    def __ge__(self,other):
        if (self.total_dryitems + self.total_chilleritems) >= (other.total_dryitems + other.total_chilleritems):
            return self.invoiceID >= other.invoiceID
        else:
            return False

@dataclass
class Customers:
    """
    This is a class for customers.
    """
    customerID: int
    customername: str
    billto_customerID: int
    customercategoryID: int
    buyinggroupID: int
    primarycontact_personID: int
    alternatecontact_personID: int
    deliverymethodID: int
    delivery_cityID: int
    postal_cityID: int
    creditlimit: float
    accountopeneddate: date
    standarddiscountpercentage: float
    is_statementsent: bool
    is_oncredithold: bool
    paymentdays: int
    phonenumber: str
    faxnumber: str
    deliveryrun: str
    runposition: str
    websiteurl: str
    deliveryaddressline1: str
    deliveryaddressline2: str
    deliverypostalcode: str
    deliverylocation: str
    postaladdressline1: str
    postaladdressline2: str
    postalpostalcode: str
    lastedited_by: int
    validfrom: datetime
    validto: datetime