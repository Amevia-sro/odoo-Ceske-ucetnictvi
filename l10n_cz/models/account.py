from odoo import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _prepare_liquidity_account(self, name, company, currency_id, type):
        res = super(AccountJournal, self)._prepare_liquidity_account(name, company, currency_id, type)
        if company.chart_template_id == self.env.ref('l10n_cz.czech_chart_template'):
            if res['code'] == '211':
                res['name'] = 'Pokladna'
                res.update({
                    'group_id': self.env.ref('l10n_cz.account_group_21').id,
                    })
            elif res['code'] == '221':
                res['name'] = 'Bankovní účty'
                res.update({
                    'group_id': self.env.ref('l10n_cz.account_group_22').id,
                    })
        return res

class AccountTaxTemplate(models.Model):
    _inherit = 'account.tax.template'

    rate_type = fields.Selection([
        ('basic', 'Basic'),
        ('first_reduced', 'First Reduced'),
        ('second_reduced', 'Second Reduced')
    ], string='VAT Rate Type')

    def _get_tax_vals(self, company, tax_template_to_tax):
        val = super(AccountTaxTemplate, self)._get_tax_vals(company, tax_template_to_tax)
        val.update({'rate_type': self.rate_type})
        return val

class AccountTax(models.Model):
    _inherit = 'account.tax'

    rate_type = fields.Selection([
        ('basic', 'Basic'),
        ('first_reduced', 'First Reduced'),
        ('second_reduced', 'Second Reduced')
    ], string='VAT Rate Type')
