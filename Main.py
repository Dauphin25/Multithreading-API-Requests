import requests
import threading
import json

#saving file name
file_name = 'My_Products'
#creating blank list for urls
urls = []
#creating blank list fro threads
threads = []

#clear all data in my json file if there is any from previous test
with open(file_name, 'w') as json_file:
    json_file.write('')

def get_product_data(url, product_file):
    try:
        #making get request to server
        response = requests.get(url)

        #checking if request is successful
        if response.status_code == 200:
            #making json content
            data = response.json()

            #converting data to single-line json format
            json_data = json.dumps(data)

            #writing data in json file
            with open(product_file, 'a') as json_file:
                json_file.write(json_data + '\n')
                print('data form {} is written in your file {}'.format(url, product_file))
        else:
            print('error geting data from {} , with status code {}'.format(url, response.status_code))

        pass

    except Exception as e:
        print('An error occurred: {}'.format(e))

#generating urls
for i in range(1,101):
    urls.append('https://dummyjson.com/products/{}'.format(i))

#creating threads for each url
for url in urls:
    thread = threading.Thread(target=get_product_data, args=(url, file_name))
    thread.start()
    threads.append(thread)

#joining threads to main thread
for thread in threads:
    thread.join()

print('all information saved in {}'.format(file_name))
