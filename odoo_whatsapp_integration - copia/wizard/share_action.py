import urllib.parse as urllib
from odoo import models, fields, api

class ShareAction(models.TransientModel):
    _inherit = 'portal.share'

    def get_name(self):
        module = self.env['ir.module.module'].search([('name', '=', 'odoo_whatsapp_integration')])
        module_installed = True if module and module.state == 'installed' else False
        if module_installed:
            if self.env[self._context.get('active_model')]._name == 'sale.order':
                rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
                return rec.partner_id.name
            elif self.env[self._context.get('active_model')]._name == 'purchase.order':
                rec = self.env['purchase.order'].browse(self.env.context.get('active_id'))
                return rec.partner_id.name
            elif self.env[self._context.get('active_model')]._name == 'account.move':
                rec = self.env['account.move'].browse(self.env.context.get('active_id'))
                return rec.partner_id.name

    share_type = fields.Selection([
        ('mail', 'Mail'),
        ('whatsapp', 'Whatsapp')], string="Compartir", default="mail")
    partner_id = fields.Char(string='Partner',default=get_name)
    mobile_number = fields.Char(string='Número telefónico')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.mobile_number = self.env[self._context.get('active_model')].browse(self.env.context.get('active_id')).partner_id.mobile

    def action_send_whatsapp(self):
        if self.note and self.mobile_number:
            if self.res_model == 'sale.order':
                common_message = 'Acceso a la orden de venta.'
            elif self.res_model == 'account.move':
                common_message = 'Acceso a la factura.'
            elif self.res_model == 'purchase.order':
                common_message = 'Acceso a la orden de compra.'
            else:
                common_message = 'Puedes acceder al siguiente Documento.'
            message_string = self.note + '%0a' + common_message + '%0a''%0a' + urllib.quote(self.share_link)
            related_record = self.env[self.res_model].search([('id', '=', int(self.res_id))])
            related_record.message_post(body=message_string)
            link = "https://api.whatsapp.com/send/?phone=" + self.mobile_number #Cambiado link
            return {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }