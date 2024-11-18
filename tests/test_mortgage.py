"""
Description: A class used to test the Mortgage class.
Author: Matt Kenyon
Date: 2024-11-17
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
    """
    Description: This class will be used to contain test cases for other classes. 

    Args:
    """
    ## Attribute Tests
    def test_init_invalid_amount(self):
        #Arange
        loan_amount = -5000
        Rate = "FIXED_1"
        Frequency = "MONTHLY"
        Amortization = "10" 
        
        expected = "Loan Amount must be positive"
        #Act & Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, Rate, Frequency, Amortization)
        
        self.assertEqual(expected, str(context.exception))
        

    def test_init_invalid_rate(self):
        #Arange
        loan_amount = 5000
        Rate = 42
        Frequency = "MONTHLY"
        Amortization = "10"

        expected = "Rate provided is invalid."
        #Act + Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, Rate, Frequency, Amortization)
        
        self.assertEqual(expected, str(context.exception))
        

    def test_init_invalid_frequency(self):
        #Arange
        loan_amount = 5000
        rate = "FIXED_5"
        frequency = 42
        amortization = "10"

        expected = "Frequency provided is invalid."
        #Act & Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        
        self.assertEqual(expected, str(context.exception))
        
        

    def test_init_invalid_amortization(self):
        #Arange
        loan_amount = 5000
        Rate = "FIXED_5"
        Frequency = "MONTHLY"
        Amortization = 13

        expected = "Amortization provided is invalid."
        #Act & Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, Rate, Frequency, Amortization)
        
        self.assertEqual(expected, str(context.exception))
        
        

    def test_init_valid_inputs(self):
        #Arange
        loan_amount = 5000
        rate = "FIXED_5"
        frequency = "MONTHLY"
        amortization = 10
        
        #Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        #Assert
        self.assertEqual(loan_amount, mortgage._Mortgage__loan_amount)
        self.assertEqual(MortgageRate.FIXED_5, mortgage._Mortgage__rate) 
        self.assertEqual(PaymentFrequency.MONTHLY, mortgage._Mortgage__frequency) 
        self.assertEqual(amortization, mortgage._Mortgage__amortization)

    ## Accessor & Mutator Tests
    def test_loan_amount_mutator_negative(self):
        #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)                 
        
        #Act        
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -42
        
        #Assert
        self.assertEqual("Loan Amount must be positive.", str(context.exception))


    def test_loan_amount_mutator_zero(self):
        #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)                 
        
        #Act        
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        
        #Assert
        self.assertEqual("Loan Amount must be positive.", str(context.exception))
    
    def test_loan_amount_mutator_positive(self):
        #Arange
        expected_loan_amount = 7500 

        #Act
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)
        mortgage.loan_amount = expected_loan_amount
        #Assert
        
        self.assertEqual(expected_loan_amount, mortgage.loan_amount)


    def test_rate_mutator_type_valid(self):
         #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)        
        expected = MortgageRate.FIXED_5 
        
        #Act
        mortgage.rate = MortgageRate.FIXED_5
        
        #Assert        
        self.assertEqual(expected, mortgage.rate)

    #This test isn't working 
    def test_rate_mutator_type_invalid(self):
        #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)        
        expected = "Rate provided is invalid." 
        
        #Act
        with self.assertRaises(ValueError) as context:
            mortgage.rate = "INVALID" 
        
        #Assert        
        self.assertEqual(expected, str(context.exception))

    def test_frequency_mutator_type_valid(self):
         #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)        
        expected = PaymentFrequency.MONTHLY
        
        #Act
        mortgage.frequency = PaymentFrequency.MONTHLY
        
        #Assert        
        self.assertEqual(expected, mortgage.rate)

    #This test isn't working 
    def test_frequency_mutator_type_invalid(self):
        #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)        
        expected = "Frequency provided is invalid." 
        
        #Act
        with self.assertRaises(ValueError) as context:
            mortgage.frequency = "INVALID" 
        
        #Assert        
        self.assertEqual(expected, str(context.exception))

    def test_amortization_mutator_type_valid(self):
         #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)        
        expected = 10
        
        #Act
        mortgage.ammortization = VALID_AMORTIZATION[1]
        
        #Assert        
        self.assertEqual(expected, mortgage.ammortization)

    #This test isn't working 
    def test_amortization_mutator_type_invalid(self):
        #Arange
        mortgage = Mortgage(5000,"FIXED_5", "MONTHLY", 10)        
        expected = "Amortization provided is invalid." 
        
        #Act
        with self.assertRaises(ValueError) as context:
            mortgage.ammortization = "INVALID" 
        
        #Assert        
        self.assertEqual(expected, str(context.exception))

    
    #if __name__ == '__main__':
    #   TestCase.main()
    
    



