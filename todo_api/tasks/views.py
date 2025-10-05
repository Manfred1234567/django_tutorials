from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from .models import Task
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET' : 'api/tasks/'},
        {'POST' : 'api/tasks/'},
        {'PUT' : 'api/tasks/<id>/'},
        {'DELETE' : 'api/tasks/<id>/'},
    ]
    return Response(routes)

#Get all tasks
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({
        "count" : tasks.count(),
        "data" : serializer.data #Return serialized data
    }, status=status.HTTP_200_OK)


#Create a task
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
        {"message" : "Created succesfully","data":serializer.data}
        , status=status.HTTP_201_CREATED
        )
    return Response({
        "message" : "Task creation failed.",
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

#Update task
@api_view(['PUT'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message" : "Task updated succesfully!",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response({
        "message" : "Failed to update task.",
        "error" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
            


#Delete Task
@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response(
        {'message' : 'Task was deleted successfully!!'},status=status.HTTP_200_OK
    )