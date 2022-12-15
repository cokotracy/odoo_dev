# -*- coding: utf-8 -*-

from odoo import models

class AccountGenericTaxReport(models.AbstractModel):
    _inherit = 'account.generic.tax.report'

    def _get_grids_refund_sql_condition(self):
        # Overridden in order to also consider as refunds the 'entry' moves
        # generated by the POS when returning a product without creating an invoice.
        parent_condition = super()._get_grids_refund_sql_condition()
        return """(%s)
                  OR (
                    (EXISTS(SELECT id FROM pos_session WHERE pos_session.move_id = account_move.id)
                    OR EXISTS(SELECT id FROM pos_order WHERE pos_order.account_move = account_move.id))
                    AND account_move.move_type = 'entry'
                    AND debit > 0)
        """ % parent_condition
