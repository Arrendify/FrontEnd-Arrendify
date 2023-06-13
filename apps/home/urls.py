# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    #inquilinos
    path('', views.index, name='home'),    
    path('inquilinos/', views.path_inq, name='inquilinos'),    
    path('detalles_inquilino/<int:id>', views.path_inq_detalles, name='inquilinos_detalles'),    
    path('editar_inq/<int:id>', views.path_inq_edit, name='inquilinos_editar'),    
    path('documentos_inq/<int:id>', views.path_archivos_inq, name='archivos_inquilinos'),    
    path('detalles_documentos/<int:id>', views.path_detalles_archivos, name='detalles_archivos'),    
    #inmuebles
    path('inmuebles/', views.path_inmuebles, name='inmuebles'),  
    #fiador 
    path('fiador_obligado/', views.path_foo, name='fiador_obligado'),   
    path('detalles_fiador/<str:slug>', views.path_foo_detalles, name='inquilinos_detalles'),    
    path('editar_fiador/<str:slug>', views.path_foo_edit, name='inquilinos_editar'),
    path('documentos_fia/<int:id>', views.path_archivos_fia, name='archivos_fiador'),    
    path('det_documentos/<int:id>', views.path_detalles_archivos_fia, name='detalles_archivos_fiador'),
    path('tyc/', views.tyc, name='tyc'),  
    #inquilinos
    path('investigacion/', views.path_investigacion, name='investigacion'),
    path('checklist_investigacion/', views.path_check_investigacion, name='check_investigacion'),
    
    #otros  
    path('prueba/', views.prueba, name='Arren'),  
    
    path('archivos', views.path_doc_inquilino, name='inquilinos_docs'),  


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
