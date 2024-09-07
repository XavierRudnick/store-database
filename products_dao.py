from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor() #MySQL cursor for executing querys
    query = ("SELECT Products.products_id,Products.name , Products.uom_id , Products.price_per_unit , uom.uom_name FROM Products inner join uom on Products.uom_id = uom.uom_id")
    cursor.execute(query)

    response = []
    for (product_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({
            'product_id':product_id,
            'name':name,
            'uom_id':uom_id,
            'price_per_unit':price_per_unit,
            'uom_name':uom_name
        })

    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO Products (name, uom_id, price_per_unit) VALUES (%s,%s,%s)")
    data = (product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid #return new products id number
    
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("delete from Products where products_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    
if __name__ == "__main__":
    connection = get_sql_connection()
    print(delete_product(connection,5))

    