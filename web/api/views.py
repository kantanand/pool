from django.shortcuts import render
from pool_app.models import *
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
def add_user(request):
	if request.method == 'POST':
		data = request.body
		errors = []

		pool_user_data = json.loads(data)
		user_id = pool_user_data['unique_id']
		age 	= pool_user_data['age']
		gender	= pool_user_data['gender']
		mobile_number = pool_user_data['mobile_number']
		location = pool_user_data['location']
		try:
			pool_user = PoolUsers(user_id=user_id,age=age,
							gender=gender,mobile=mobile_number,location=location)
			pool_user.save()
			return HttpResponse('Pool user Created')
		except IntegrityError, message:
			print "exceptions occured and error is "
			error_code = message[0]
			print error_code
			error = ''
			if error_code == 1062:
				error = "uniquie is already existing"
				print error
				errors.append(error)
			return HttpResponse('Pool user not created')

@csrf_exempt
def find_hashtag(request):
	if request.method == 'POST':
		data = request.body
		pool_data = json.loads(data)

		pool_tag = pool_data['hash_tag']
		try:
			pool_tag_details = PoolTagMaster.objects.get(pk = pool_tag)
			return HttpResponse("yes")
		except ObjectDoesNotExist:
			return HttpResponse("no")

@csrf_exempt
def search_question(request):
	if request.method == 'POST':
		data = request.body
		pool_data = json.loads(data)

		pool_tag = pool_data['hash_tag']
		details  = []
		try:
			pool_tag_details = PoolTagMaster.objects.get(pk=pool_tag)
			details.append({"pool_tag":pool_tag_details.pool_tag,
							"question":pool_tag_details.question,
							"option1":pool_tag_details.option1,
							"option2":pool_tag_details.option1,
							"option3":pool_tag_details.option1,
							"option4":pool_tag_details.option1,
							# "pool_start":pool_tag_details.pool_start,
							# "pool_end":pool_tag_details.pool_end
							})
			return HttpResponse(json.dumps(details), content_type="application/json")
		except ObjectDoesNotExist:
			return HttpResponse("no")

@csrf_exempt
def create_question(request):
	if request.method == 'POST':
		data = request.body

		question_details = json.loads(data)
		pool_tag = question_details['hash_tag']
		user_id  = question_details['unique_id']
		question = question_details['question']
		age      = question_details['age']
		gender   = question_details['gender']
		option1  = question_details['option1']
		option2  = question_details['option2']
		option3  = question_details['option3'] 
		option4  = question_details['option4']
		start_time = question_details['start_time']
		end_time = question_details['end_time']
		result_private = question_details['result_private']

		post_question = PoolTagMaster(pool_tag=pool_tag,question=question,
										option1=option1,option2=option2,
										option3=option3,option4=option4,
										age=age,gender=gender,
										user_id=user_id,pool_start=start_time,
										pool_end=end_time,
										option1_count=0,option2_count=0,
										option3_count=0,option4_count=0,
										)
		post_question.save()

		# return HttpResponse(json.dumps(response), content_type="application/json")
		return HttpResponse(pool_tag)

@csrf_exempt
def answer_this_question(request):
	if request.method == 'POST':
		data = request.body

		answer_details = json.loads(data)

		pool_tag = answer_details['hash_tag']
		option_selected = answer_details['option_selected']
		option_text = answer_details['option_text']
		user_id = answer_details['unique_id']
		age     = answer_details['age']
		gender  = answer_details['gender']
		try:
			post_answer = PoolTagAnswer(pool_tag_id=pool_tag,
										option_selected=option_selected,
										option_text=option_text,
										user_id=user_id,
										age=age,gender=gender)
			post_answer.save()

			pool_count = PoolTagMaster.objects.get(pk=pool_tag)
			if option_selected == 1:
				pool_count.option1_count = pool_count.option1_count+1
			if option_selected == 2:
				pool_count.option2_count = pool_count.option2_count+1
			if option_selected == 3:
				pool_count.option3_count = pool_count.option3_count+1
			if option_selected == 4:
				pool_count.option4_count = pool_count.option4_count+1
			pool_count.save()
			return HttpResponse("success")
		except:
			return HttpResponse("failure")

@csrf_exempt
def get_answers(request):
	if request.method == 'POST':
		data = request.body
		pool_data = json.loads(data)

		pool_tag = pool_data['hash_tag']
		pool_results = []
		try:
			pool_details = PoolTagMaster.objects.get(pk=pool_tag)
			pool_results.append({"pool_tag":pool_details.pool_tag,
									"option1":pool_details.option1,
									"option2":pool_details.option2,
									"option3":pool_details.option3,
									"option4":pool_details.option4,
									"option1_count":pool_details.option1_count,
									"option2_count":pool_details.option2_count,
									"option3_count":pool_details.option3_count,
									"option4_count":pool_details.option4_count
								})
			return HttpResponse(json.dumps(pool_results), content_type="application/json")
		except ObjectDoesNotExist:
			return HttpResponse("invalid_hash_tag")