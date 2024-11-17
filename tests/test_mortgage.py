"""
Description: A class used to test the Mortgage class.
Author: Matt Kenyon
Date: 2024-11-17
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    """
    Description: This class will be used to contain test cases for other classes. 

    Args:
    """

    
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
        Rate = "FIXED_5"
        Frequency = 42
        Amortization = "10"

        expected = "Frequency provided is invalid."
        #Act & Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, Rate, Frequency, Amortization)
        
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

        #expected_rate = 0.0519
        #expected_frequency = 12

        
        #Act
        mortage = Mortgage(loan_amount, rate, frequency, amortization)

        #Assert
        self.assertEqual(loan_amount, mortage._Mortgage__loan_amount)
        self.assertEqual(MortgageRate.FIXED_5, mortage._Mortgage__rate) 
        self.assertEqual(PaymentFrequency.MONTHLY, mortage._Mortgage__frequency) 
        self.assertEqual(amortization, mortage._Mortgage__amortization)  


    #if __name__ == '__main__':
    #   TestCase.main()
    
    



