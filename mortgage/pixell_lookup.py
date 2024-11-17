"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Matt Kenyon
Date: 2024-11-17
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum


#A class containing fixed and variable mortgage rates
class MortgageRate(Enum):
    
    """
    Description: This class contains various mortage rate amounts for caclulations later.

    Args:
        FIXED (float): The fixed mortage rate options

        VARIABLE (float): Variable mortgage rate options  
    """
    
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679

#A class that stores how often payments can be made.
class PaymentFrequency(Enum):
    """
    Description: This class contains the available payment periods.

    Args:
        MONTHLY (int): A payment period that occurs 12 times a year.

        BI_WEEKLY (int): A payment period that occurs 26 times a year.

        WEEKLY (int): A payment period that occurs 52 times a year.
    """
    
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
    
#A variable that stores how many years the mortgage can be made.
VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}    
    