# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  Leonardo Bozzi  (http://www.vangrow.ar)
#    All Rights Reserved.
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
# -----------------------------------------------------------------------------------
{
    "name": "Sale Documents Integration",
    "summary": "This module allows to save attachments of a sale order "
    "to a particular folder of Documents.",
    "version": "15.0.1.0.0",
    "category": "Documents",
    "author": "Leonardo Bozzi",
    "license": "Other OSI approved licence",
    "depends": [
        "sale_management",
        "documents",
    ],
    "data": [
        "data/document_data.xml",
        "views/res_config_settings_view.xml",
        "views/sale_order_views.xml",
    ],
    "images": ["images/sale_documents_integration.gif"],
    "installable": True,
    "auto_install": False,
}
