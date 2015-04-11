from django.test import TestCase

# Create your tests here.
# Testing for getting answers
curl -H "Content-Type: application/json" -X POST -d '{"hash_tag":"xyz"}' http://localhost:8000/api/get_answers

# Testing for creating users
curl -H "Content-Type: application/json" -X POST -d '{"unique_id":"9591046096","age":25,"gender":"Male","mobile_number":"9591046096","location":"bangalore"}' http://localhost:8000/api/add_user/

# finding hash_tag 
curl -H "Content-Type: application/json" -X POST -d '{"hash_tag":"9591046096"}' http://localhost:8000/api/find_hashtag/

# geting question detail
curl -H "Content-Type: application/json" -X POST -d '{"hash_tag":"9591046096"}' http://localhost:8000/api/search_question/

# creating a question
curl -H "Content-Type: application/json" -X POST -d '{"hash_tag":"#1","question":"What is my full name","unique_id":"9591046096","age":25,"gender":"Male","option1":"Nitesh","option2":"Parimala Nitesh","option3":"M Parimala Nitesh","option4":"MVP Nitesh","start_time":"2015-04-11","end_time":"2020-04-10","result_private":"no"}' http://localhost:8000/api/create_question/

# answering the question
curl -H "Content-Type: application/json" -X POST -d '{"hash_tag":"#1","option_selected":4,"option_text":"MVP Nitesh","unique_id":"9591046096","age":25,"gender":"Male"}' http://localhost:8000/api/answer_this_question/

# getting answers 
curl -H "Content-Type: application/json" -X POST -d '{"hash_tag":"#1"}' http://localhost:8000/api/get_answers/