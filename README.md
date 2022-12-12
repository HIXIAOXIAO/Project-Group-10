# Fruits Purchase System 
## Group 10 
## Xiaoxiao Fu & Ujjwal Upadhyay
### 1. Description of the package
Our project topic is Fruits Purchase System. We create two sub-packages named as customer and produce. The main modules in these sub-packages are Customer.py, which manages customers’ purchasing needs. Search.py is used for customers to search for fruits’ storage, price, and notification words. Fruits.py is used to set different fruits' information, like price, discount, inventory and expiry time. Inventory.py are used for record the fruits’ inventory information.

### 2.Description of the functions
#### (1)Functions in Customer.py
set_budget() : customers use this function to enter budgets.
shop_item(): prevent duplicate entry. If customers enter the same fruits, the systerm will notice that "Please do not enter the same fruit."
items_detail(): show purchase list.
get_items():clear purchase list according to the users' choice.
#### (2)Functions in Search.py
