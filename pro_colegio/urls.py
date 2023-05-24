from django.urls import path, include
from django.contrib import admin
from colegio import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('', include('render.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    path('gestion_cursos/', views.CursoListView.as_view(), name='gestion_cursos'),
    path('registrarCurso/', views.registrar_curso, name='registrar_curso'),
    path('eliminacionCurso/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    path('edicionCurso/<int:id>/', views.edicion_curso, name='edicion_curso'),
    path('editarCurso/', views.editar_curso, name='editar_curso'),

    path('gestion_alumnos/', views.AlumnoListView.as_view(), name='gestion_alumnos'),
    path('registrarAlumno/', views.registrar_alumno, name='registrar_alumno'),
    path('eliminacionAlumno/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('edicionAlumno/<int:id>/', views.edicion_alumno, name='edicion_alumno'),
    path('editarAlumno/', views.editar_alumno, name='editar_alumno'),
]
