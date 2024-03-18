from __init__ import CONN, CURSOR
from customer import Customer
from restaurant import Restaurant
from reviews import Review


def my_databse():
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

    Customer.add_customer("Senzia","Mariee")
    Customer.add_customer("Maria","Goretti")
    Customer.add_customer("Brian","Kiprono")


    Restaurant.add_restaurant("Hemingways Karen", 80000 )
    Restaurant.add_restaurant("Four points by Sheraton", 50000 )
    Restaurant.add_restaurant("Onza", 20000 )


    Review.add_review(1,'Senzia Mariee','Hemingways Karen', "Excellent food and service", 5)
    Review.add_review(2,'Maria Goretti','Four points by Sheraton', "Great value for money!", 4.5)
    Review.add_review(3,'Brian Kiprono', 'Onza', "Ambiance 10/10", 4.5),
    Review.add_review(1,'Senzia Mariee','Onza', "Aesthetically pleasing",4)

    #customer instance
    # customer_instance = Review.customer(3)
    # print("******customer instance******")
    # print(customer_instance)
    #restaurant
    # restaurant_instance = Review.restaurant(1)
    # print("******restaurant instance******")
    # print(restaurant_instance)

    #restaurant reviews
    # restaurant_reviews = Restaurant.reviews(3)
    # print("******all restaurant reviews******")
    # print(restaurant_reviews)
    # #customer
    # customer = Restaurant.customer(3)
    # print("******customers who reviewed restaurant******")
    # print(customer)


    #customer reviews
    # customer_reviews = Customer.customer_reviews(1)
    # print("******  all reviews left by customer  ******")
    # print(customer_reviews)
    # restaurant reviewed
    #collection of restaurants
    # restaurant = Customer.restaurant(1)
    # print("******customers who reviewed restaurant******")
    # print(restaurant)


    #full name
    # full_name = Customer.full_name()
    # print(full_name)

    #returns customers
    # customer1 = Customer(1, "Amad", "Dialo")
    # print(customer1.customer_name)

    #favourite restaurant
    # print(Customer.favourite_restaurant(1))


    #Add restaurant
    # new_restaurant1 = Customer.add_review(5, 3, "Inti", "Best sushi in town!!",4.2)
    # new_restaurant2 = Customer.add_review(6, 3, "Smokys", "Worst wing ever!!!!!!", 1.2)

    # print(new_restaurant1,new_restaurant2)

    #delete review
    # print(Customer.delete_review(6))

    #full review
    # print(Review.full_review(3))

    #fanciest restaurant
    # print(Restaurant.fanciest())

    #list of strings
    print(Restaurant.all_reviews(1))


my_databse()