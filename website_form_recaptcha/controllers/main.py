# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request
from openerp.exceptions import ValidationError

import json


class WebsiteForm(http.Controller):

    @http.route(
        '/website/recaptcha/',
        type='http',
        auth='public',
        methods=['GET'],
        website=True,
    )
    def recaptcha_public(self):
        return json.dumps({
            'site_key': request.env['ir.config_parameter'].get_param(
                'recaptcha.key.site'
            ),
        })

    def extract_data(self, **kwargs):
        """ Inject ReCaptcha validation into pre-existing data extraction """
        captcha_obj = request.env['website.form.recaptcha']
        ip_addr = request.httprequest.environ.get('HTTP_X_FORWARDED_FOR')
        if ip_addr:
            ip_addr = ip_addr.split(',')[0]
        else:
            ip_addr = request.httprequest.remote_addr
        try:
            captcha_obj.action_validate(
                kwargs.get(captcha_obj.RESPONSE_ATTR), ip_addr
            )
        except ValidationError:
            raise ValidationError([captcha_obj.RESPONSE_ATTR])
        return True
