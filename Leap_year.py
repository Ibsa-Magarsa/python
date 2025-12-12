def is_leap(year):
    if year % 4 == 0:
        if year %100 ==0:
            if year ==0:
                # print("Leap Year. ")
                return True 
            else:
                # print("Not Leao Year. ")
                return False
        else:
            # print("Leap Year. ")
            return True 
    else:
        # print("Not Leap Year. ")
        return False 
