from __init__ import CURSOR, CONN

class Customer():
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    @property
    def customer_name(self):
        return self.first_name + " " + self.last_name
    
    @customer_name.setter
    def customer_name(self, first_name, last_name):
        self._customer_name = first_name + last_name

    def __repr__(self):
        return f"Customer {self.customer_id}: {self.first_name} {self.last_name}" 


    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS customers (
              customer_id INTEGER PRIMARY KEY,
              first_name STRING,
              last_name STRING               
            )
        """)
        CONN.commit()


    @classmethod
    def add_customer(cls, first_name, last_name):
        CURSOR.execute("""
            INSERT INTO customers(first_name, last_name)
            VALUES (? , ?)
        """, (first_name,last_name))
        CONN.commit()

    
    @classmethod
    def customer_reviews(cls,customer_id):
        from reviews import Review
        CURSOR.execute("""
            SELECT * FROM reviews
            WHERE customer_id = ?  
        """,(customer_id,))
        return CURSOR.fetchall()
    
    @classmethod
    def restaurant(cls,customer_id):
        from reviews import Review
        CURSOR.execute("""
            SELECT restaurant_id FROM reviews
            WHERE customer_id = ?  
        """,(customer_id,))
        return CURSOR.fetchall()
    

    @classmethod
    def favourite_restaurant(cls,customer_id):
        from reviews import Review
        CURSOR.execute("""
            SELECT name,star_rating FROM reviews
            WHERE customer_id = ?  
            ORDER BY star_rating DESC  
            LIMIT 1            
        """,(customer_id,))
        return CURSOR.fetchall()
    
    @classmethod
    def add_review(cls,review_id, customer_id, name, review_text, star_rating):
        CURSOR.execute("""
            INSERT INTO reviews (review_id, customer_id, name, review_text, star_rating )
            VALUES (?,?,?,?,?)
        """,(review_id, customer_id, name, review_text, star_rating))
        CONN.commit()

        return (review_id, customer_id, name, review_text, star_rating)
    
    @classmethod
    def delete_review(cls,review_id):
        CURSOR.execute("""
            DELETE FROM reviews
            WHERE review_id = ?
        """,(review_id,))
        CONN.commit()

        return (review_id)
    