print('khurram khalil')
from datetime import date
print('enter the date in formate of your desktop')
#enter date like date (which you wan tto find the diff)
initial_date=eval(input('enter the starting date in your PC format: '))

final_date=eval(input('enter the ending date in your PC format: '))

num_of_days= final_date - initial_date
print('you got', num_of_days.days, 'days between these two dates')
