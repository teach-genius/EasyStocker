from django.urls import path
from .views import view_home,add_mouvement_view, product_view, move_view,view_delete, vente_view, warning_view, add_product_view,view_detail
from gestionstock import settings
from django.conf.urls.static import static
app_name = "easygestion"  # Ajout du namespace

urlpatterns = [
    path("", view_home, name="home"),
    path("product/", product_view, name="product"),
    path("productview/<slug:slug>/", view_detail, name="productview"),
    path("delete/<slug:slug>/", view_delete, name="delete"),
    path("move/", move_view, name="move"),
    path("vente/", vente_view, name="vente"),
    path("warning/", warning_view, name="warning"),
    path("add_product/", add_product_view, name="add_product"),
    path("add_mouvement/", add_mouvement_view, name="add_mouvement"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
