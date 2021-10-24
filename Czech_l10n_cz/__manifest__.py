{
    'name' : 'Czech Republic - Accounting',
    'version' : '1.0',
    'category': 'Localization',
    'author': 'Amevia s.r.o.',
    "website" : "https://www.amevia.eu",
    'summary': 'This module adds the Czech accounting-charts of accounts,fiscal possitions,VAT taxes',
    'description': """ 
This is the module to manage the accounting chart for Czech Republic in Odoo.
==================================================================================
    """,
    'depends' : [
        'account',
    ],
    'data': [
        'data/account_group.xml',
        'data/account_account_tag.xml',
        'data/l10n_cz_chart_data.xml',
        'data/account_tax_report_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_tax_fiscal_position_data.xml',
        'data/account_chart_template_data.xml',
        'views/account_tax_view.xml',
        'views/product_view.xml',
    ],
    'images': [
        'static/description/logo.png',
    ],
}
