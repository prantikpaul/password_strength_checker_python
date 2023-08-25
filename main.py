# #password strength checker
def chck_pass_strnth(pss):
    lenght_need = len (pss) >= 8
    upper_need = any(char.isupper() for char in pss )
    lower_need = any(char.islower() for char in pss )
    contain_num = any(char.isnumeric() for char in pss)
    if lenght_need & lower_need & upper_need & contain_num:
        return "Your Password is Strong"
    elif lenght_need & lower_need & contain_num  :
        return "Your Password is Medium"
    elif lenght_need & lower_need or contain_num :
        return "Your Password is weak"
    else :
        return 'Your password must contain atleast 8 characters '


psck = input('Please Enter a password :')
pp = chck_pass_strnth(psck)
print(pp)
