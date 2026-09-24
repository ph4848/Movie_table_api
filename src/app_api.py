import requests

def insert_record(title, country, year, imdb_rate):
    url = "http://127.0.0.1:8000/insert/{title}/{country}/{year}/{imdb_rate}"

    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    else:
        return "Done!"
#----------------------------------------------
def select_all_records():
    url = "http://127.0.0.1:8000/select_all/"

    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    else:
        response = response.json()
        return response
#----------------------------------------------
def select_record_by_id(id):
    url = "http://127.0.0.1:8000/select_by_id/{id}"

    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    else:
        response = response.json()
        return response
#----------------------------------------------
def select_record_by_name(title):
    url = "http://127.0.0.1:8000/select_by_name/{title}"

    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    else:
        response = response.json()
        return response
#----------------------------------------------
def delete_record_by_id(id):
    url = "http://127.0.0.1:8000/delete_by_id/{id}"

    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    else:
        return "Done!"
#----------------------------------------------
def update_record_by_id(id, new_imdb_rate, new_year):
    url = "http://127.0.0.1:8000/update_by_id/{id}/{new_imdb_rate}/{new_year}"

    response = requests.get(url)
    if response.status_code != 200:
        return "ERROR"
    else:
        return "Done!"
#----------------------------------------------
if __name__ == "__main__":
    print(select_record_by_id(1))