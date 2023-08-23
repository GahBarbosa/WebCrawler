import product
import urllib.request, json 
import timeit

startT = timeit.default_timer()
res = product.getProducts(2)

for row in res:
    start = timeit.default_timer()

    url = row[1] +".json"
    with urllib.request.urlopen(url) as productJson:
        data = json.load(productJson)
        last_update = data['product']['updated_at']
        price = data['product']['variants'][0]['price']
    product.update(row[0],price,last_update)
    stop = timeit.default_timer()
    print(row[0], row[1]," was Successful updated Time: ", stop - start)

stopT = timeit.default_timer()
print('Total items: ',len(res),' Time: ', stopT - startT)  