import requests
import logging
import data
import json

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

def test_Add_new_course():

    try:
        api_url = "https://qwallity3.herokuapp.com/add_course/api"
        todo = data.data_post
        response = requests.post(api_url, json=todo)
        print(response.text)

        assert int(response.status_code) == 200
        print("The API post is passed")
    
    except Exception as e:
        logging.error(e)
        print("The request is failed")

    finally:
        json_response = json.loads(response.text)
        new_course_id = json_response["id"]
    
    return new_course_id

test_Add_new_course()
#Nel, that's what i need to see, return created course data and pass to next calls