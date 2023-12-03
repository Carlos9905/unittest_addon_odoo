from odoo import fields, models, api

class Modelo(models.Model):
    _name = 'model.prueba'
    _description = 'Modelo de prueba'

    name = fields.Char(string='Nombre', default="Nuevo")
    horas = fields.Float("Horas trabajadas")
    salario = fields.Float("Salario por hora")
    total = fields.Float("Salario total", compute="_calcula_total")
    bono = fields.Boolean("Bono")

    @api.depends('salario', 'horas')
    def _calcula_total(self):
        for record in self:
            record.total = record.salario * record.horas
    
    def boton_bono(self):
        for record in self:
            record.total = record.total + 2000