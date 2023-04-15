import requests
import logging
import data
import test_Add_new_course

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)
update_course_id = test_Add_new_course.test_Add_new_course()
print(update_course_id)
def test_Update_already_exists_course():

    try:
        api_url = f"https://qwallity2.herokuapp.com/course/{update_course_id}/update"
        todo = data.data_put
        response = requests.put(api_url, json=todo)
        print(response.text)

        assert int(response.status_code) == 200
        print("The API put is passed")
    
    except Exception as e:
        logging.error(e)
        print("The request is failed")

test_Update_already_exists_course()
#Nel, correct

#Greate job, you imagine the whole structure correctly