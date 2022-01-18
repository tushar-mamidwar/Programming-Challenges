def purches_product(product,price,material=None,brand=None):
    if product=='mobile':
        if brand=='Apple':
            discount=10
        else:
            discount=5
    total=price-price*discount/100
    if product=="shoe":
        if material=="leather":
            tax=5
        else:
            tax=2
        total=price+price*tax/100
    print(" Total price of "+product+" is " +str(total))
   
purches_product("mobile",20600)