# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 B-Informed (<http://www.b-informed.nl>).
#    Author: Roel Adriaans
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Alter robots.txt disallow indexing',
    'summary': 'Disables robots.txt for indexing by webcrawlers like Google',
    'license': 'AGPL-3',
    'version': '8.0.1.0.0',
    'author': "B-Informed B.V.,Odoo Community Association (OCA)",
    'category': 'Website',
    'depends': [
        'website',
    ],
    'data': [
        'views/disable_robots.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
}
