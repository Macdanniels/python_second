

#commision_rate calculator.

advanced = 2000


def mainfunction():
    print('Commission Rate Calculator:')
   
    sales = float(input('Enter your monthly sale: '))
    ad_pay = float(input('Enter Advanced payment: '))
    print('')
    
    amount_advanced(ad_pay)
    monthly_sale(advanced_pay=ad_pay, sale = sales) 
    
    
    # commission_rate(payment)
 
# def commission_rate(payment):
    



def amount_advanced(advanced_pay):
    
    diff = advanced - advanced_pay
    if(diff > 0):
        print('You need to reimburse: $',diff)
        print('your advanced pay is: ', advanced_pay)
        print('')
       

        # return diff
        
    else: 
        print('you can borrow up to $2000')
        
       


def monthly_sale(advanced_pay, sale):

   
    if sale <= 9999:
        pay = (sale *  0.1 - advanced_pay)
        print('This is your pay : ', '$', +pay)
        # print('This is your pay 1: ', advanced_pay)
        
    elif sale == 10000 or sale <=14999:
        pay = (sale *   0.12) -  advanced_pay
        print('This is your pay : ', '$',+pay)

    elif sale == 15000 or sale <=17999:
        pay = (sale *  0.14) -  advanced_pay
        print('This is your pay : ', '$'+pay)

    elif sale == 18000  or  sale <=21999:
        pay = (sale *  0.16) -  advanced_pay
        print('This is your pay : ', '$',+pay)
  
    elif sale >= 22000:
        pay = (sale *  0.18) -  advanced_pay
        
        print('This is your pay : ', '$',+pay)
        print('your sale: ', sale)
       

        return pay    
        
    
mainfunction()