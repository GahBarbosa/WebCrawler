import psycopg2
config = "dbname= user= password= host="
def update(productId,price,last_update):
  conn = psycopg2.connect(config)
  cur = conn.cursor()

  cur.execute("""
      INSERT INTO product_data (product_id,sales,price, invoice)
      VALUES (%(id)s, 0, %(price)s, 0)
      ON CONFLICT (product_id,day)
      DO UPDATE SET
      sales = product_data.sales + 1,
      price = %(price)s,
      invoice = product_data.invoice + %(price)s,
      last_update = now()
      WHERE
        product_data.product_id = %(id)s AND
        product_data.day = current_date
        AND product_data.last_update < %(last_update)s;
      """,({'id': productId, 'price': price, 'last_update': last_update}))

  conn.commit()
  cur.close()
  conn.close()

def getProducts(storeId):
  conn = psycopg2.connect(config)
  cur = conn.cursor()
  cur.execute("SELECT id,url FROM product_info WHERE store_id = %s ORDER BY id",[storeId])
  res = cur.fetchall()
  cur.close()
  conn.close()
  return res