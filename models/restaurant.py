from __init__ import CURSOR, CONN

class Restaurant():
    def __init__(self, restaurant_id, name, price):
        self.restaurant_id = restaurant_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Restaurant : {self.name} , {self.price}" 


    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS restaurants (
              restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name STRING,
              price INTEGER              
            )
        """)
        CONN.commit()

    @classmethod
    def add_restaurant(cls, name, price):
        CURSOR.execute("""
            INSERT INTO restaurants(name, price)
            VALUES (? , ?)
        """, (name,price)
        )
        CONN.commit()
        
    @classmethod
    def reviews(cls,restaurant_id):
        from reviews import Review
        CURSOR.execute("""
            SELECT review_id,review_text,star_rating FROM reviews
            WHERE restaurant_id = ?
        """,(restaurant_id,))
        return  CURSOR.fetchall()
    
    
    @classmethod
    def customer(cls,restaurant_id):
        from reviews import Review
        CURSOR.execute("""
            SELECT customer_id FROM reviews
            WHERE restaurant_id = ?  
        """,(restaurant_id,))
        return CURSOR.fetchall()

    
    @classmethod
    def fanciest(cls):
        CURSOR.execute("""
            SELECT name,price FROM restaurants  
            ORDER BY price DESC  
            LIMIT 1           
        """,)
        return CURSOR.fetchall()
    
    @classmethod
    def all_reviews(cls,review_id):
        from reviews import Review
        CURSOR.execute("""
            SELECT * FROM reviews 
            WHERE review_id = ?
        """,(review_id,))
        return CURSOR.fetchall() 
