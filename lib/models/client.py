from models.config import CONN, CURSOR
import ipdb

class Client:

    def __init__(self, name, type, contact_info,id=None):
        self.name= name
        self.type= type
        self.contact_info= contact_info
        self.id = id 

    def __repr__(self):
        return f"Client(name={self.name},type={self.type},contact_info={self.contact_info})" 
    
    @classmethod
    def from_db(cls, row):
        client_instance= Client(row[1], row[2], row[3])
        client_instance.id= row[0]
        return client_instance

    @classmethod
    def create_table(cls):
        sql= """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            type TEXT,
            contact_info TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
        INSERT INTO clients (name, type, contact_info) VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type, self.contact_info))
        CONN.commit()
        self.id= CURSOR.lastrowid

    @classmethod
    def create(cls, name, type, contact_info):
        client= cls(name, type, contact_info)
        client.save()
        return client 
    
    @classmethod
    def delete(cls, client_id):
        sql= "DELETE FROM clients WHERE id = ?"
        CURSOR.execute(sql,(client_id,))
        CONN.commit()

    @classmethod
    def find_by_name(cls,name):
        query = "SELECT * FROM clients WHERE name is ?"
        result = CURSOR.execute(query,(name,)).fetchone()
        if result:
            
            return (result)
        else:
            return None
    
    @classmethod
    def display_all_clients(cls):
        rows = CURSOR.execute("SELECT * FROM clients" ).fetchall()
        

        if len(rows) == 0:
            print("no clients found")
        else:
            print("Clients:")
            for row in rows:
                print(row)    

    @classmethod
    def view_by_type(cls,type):  
        rows = CURSOR.execute("SELECT * FROM clients WHERE type is ?", (type,)).fetchall()
        return [cls.from_db(row) for row in rows] 
    
    @classmethod
    def drop_table(cls):
        sql= "DROP TABLE clients;"
        CURSOR.execute(sql)
        CONN.commit() 

    @classmethod
    def find_by_id(cls, id):
        sql= "SELECT * FROM clients WHERE id= ?"
        row= CURSOR.execute(sql, (id,)).fetchone()
        return cls.from_db(row)

    
    


