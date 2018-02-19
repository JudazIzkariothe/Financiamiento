# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _


class acreditacion_modelo(osv.osv):
	_name = 'acreditacion.modelo'
	_description = 'Acreditacion'
	_rec_name = 'acreditacion'
	_columns = {
        # Campo oblidatorio para buscar , readonly = True
       'esquema_id': fields.many2one('esquema.modelo',string = 'Esquema:'),
       'acreditacion': fields.char('Acreditacion:', size=30, type='text',required=True),
       'monto': fields.float('Monto:', size=30, type='text',required=True),
       'plazo' : fields.selection((('1','0'), ('2','6'),('3','12'),('4','24'), ('5','36'),('6','48')),'Plazo:'),
       'periodog': fields.integer('Periodo de Ganancia:', size=30, type='text',required=True),
       'tazao': fields.float('Tasa Ordianaria:', size=13, type='text',required=True),
       'tipog': fields.char('Tipo de Garantia:', size=30, type='text',required=True),
	}
	_defaults = {
       		'active' : 'true',
	}

class esquema_modelo(osv.osv):
      _name = 'esquema.modelo'
      _description = 'Esquema'
      _rec_name = 'esqnombre' 
      _columns = {
        # Campo oblidatorio para buscar , readonly = True
       'esqnombre' : fields.char('Nombre:' ,size=35, type='text',required=True),
       'montomin': fields.integer('Monto Minimo:', max_size=5, type='text',required=True),
       'montomax': fields.integer('Monto Maximo:', max_size=30, type='text',required=True),
       'fechaini': fields.date('Fecha Inicio:'),
       'fechafin': fields.date('Fecha Fin:'),
       'status' : fields.boolean('Status:'),

      }
      _defaults = {
                  'active' : 'true',
      }

