# Restaurant Review System
### Overview
  This project implements a simple Restaurant Review System using Python and SQLite3. The system manages relationships between Restaurants, Customers, and Reviews. A Restaurant can have multiple Reviews from different Customers, and a Customer can leave multiple Reviews for different Restaurants.

# Table Relationships
- Restaurant: Has many Reviews.
- Customer: Has many Reviews.
- Review: Belongs to both a Restaurant and a Customer.

# Topics Covered
- Table Relationships: Establishing relationships between Restaurant, Customer, and Review tables.
- Class and Instance Methods: Implementing methods within classes to manage data and relationships.
- Database Querying: Executing queries to interact with the SQLite database.
- SQLite3 and the Cursor Object: Utilizing SQLite3 for database management and Cursor object for executing SQL queries.

# Instructions
- Setup: Create necessary tables including restaurants, customers, and reviews.
- Object Relationship Methods: Implement methods to manage relationships between objects (Restaurant, Customer, Review).
- Aggregate and Relationship Methods: Implement aggregate methods to retrieve aggregated data and manage relationships.

# Deliverables
# Database
- Establish necessary tables including restaurants, customers, and reviews.
- Ensure the reviews table has columns to establish relationships and store review information (e.g., restaurant_id, customer_id, star_rating).

# Object Relationship Methods
### Review
- customer(): Returns the Customer instance for this review.
- restaurant(): Returns the Restaurant instance for this review.

### Restaurant
- reviews(): Returns all reviews for the Restaurant.
- customers(): Returns all customers who reviewed the Restaurant.

### Customer
- reviews(): Returns all reviews left by the Customer.
- restaurants(): Returns all restaurants reviewed by the Customer.

# Aggregate and Relationship Methods
### Customer
- full_name(): Returns the full name of the customer.
- favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
- add_review(restaurant, rating): Adds a new review for the given restaurant with the specified rating.
- delete_reviews(restaurant): Deletes all reviews for the specified restaurant.

### Review
- full_review(): Returns a formatted string representing the review.

### Restaurant (Class Method)
- fanciest(): Returns the restaurant instance with the highest price.
- all_reviews(): Returns a list of formatted strings containing all reviews for the restaurant.

# Usage
- Create instances of Restaurants, Customers, and Reviews.
- Test the implemented methods to ensure proper functionality.
- Use main.py to create sample data and test your models and relationships.