from django.shrotcuts import render
from todolist.models import List

def index(request):
    if request.method == 'POST':
        for key in request.POST.keys():
            if key == 'newtast' and request.POST.get('newtast'):
                p = List(tast=request.POST['newtast'])
                p.save()
            elif key.startswith('delete'):
                delete_id = key[len('delete'):]
                p = List.objects.get(id=delete_id)
                p.delete()
    task_list = List.object.all
    context = {'task_list':task_list}
    return render(request,'index.html',context)
