from django.urls import path
# from .viewsets import todo_list, todo_detail_change_and_delete
# from .viewsets import TodoListAndCreate, TodoDetailChangeAndDelete
from .viewsets import TodoViewSet
from rest_framework.routers import DefaultRouter

""" urlpatterns = [
    # path('', todo_list),
    # path('<int:id>/', todo_detail_change_and_delete),
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view())
]
 """
 
router = DefaultRouter()
router.register('', TodoViewSet)
urlpatterns = router.urls
