# -*- coding: utf-8 -*-

{
    'name': 'Customer Follow Up Management (Beta)',
    'version': '14.0.1.0.0',
    'category': 'Accounting',
    'description': """Customer FollowUp Management""",
    'summary': """Customer FollowUp Management""",
    'author': 'Odoo Mates, Odoo S.A, OdooDev',
    'license': 'LGPL-3',
    'website': '',
    'depends': ['account', 'mail'],
    'data': [
        'security/account_followup_security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/followup_print_view.xml',
        'wizard/followup_results_view.xml',
        'views/followup_view.xml',
        'views/account_move.xml',
        'views/partners.xml',
        'views/report_followup.xml',
        'views/reports.xml',
        'views/followup_partner_view.xml',
        'report/followup_report.xml',
    ],
    'demo': ['demo/demo.xml'],
    'images': ['static/description/banner.png'],
    # Inte portad till Odoo 18 (repot står på gren 14.0). Versionen
    # '14.0.1.0.0' är ogiltig för Odoo 18 och adapt_version() kastar
    # ValueError -> "Module om_account_followup: invalid manifest" ->
    # HTTP 500 på ALLA /web/static/*. Med installable: False sväljer
    # Odoo felet (modules/module.py load_manifest).
    # Skriv INTE om versionsnumret — det döljer att modulen inte är portad.
    # Se /srv/salt/README.md ("Bara TVÅ fällde registryt") och T/12318.
    'installable': False,
    'auto_install': False,
}
