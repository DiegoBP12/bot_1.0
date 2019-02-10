# -*- coding:utf-8 -*-
import web
import application.models.model_robin as model_robin # importa el model de personas
render = web.template.render('application/views/robin/', base='master') # configura la ubicación de las vistas