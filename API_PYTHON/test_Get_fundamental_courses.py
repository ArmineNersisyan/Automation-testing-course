import requests
import logging

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

def test_Get_fundamental_courses():

    try:
        api_url = "https://qwallity2.herokuapp.com/courses/fundamental/api"
        response = requests.get(api_url)
        print(response.text)

        assert int(response.status_code) == 200
        print("The API get is passed")
    
    except Exception as e:
        logging.error(e)
        print("The request is failed")

test_Get_fundamental_courses()
#Nel, correct