import requests
import logging
import test_Add_new_course

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)
delete_course_id = test_Add_new_course.test_Add_new_course()
print(delete_course_id)
def test_Delete_course():

    try:
        api_url = f"https://qwallity2.herokuapp.com/courses/course/{delete_course_id}"
        response = requests.delete(api_url)
        print(response.text)

        assert int(response.status_code) == 200
        print("The API delete is passed")
    
    except Exception as e:
        logging.error(e)
        print("The request is failed")

test_Delete_course()
#Nel, correct