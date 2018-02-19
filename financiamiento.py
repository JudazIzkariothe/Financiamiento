# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _


class financiamiento_modelo(osv.osv):
	_name = 'financiamiento.modelo'
	_description = 'Financiamiento'
	_columns = {
        # Campo oblidatorio para buscar , readonly = True
       

       'nombre' : fields.char('Nombre:' ,size=35, type='text',required=True),
       'apellidop': fields.char('Apellido Paterno:', size=30, type='text',required=True),
       'apellidom': fields.char('Apellido Materno:', size=30, type='text',required=True),
       'rfc': fields.char('RFC:', size=13, type='text',required=True, help='RFC'),
       'colonia': fields.char('Colonia:', size=30, type='text',required=True),
       'domicilio': fields.char('Domicilio:', size=60, type='text',required=True),
       'estado': fields.char('Estado:', size=13, type='text',required=True),
       'municipio': fields.char('Municipio:', size=35, type='text',required=True),
       'localidad': fields.char('Localidad:', size=35, type='text',required=True),
       'cp': fields.integer('C.P.:', size=5, type='text',required=True),
       'telefono': fields.integer('Teléfono:', size=10, type='text'),
       'correo': fields.char('Correo:', size=35, type='text',required=True),
       'acreditacion_id': fields.many2one('acreditacion.modelo',string = 'Acreditacion:'),
       
      #'telefono': fields.integer('Teléfono', size=10, type='text'),
      #'correo': fields.char('E-Mail', size=35, type='text',required=True),              
      # 'sexo' : fields.selection((('1','Masculino'), ('2','Femenino')),'Sexo'),
      #'fecha': fields.date('Fecha de Nacimiento'),
      #'status' : fields.boolean('Status'),

	}
	_defaults = {
       		'active' : 'true',
	}


