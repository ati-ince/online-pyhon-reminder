#prepare hashcode creating for that 
import hashlib 
def get_HashFrmTxt(text:str)->(str):
    '''for any string value can transform hash code and use for comparison without long text naming'''
    res = hashlib.md5(text.encode())
    return res.hexdigest()

import string    
import random # define the random module  

def random_str(len_ = 25):
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = len_))  
    # print("The randomly generated string is : " + str(ran)) # print the random data 
    
    return ran, get_HashFrmTxt(ran)