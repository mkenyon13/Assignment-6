"""
Description: A class meant to manage Mortgage options.
Author: Matt Kenyon
Date: 2024-11-11
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

#Import Enumerations and list from pixell_lookup
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


class Mortgage():
    """
    Description: This class will be used to calculate mortage payments. 

    Args:
        Loan_Amount (float): The amount of money that will be borrowed.

        Rate (str): The percentage rate at which interest will be applied to the loan.

        Frequency (str): How often the user will make payments. 

        Amortization (str): The amount of time in years that the loan will be payed.
        
    """
    def __init__(self, Loan_Amount: float, Rate: str, Frequency: str, Amortization: str):
        self.Loan_Amount = Loan_Amount
        self.Rate = Rate
        self.Frequency = Frequency
        self.Amortization = Amortization

        #Implimenting __init__ attributes
        if Loan_Amount <= 0:
            raise ValueError("Loan Amount must be positive")
        
        try:
            self.__rate = MortgageRate[Rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        try:
            self.__frequency = PaymentFrequency[Frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

        if Amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")





