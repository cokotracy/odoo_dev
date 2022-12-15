from odoo import models, fields, api, _

class SendContactMessage(models.TransientModel):
    _name = 'whatsapp.wizard.contact'

    user_id = fields.Many2one('res.partner', string="Destinatario", default=lambda self: self.env[self._context.get('active_model')].browse(self.env.context.get('active_ids')))
    mobile_number = fields.Char(related='user_id.mobile', required=True)
    message = fields.Text(string="Mensaje", required=True)

    # Error en link -- Corregido
    def send_custom_contact_message(self):
        if self.message:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            number = self.user_id.mobile
            link = "https://api.whatsapp.com/send/?phone=" + number #Cambiado link de conexión a Whatsapp web
            send_msg = {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }
            return send_msg