"""
Description: A class meant to manage Mortgage options.
Author: Matt Kenyon
Date: 2024-11-17
Usage: Create an instance of the Mortgage class to store data which can be used for mortagage calculation.
"""

#Import Enumerations and list from pixell_lookup
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


class Mortgage:
    """
    Description: This class will be used to collect data for mortage payments.

    Attributes:
        __loan_amount (float): The amount of money that will be borrowed.
        __rate (str): The percentage rate at which interest will be applied to the loan.
        __frequency (str): How often the user will make payments. 
        __amortization (str): The amount of time in years that the loan will be payed.
    Methods:
        
    """
    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: str):
        """
        Description: Initializes parameters for the class Mortgage.
        
        Args:
            loan_amount (float): The amount of money that will be borrowed.
            rate (str): The percentage rate at which interest will be applied to the loan.
            frequency (str): How often the user will make payments. 
            amortization (str): The amount of time in years that the loan will be payed.

        Raises:
            ValueError: If the loan ammount is less than 0 or negative.
            ValueError: If the rate is invalid.
            ValueError: If the frequency is invalid.
            ValueError: If the ammortization is invalid.
        """        
        
        self.__loan_amount = loan_amount
        self.__amortization = amortization

        if self.__loan_amount <= 0:
            raise ValueError("Loan Amount must be positive")


        try:
            self.__rate = MortgageRate[rate]
        except Exception as e:
            print(e)
            raise ValueError("Rate provided is invalid.")


        try:
            self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        

        if self.__amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        

## ACCESSORS 

    # loan_amount ACCESSORS 
    @property
    def loan_amount(self) -> float:
         """
         Accessor for loan_amount attribute
         """
         return self.__loan_amount
    
    # rate ACCESSORS    
    @property
    def rate(self) -> str:
         """
         Accessor for _rate attribute
         """
         return self.__rate

    # frequency ACCESSORS    
    @property
    def frequency(self) -> str:
         """
        Accessor for _frequency attribute
         """
         return self.__frequency

    # ammortization ACCESSORS 
    @property
    def ammortization(self) -> str:
         """
         Accessor for _ammortization attribute
         """
         return self.__amortization

# MUTATORS

    # loan_amount MUTATORS
    @loan_amount.setter
    def loan_amount(self, value: float):
        """
        Checks if the loan amount is positive.
        Args:
            value (str): The loan amount.
        Raises:
            ValueError: When the value provided is 
            negative.
        """
                
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        self.__loan_amount = value


    # # loan_amount MUTATORS
    # @loan_amount.setter
    # def loan_amount(self, value: str):
    #     """"""

    # # loan_amount MUTATORS
    # @loan_amount.setter
    # def loan_amount(self, value: str):
    #     """"""

    # # loan_amount MUTATORS
    # @loan_amount.setter
    # def loan_amount(self, value: str):
        """"""








