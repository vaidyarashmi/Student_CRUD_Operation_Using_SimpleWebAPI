import requests
import json
BASE_URL='http://127.0.0.1:8000/'
END_URL='api/'

# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+END_URL,data=json.dumps(data))
#     print(resp.json())
#     print(resp.status_code)
# get_resource()

# def delete_resource(id=None):
#     data={
#         'id':id
#     }
#     resp=requests.delete(BASE_URL+END_URL,data=json.dumps(data))
#     print(resp.json())
#     print(resp.status_code)
# delete_resource()

# def create_resource():
#     new_student={
#         'roll_no':557,
#         'name':'Shivraj',
#         'marks':70.00
#     }
#     resp=requests.post(BASE_URL+END_URL,data=json.dumps(new_student))
#     print(resp.json())
#     print(resp.status_code)
# create_resource()

# def update_resource(id=None):
#     new_student={
#         'id':id,
#         'name':'Shivraj',
#         'marks':70000
#     }
#     resp=requests.put(BASE_URL+END_URL,data=json.dumps(new_student))
#     print(resp.json())
#     print(resp.status_code)
# update_resource(12)
