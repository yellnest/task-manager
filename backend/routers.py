from rest_framework import routers

from todo.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TodoViewSet)

urlpatterns = router.urls
