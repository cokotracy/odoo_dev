# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _


class StockChecklist(models.Model):
    _name = 'stock.checklist'
    _description = 'Checklist de recibo'
    _rec_name = 'nro_doc'

    nro_doc = fields.Char('Nro. Documento')
    type = fields.Char('Tipo')
    phase = fields.Char('Fase')
    document_owner = fields.Char('Dueño del documento') # Check field
    title = fields.Char('Título')
    nro_revision = fields.Integer('Nro. Revisión')
    date_published = fields.Date('Fecha Publicación')
    classification = fields.Char('Clasificación')
    date = fields.Date('Fecha')
    nro_container = fields.Char('Nro. Contenedor')
    dua_match = fields.Boolean('Revisión documental, ¿el número de contenedor coincide con el DUA?')
    nro_label_truck = fields.Boolean('¿El número de marchamo del camión coincide con la documentación?')
    label_integrity = fields.Boolean('¿El marchamo se encuentra íntegro (no está roto y la numeración es legible)?')
    termokin_condition = fields.Boolean('¿El transporte cuenta con un termokin en buen estado?')
    temperature_value = fields.Float('En caso de que el transporte sea de temperatura controlada, anotar el valor')
    container_closed = fields.Boolean('¿El contenedor se encuentra cerrado (no hay huecos en techo, piso, paredes, etc)?')
    strange_odors = fields.Boolean('¿Libre de olores extraños (detergente, pintura, cloro, insecticidas, entre otros)?')
    dust_mist = fields.Boolean('¿Hay polvos suspendidos o neblinas?')
    spill_hole = fields.Boolean('¿Hay derrames de ingredientes, pozos de agua o algún otro material?')
    cleanliness_acceptable = fields.Boolean('¿La limpieza general es aceptable (sin polvo, suciedad, plagas, escombros)?')
    load_mixed = fields.Boolean('¿La carga no viene mezclada con materiales que no sean compatibles con materiales de consumo humano (plaguicidas, detergentes, medicinas, químicos)?')
    clean_dust_debris = fields.Boolean('¿El material se encuentra limpio, libre de polvo, escombros, entre otros?')
    odor_leaking_contaminated = fields.Boolean('¿El material presenta olores extraños que sugieran que está fugando o que está contaminado?')
    pallet_condition = fields.Boolean('¿Las tarimas están en buenas condiciones, libres de moho, focos de contaminación visible, malos olores, clavos o tornillos expuestos, piezas quebradas o astilladas, entre otros?')
    sack_bag_drum_leaking = fields.Boolean('¿Los tambores, sacos, bolsas u otro material de empaque primario/secundario que contenga el producto está perforado, fugando o deformado?')
    material_supplier_id = fields.Boolean('¿El material cuenta con identificación del proveedor, el cual, incluye como mínimo lote, tipo de material y nombre del proveedor?')
    label_info = fields.Boolean('¿La información de la etiqueta del material es legible?')
    security_mechanism = fields.Boolean('¿Los materiales tienen sellos, cintas u otros mecanismos de seguridad, y este se encuentra íntegro e identificado por la casa de manufactura?')
    temperature_material = fields.Boolean('¿La temperatura está de acuerdo al tipo de material, sin humedad excesiva que dañe la materia prima, material de empaque, entre otros?')
    responsible = fields.Char('Responsable') # Check field

