# API_Storage_Products


an API it's a set of definitions and protocols used to develop and integrate application software, allowing communication between two software applications through a set of rules.


This is an api designed to communicate a product page and its database, with the API you can create users and log into the page with the user that you create.

Also, you can save products for the online store with the following information

To create a new user you need: 
- first_name.
- last_name.
- identity_card.
- phone.
- email.
- birthday.
- username.
- password.



To create a product you need:
- name.
- long_description.
- short_description.
- dimensions.
- weight.
- image_one.
- image_two.
- image_three.
- image_four.
- quantity.
- price.

You have the following routes:

Post:

    - http://localhost:2000/register  -> Allows to register a new user in the page.
    - http://localhost:2000/product  -> Allows to register a new product in the page.
    - http://localhost:2000/login  -> Allows you to log into the page with the registered account.

Get:

    - http://localhost:2000/product  -> Allows you to obtain all the products in the database.
    - http://localhost:2000/product/[id]  -> Allows you to obtain a product by its ID.
    - http://localhost:2000/user  -> Allows you to get all registered users.





