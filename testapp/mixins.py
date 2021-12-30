from testapp.import_statements import *
class IDMixins(object):
    def get_object_by_id(self,id):
        try:
            stud=Student.objects.get(id=id)
        except:
            stud=None
        return stud
class HttpMixins(object):
    def get_http_res(self,json_data,status_code):
        return HttpResponse(json_data,content_type='application/json',status=status_code)
class JSONDataMixins(object):
    def get_field_record(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        final_list=[]
        for obj in p_data:
            emp_data=obj['fields']
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data