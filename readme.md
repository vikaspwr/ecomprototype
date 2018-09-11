# Descriptions
    This project is prototype of ecommerce basic APIs for add products,
    edit products, get products, delete products.

# Technology
    1. Python 2.7.15
    2. django 1.10
    3. djangorestframework 3.8.2
    4. Pillow   5.2.0 (For ImageFileField)
    5. sqllite database

# How to run the project.
    Installation:
    The below steps assumes that python 2.7 is installed and python path is set in environment variable.
    
    1. pip install django==1.10
    2. pip install djangorestframework==3.8.2
    3. pip install pillow==5.2.0
    
    Download the project and go to the ecommerce directory in cmd/terminal where manage.py file is located.
    
    Run the below command:
    
    python manage.py runserver
    
    The default username and password are:
    username: vikas
    password: admin@123
    
    However you can create new user by using below command:
    
    python manage.py createsuperuser
    
# Notes
    In all below APIs the headers in required in all the APIs except login api.
    
#TODO
    1. Logging
    2. CONFIG
    3. Optimization
    4. Test Cases
    5. Deployment to PAAS
    6. Auto Setup.
    7. Edit Product
    
#API
    Below are all the APIs mentioned.
   
    The Category APIs does not have any dependency.
    The SubCategory APIs has dependency on the Category APIs.
    The Supplier APIs does not have any dependency.
    The product APIs has dependency on the Category, Sub Category and Supplier APIs. 

#Login API

    URL: 
        /api/login
 
    Method: 
        POST

    Headers: 
        None

    PARAMS (Form-Data): 
        1. username (required)
        2. password (required)

    Returns:
        {
            "token": "ee13837e01b58f7144e8872edae13d4a8dda54af"
        }

    Raises: 
        1. if username or password params missing:
            response: 
            {'error': 'Please provide both username and password.'} 
            code: 400 BAD_REQUEST
            
        2. if user is not authenticated:
            response:
            {'error': 'Invalid Credentials.'}
            code: 404 NOT_FOUND


# CATEGORY API

###1. ADD CATEGORY:
	URL: 
	    /api/category
	
	METHOD: 
	    POST
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
		1. category_name (required)
		
	RETURNS:
		MESSAGE : {'success': "Category X added successfully."}
		CODE    : 200_OK
		NOTES   : X is refer to the value which is sent to server.
	
	RAISES:
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST
			
		2.	if user is not superuser.
		
			MESSAGE	: {'error': 'You don\'t have permissions to edit category. Please contact administrator'}
			CODE	: 400 BAD_REQUEST
		
		3.	if category_name form data not provided.
		
			MESSAGE	: {'error': 'Category name is not provided.'}
			CODE	: 400 BAD_REQUEST
	
		4. if category name is already exists.
		
			MESSAGE	: {'error': 'Category name "{0}" is already exist.'}
			CODE	: 400 BAD_REQUEST

###2. GET CATEGORY:
	
	URL: 
	    /api/category
	
	DESCRIPTIONS: 
	    This URL and GET method is returns all the category from database.
	
	METHOD: 
	    GET
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
			None
		
	RETURNS:
			DATA:	[
						{
							"Response": true
						},
						[
							{
								"id": 1,
								"name": "Electronics"
							},
							{
								"id": 3,
								"name": "Automobiles"
							}
						]
					]
					
    CODE:   
        200 OK
		
	RAISES: 
		Runtime errors if any.


###3. PUT CATEGORY:

	URL: 
	    /api/category
	
	DESCRIPTIONS: 
	    This URL and PUT method is use to edit the category name in database. This operation can be done by only superuser.
	
	METHOD: 
	    PUT
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
		1. category_name (required)
		2. id			 (required)
	
    RETURNS:
        {
            "success": "The category name has been updated from \"Electronic\" to \"Electronics\"."
        }
		
    CODE: 
        200 OK
	
	RAISES:
	
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST
			
		2.	if user is not superuser.
		
			MESSAGE	: {'error': 'You don\'t have permissions to edit category. Please contact administrator'}
			CODE	: 400 BAD_REQUEST
		
		3.	if category_name or id not provided in form data.
		
			MESSAGE	: {'error': 'Category name and id must be provided.'}
			CODE	: 400 BAD_REQUEST
	
		4. if category name and id is provided in form data but the value is Null.
		
			MESSAGE	: {'error': 'Category name and id should not be None.'}
			CODE	: 400 BAD_REQUEST


# SUB CATEGORY

