# -*- coding: utf-8 -*-
import hashlib
import os
import werkzeug
from odoo import http

class Sso(http.Controller):
    @http.route('/sso', auth='user')
    def index(self, **kw):
        redirectUri = os.environ['SSO_REDIRECT_URI']
        secret = os.environ['SSO_SECRET']
        state = kw.get('state', '')
        uid = str(http.request.env.context.get('uid'))
        data = state + '/' + uid + '/' + secret
        code = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return werkzeug.utils.redirect(redirectUri + "?uid=" + uid + "&code=" + code)
