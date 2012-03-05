from taller.models import Reparacion, ReparacionForm
from django.views.generic.create_update import create_object, update_object, delete_object

def create(request):
	return create_object(request,
        form_class=ReparacionForm,
        template_name='common/detail.html',
        post_save_redirect="/taller"
    )

def update(request, id):
	return update_object(request,
        form_class=ReparacionForm,
        object_id=id,
        template_name='common/detail.html',
        post_save_redirect="/taller"
    )      

def delete(request, id):
	return delete_object(request,
        model=Reparacion,
        object_id=id,
        template_name='common/delete.html',
        template_object_name='object',
        post_delete_redirect="/taller"
    )    