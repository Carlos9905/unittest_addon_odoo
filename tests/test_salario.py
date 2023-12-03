from odoo import Command
from odoo.tests import tagged, Form, common
import logging
_logger = logging.getLogger(__name__)

@tagged('post_install', '-at_install')
class TestSalario(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestSalario, cls).setUpClass()
        cls.empleado_obj = cls.env['model.prueba']

        cls.juan = cls.empleado_obj.create(dict(name="Juan", horas=8, salario=15))
        cls.pedro = cls.empleado_obj.create(dict(name="Pedro", horas=8, salario=8))
        cls.maria = cls.empleado_obj.create(dict(name="Maria", horas=10, salario=10))
    
    def test_salario(self):
        self.assertEqual(self.juan.total, 120)#
        self.assertEqual(self.pedro.total, 64)
        self.assertEqual(self.maria.total, 100)