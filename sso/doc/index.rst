Odoo SSO
========

Module to use Odoo as SSO provider for other web-based application

Example environment variables:
SSO_REDIRECT_URI=http://localhost:8000/login_check
SSO_SECRET=supersecret

When a user is redirect to /sso?state=$STATE, the Odoo login form will be shown. 
After successful login, the user is redirected to:
$SSO_REDIRECT_URI?uid=$UID&code=$HASH
where $UID is the unique Odoo user id and $HASH is the SHA256 of "$STATE/$UID/$SSO_SECRET"

The target app must compare the hash in order to verify authentication