def price(amount,distance):
    final=amount+distance
    return final
def coupons(final):
    c=""
    if(final<=100):
        coupons="voucher for 20% off!"
        return coupons
    else:
        coupons="Buy One, Get One offer!"
        return coupons
