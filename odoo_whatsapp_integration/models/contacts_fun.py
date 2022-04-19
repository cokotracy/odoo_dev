from odoo import models, fields, api, _

class SaleOrderValidation(models.Model):
    _inherit = 'res.partner'

    def contact_whatsapp(self):
        record_phone = self.mobile
        if not record_phone[0] == "+":
            view = self.env.ref('odoo_whatsapp_integration.warn_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            # Traducido
            context['message'] = "No tiene código de país! Por favor ingrese número telefónico con su código de país!"
            return {
                'name': 'Invalid Mobile Number',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'display.error.message',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context
            }
        else:
            # Error del wizard
            return {'type': 'ir.actions.act_window',
                    'name': _('Whatsapp Message'),
                    'res_model': 'whatsapp.wizard.contact',
                    'target': 'new',
                    'view_mode': 'form',
                    'view_type': 'form',
                    'context': {
                        'default_template_id': self.env.ref('odoo_whatsapp_integration.whatsapp_contacts_template').id},
                    }