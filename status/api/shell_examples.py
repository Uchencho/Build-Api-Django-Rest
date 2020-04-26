from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

'''
Serialize a single object
'''
obj = Status.objects.first()
serializer = StatusSerializer(obj)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

#Second method
stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


'''
Serialize a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)

'''
create obj
'''
data = {'user':1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save() #Need to call is valid before saving


'''
update obj
'''
obj = Status.objects.first() #How to get the specific object
data = {'content': 'some new content', 'user': 1}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()


'''
Delete obj
'''
data = {'user':1, 'content':'Please delete me'}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
#data = {'id':create_obj.id}

obj = Status.objects.last()
obj.delete()