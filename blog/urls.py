from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('blog', views.BlogViewSet, basename='blog')

blog_routers = routers.NestedDefaultRouter(router, 'blog', lookup='blog')
blog_routers.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = router.urls + blog_routers.urls