###1. ADD SUB CATEGORY:
	URL: 
	    /api/subcategory
	
	METHOD: 
	    POST
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
		1. sub_category_name (required)
		2. category_id		 (required)
		
	RETURNS:
		MESSAGE: {'success': "Sub Category \"X"\ added successfully."}
		CODE: 	 200_OK
		NOTES   : X is refer to the value which is sent to server.
	
	RAISES:
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST
			
		2.	if user is not superuser.
		
			MESSAGE	: {'error': 'You don\'t have permissions to edit category. Please contact administrator'}
			CODE	: 400 BAD_REQUEST
		
		3.	if sub_category_name and category_id field is missing or not not provided in form data.
		
			MESSAGE	: {'error': 'sub_category_name and category_id field is missing or not provided.'}
			CODE	: 400 BAD_REQUEST
	
		4. if sub category name is already exists.
		
			MESSAGE	: {'error': 'Sub Category name \"{0}\" is already exist.'}
			CODE	: 400 BAD_REQUEST

			
###2. GET SUB CATEGORY:
	URL: 
	    /api/subcategory
	
	METHOD: 
	    GET
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
		None

# Supplier

###1. ADD Supplier:
URL: 
	    /api/subcategory
	
	METHOD: 
	    POST
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
		1.  name            (required)
		2.  email           (required)
		3.  phone           (required)
		4.  first_name      (optional)
		5.  last_name       (optional)
		6.  address         (optional)
		7.  city            (optional)
		8.  state           (optional)
		9.  pincode         (optional)
		10. logo            (optional)
		
		
	RETURNS:
		MESSAGE : {"success":"Sub Category \"X\" added successfully."}
		CODE    : 200_OK
		NOTES   : X is refer to the value which is sent to server.
	
	RAISES:
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST
			
		2.	if user is not superuser.
		
			MESSAGE	: {'error': 'You don\'t have permissions to edit category. Please contact administrator'}
			CODE	: 400 BAD_REQUEST
		
		3.	if name, email and phone field is missing or not not provided in form data.
		
			MESSAGE	: {'error': 'name, email and phone field must be provided.'}
			CODE	: 400 BAD_REQUEST
			
		4.  if name, email and phone field is passed in form data but value is Null.
		
			MESSAGE	: {'error': 'name, email and phone field should not be Null.'}
			CODE	: 400 BAD_REQUEST
			
		5.  if email id is not valid.
		    MESSAGE : {'error': 'Email id X is not valid email id.'}
		    CODE    : 400 BAD_REQUEST
		    NOTES   : X is refer to the value which is sent to server.
        
        6.  if phone number is not numeric.
            
            MESSAGE  : {'error': 'Phone number X is not valid.'}
            CODE     : 400 BAD_REQUEST
            NOTES    : X is refer to the value which is sent to server. 


###1. GET Supplier:
    
    URL: /api/supplier
	
	METHOD: 
	    GET
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
    
    PARAMS:
        None
    
    RETURNS:
        returns all the result.
        
        [
    {
        "success": true
    },
    [
        {
            "id": 1,
            "name": "ABC India Pvt Ltd",
            "email": "x@XXXX.com",
            "phone": 9999999999,
            "first_name": null,
            "last_name": null,
            "address": null,
            "city": null,
            "state": null,
            "pincode": null,
            "logo": null,
            "is_active": false
        },
        {
            "id": 2,
            "name": "DEF India Pvt Ltd",
            "email": "def@def.com",
            "phone": 8888888888,
            "first_name": "Admin",
            "last_name": "Admin",
            "address": "Ahmedabad",
            "city": "Ahmedabad",
            "state": "Gujarat",
            "pincode": 38001,
            "logo": "/media/myw3schoolsimage_1.jpg",
            "is_active": false
        }
    ]
]

# Product

###1. ADD Product:
URL: 
	    /api/product
	
	METHOD: 
	    POST
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
	
	PARAMS:
		1.  category_id             (required)
		2.  sub_category_id         (required)
		3.  supplier_id             (required)
		4.  name                    (required)
		5.  description             (required)
		6.  sku                     (required)
		7.  price                   (required)
		8.  quantity                (required)
		
		Note: Multiple image can be send to server at a onetime. with name of image1, image2 to imageN
		9.  image1                  (optional File field)
		10. image2                  (optional File field)
		11. image3                  (optional File field)
		
		
	RETURNS:
		MESSAGE : {"success":"Product \"X\" added successfully."}
		CODE    : 200_OK
		NOTES   : X is refer to the value which is sent to server.
	
	RAISES:
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST
			
		2.	if user is not superuser.
		
			MESSAGE	: {'error': 'You don\'t have permissions to edit category. Please contact administrator'}
			CODE	: 400 BAD_REQUEST
		
		3.	if sub_category_id, category_id, supplier_id, name, description, sku, price, and quantity field is missing or not not provided in form data.
		
			MESSAGE	: {'error': "sub_category_id, category_id, supplier_id, name, description, sku, price, and quantity fields must be provided.'}
			CODE	: 400 BAD_REQUEST
			
		4.  if sub_category_id, category_id, supplier_id, name, description, sku, price, and quantity field is passed in form data but value is Null.
		
			MESSAGE	: {'error': sub_category_id, category_id, supplier_id, name, description, sku, price, and quantity fields should not be Null.'}}
			CODE	: 400 BAD_REQUEST 


###2. GET Product:
    
    URL: /api/product
	
	METHOD: 
	    GET
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
    
    PARAMS:
        None
    
    RETURNS:
        returns all the result.
        
        [
            {
                "success": true
            },
            [
                {
                    "id": 3,
                    "images": [
                        {
                            "id": 1,
                            "image": "/media/image2",
                            "create_date": "2018-09-11T13:11:45.346000+05:30",
                            "last_update_date_time": "2018-09-11T13:11:45.346000+05:30",
                            "product": 2,
                            "create_by": 1,
                            "last_update_by": 1
                        },
                        {
                            "id": 2,
                            "image": "/media/image1",
                            "create_date": "2018-09-11T13:11:45.356000+05:30",
                            "last_update_date_time": "2018-09-11T13:11:45.356000+05:30",
                            "product": 2,
                            "create_by": 1,
                            "last_update_by": 1
                        },
                        {
                            "id": 3,
                            "image": "/media/product1.jpg",
                            "create_date": "2018-09-11T13:15:06.024000+05:30",
                            "last_update_date_time": "2018-09-11T13:15:06.024000+05:30",
                            "product": 3,
                            "create_by": 1,
                            "last_update_by": 1
                        },
                        {
                            "id": 4,
                            "image": "/media/myw3schoolsimage_1_V407fM0.jpg",
                            "create_date": "2018-09-11T13:15:06.034000+05:30",
                            "last_update_date_time": "2018-09-11T13:15:06.034000+05:30",
                            "product": 3,
                            "create_by": 1,
                            "last_update_by": 1
                        }
                    ],
                    "name": "iphone X",
                    "description": "Iphone X 32GB ROM 4GB RAM",
                    "sku": "iphonex-32-4-black-dec-2017",
                    "price": 79000,
                    "quantity": 5,
                    "is_active": true,
                    "create_date": "2018-09-11T13:15:06.019000+05:30",
                    "last_update_date_time": "2018-09-11T13:15:06.019000+05:30",
                    "category": 1,
                    "sub_category": 1,
                    "supplier": 1,
                    "create_by": 1,
                    "last_update_by": 1
                }
            ]
        ]


###3. DELETE Product:
    Delete product APIs will not delete the record from the database.
    Which is not good practice. so when the delete APIs are called it
    actually disabled the product. it set the flag is_active to False.
    
    
    URL: /api/product
	
	METHOD: 
	    GET
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
    
    PARAMS:
        product_id      (required)
    
    RETURNS:
        MESSAGE:
            {"success": "Product \"X\" has been disabled."}
            
        CODE: 200 OK
        
        NOTE: X in MESSAGE refer to product name.
    
    RAISES:
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST
			
		2.	if user is not superuser.
		
			MESSAGE	: {'error': 'You don\'t have permissions to delete product. Please contact administrator'}
			CODE	: 400 BAD_REQUEST
		
		3.	if product_id field is missing or not not provided in form data.
		
			MESSAGE	: {'error': "product_id fields must be provided.'}
			CODE	: 400 BAD_REQUEST
			
		4.  if product_id field is passed in form data but value is Null.
		
			MESSAGE	: {'error': product_id fields should not be Null.'}}
			CODE	: 400 BAD_REQUEST  

# Logout
    URL: /api/logout
	
	METHOD: 
	    GET
	
	HEADERS: 
	    "Authorization", "Token ee13837e01b58f7144e8872edae13d4a8dda54af" (Token which is recieved from the /api/login api.) 
    
    PARAMS:
        None
    
    RETURNS:
        MESSAGE:
            {'success': 'You are logged out successfully.'
            
        CODE: 200 OK
        
        NOTE: X in MESSAGE refer to product name.
    
    RAISES:
		1.	if user is not authenticated.
		
			MESSAGE	: {'error': 'User is not authenticated.'}
			CODE	: 400 BAD_REQUEST