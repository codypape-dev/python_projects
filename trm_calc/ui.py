# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:31:19 2023

@author: Paula Perdomo
"""

import library as lb

def exec_conv_curr_to_usd(trm : float, curr_code: str) -> None:
    
    curr = float(input("Enter the currency amount: "))
    usd = lb.conv_curr_to_usd(curr, trm)
    print(round(curr), curr_code, " equals to: ", round(usd, 2), "USD")
          
def exec_conv_usd_to_curr(trm : float, curr_code: str) -> None:
    usd = float(input("Enter the USD amount: "))
    curr = lb.conv_usd_to_curr(usd, trm)
    print(round(usd, 2), "USD equals to: ", round(curr), curr_code)

def exec_app() -> None:
    curr_code = str.upper(input("Enter your currency code: "))
    trm = float(input("Enter the TRM for {} to USD: ".format(curr_code)))
    exec_conv_curr_to_usd(trm, curr_code)
    exec_conv_usd_to_curr(trm, curr_code)
    
exec_app()
