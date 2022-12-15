from odoo import models, fields, api, _
import html2text
import urllib.parse as parse

class SendMultipleContactMessage(models.TransientModel):
    _name = 'whatsapp.wizard.multiple.contact'

    partner_id = fields.Many2one('res.partner', string="Receptor")
    mobile = fields.Char(required=True, string="Número Contacto")
    message = fields.Text(string="Mensaje", required=True)

    def send_multiple_contact_message(self):
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + ' '
            message_string = parse.quote(message_string)
            html2text.html2text(message_string)
            message_string = message_string[:(len(message_string) - 3)]
            number = self.mobile
            link = "https://api.whatsapp.com/send/?phone=" + number #Cambiado link de conexión a Whatsapp web
            send_msg = {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }
            return send_msg