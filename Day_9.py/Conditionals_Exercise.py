# optimize/shorten the code in the function
# try to reduce the number of conditionals 


from calendar import month


def num_days(month):

   if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
    print('number of days in',month,'is',31)
   elif month == 'feb':
    print ('number of days in ',month,'is',28)
   elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
    print('number of days in',month,'is',30)
    
num_days('jan')
num_days('feb')

def num_days(month):
  days = 31
  if month in ['apr', 'jun', 'sep', 'nov']:
    days = 30   
  elif month == 'feb':
    days = 28
  print('number of days in', month, 'is', days)

num_days('apr')