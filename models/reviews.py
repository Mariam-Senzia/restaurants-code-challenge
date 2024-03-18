from __init__ import CURSOR, CONN

class Review():
    def __init__(self,review_id, customer_id,customer_name, restaurant_id, review_text, star_rating):

        self.review_id = review_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.restaurant_id = restaurant_id
        self.review_text = review_text
        self.star_rating = star_rating

    def __repr__(self):
        return f"Review : review:{self.review_id}, customer:{self.customer_id} , customer_name:{self.customer_name}, restaurant{self.restaurant_id} ,{self.review_text} , {self.star_rating}" 


    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
              review_id INTEGER PRIMARY KEY AUTOINCREMENT,
              customer_id INTEGER,
              customer_name STRING,  
              name STRING,    
              review_text STRING,
              star_rating INTEGER, 
              FOREIGN KEY (customer_id) REFERENCES customers(customer_id)   , 
              FOREIGN KEY (name) REFERENCES restaurants(name)                  
            )
        """)
        CONN.commit()

    @classmethod
    def add_review(cls, customer_id,customer_name, name, review_text, star_rating):
        CURSOR.execute("""
            INSERT INTO reviews(customer_id,customer_name, name, review_text, star_rating)
            VALUES (? , ?, ?, ?,?)
        """, (customer_id, customer_name, name, review_text, star_rating)
        )
        CONN.commit()

    @classmethod
    def customer(cls, review_id):
        from customer import Customer
        CURSOR.execute("""
            SELECT * FROM customers
            INNER JOIN reviews ON customers.customer_id = reviews.customer_id
            WHERE reviews.review_id = ? 
        """, (review_id,))
        return CURSOR.fetchone()
    
    @classmethod
    def restaurant(cls,review_id):
        from restaurant import Restaurant
        CURSOR.execute("""
            SELECT * FROM restaurants
            INNER JOIN reviews ON restaurants.restaurant_id = reviews.restaurant_id
            WHERE reviews.review_id = ?
        """,(review_id,))
        return CURSOR.fetchone()
    
    @classmethod
    def full_review(cls,customer_id):
        CURSOR.execute("""
            SELECT name,customer_name,star_rating FROM reviews
            WHERE customer_id = ?  
        """,(customer_id,))
        return CURSOR.fetchall()
    # f"Review for {cls.name} by {insert customer's full name}: {cls.star_rating} stars."
    #return in provided format
        