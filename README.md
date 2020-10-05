# microFlipcart

A micro version of the ecommerce site, with the following supports:

Types of user and their roles/functions/privileges:


1. ###### Admin:

	> Login using username and password.
	
	> Create users for roles (customer, sales-agent)
	
	> Create new products and update existing products. 
	
	> Update product info
	
	> Update current price
	
	> Update current stock level
	
	> Update product status - currently eligible for selling



2. ###### Customer:

	> Login using mobile number and an OTP (mocking OTP will be sufficient)
	
	> View products for sale
	
	> Place an order for multiple products:
	
	> While placing a new order, the customer's last purchase price for every product that has been purchased in the past should be shown along with the current price.
	
	> Only products which are “In stock” should be allowed to order.
	
	> View past orders



3. ###### Sales Agent: 

	> Login using username and password. View orders for all customers.
	
	> Process an Order: Update order status [“Accepted”, “Delivered”, “Cancelled”]	
	
	> On order accept: An SMS is sent to the customer (Hint: Make it asynchronous.)
	


###### Username -  Phone  - Password

Administrator

* admin - +919007007007 - admin

Salesman

* salesman - +919871199217 - person@1990


Customers

* alfred - +919871199210 - alfred@1990

* albus - +919871199211 - albus@1990

* louis - +919871199212 - louis@1990

* salazar - +919871199213 - salazar@1990

* slytherin - +919871199214 - salazar@1990

* godric - +919871199215 - hollows@1990



###### Assumptions/Constraints:
1. Each product when entered into stock, would include more than just name in the title/name of the product, as seen on most of the ecommerce website.
Something like this - *Apple iPhone 11 (64GB) - Black*.  This helps in formatting the view of *price of older ordered products*. Although, can be explicitly extended to support more filtering criteria

2. Register link works and creates customer-type users. So to convert a customer to a *is_admin*, *is_staff* user, login using admin and update the user permissions there. 
