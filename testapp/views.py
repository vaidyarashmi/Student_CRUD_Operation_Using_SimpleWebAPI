from testapp.import_statements import *
# Create your views here.

class student_CBV(HttpMixins,JSONDataMixins,IDMixins,View):
    def get(self,request,*args,**kwargs):
        data=request.body
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            stud=self.get_object_by_id(id=id)
            if stud is None:
                json_data=json.dumps({'msg':'Resource Not found'})
                return self.get_http_res(json_data,400)
            json_data=self.get_field_record([stud,])
            return self.get_http_res(json_data,200)
        qs=Student.objects.all()
        json_data=self.get_field_record(qs)
        return self.get_http_res(json_data,200)
    
    def delete(self,request,*args,**kwargs):
        data=request.body
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:           
            stud=self.get_object_by_id(id)
            if stud is None:
                json_data=json.dumps({'msg':'NO matched records found'})
                return self.get_http_res(json_data,404)
            status,deleted_item = stud.delete()
            if status == 1:
                json_data=json.dumps({'msg':'Deleted Sucessfully'})
                return self.get_http_res(json_data,200)
            json_data=json.dumps({'msg':'Unable to perform delete operation'})
            return self.get_http_res(json_data,400)
        json_data=json.dumps({'msg':'Please enter valid id'})
        return self.get_http_res(json_data,404)

    def post(self,request,*args,**kwargs):
        data=request.body
        stud=json.loads(data)
        form=StudentForm(stud)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Created Sucessfully'})
            return self.get_http_res(json_data,200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.get_http_res(json_data,400)
        
    def put(self,request,*args,**kwargs):
        data=request.body
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform updation id is mandatory. Please provide id'})
            return self.get_http_res(json_data,400)
        stud=self.get_object_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'No matched records found'})
            return self.get_http_res(json_data,400)
        provided_data=json.loads(data)
        original_data={
            'roll_no':stud.roll_no,
            'name':stud.name,
            'marks':stud.marks
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=stud)
        if form.is_valid():
            form.save(commit=True)      
            json_data=json.dumps({'msg':'Updated Sucessfully'})
            return self.get_http_res(json_data,200)  
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.get_http_res(json_data,400)
    