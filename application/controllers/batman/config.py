# -*- coding:utf-8 -*-
import web
import application.models.model_batman as model_batman # importa el model de batman
render = web.template.render('application/views/batman/', base='master') # configura la ubicación de las vistas