import urllib2
import json

from flask import current_app as app


def get_weixin_login_url(url):
    app_id = app.config['WEIXIN_AK']
    scope = "snsapi_base"
    return "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=login#wechat_redirect" % (app_id, url, scope)


def get_weixin_user_openid(code):
    app_id = app.config['WEIXIN_AK']
    app_secret = app.config['WEIXIN_SK']
    token_url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (app_id, app_secret, code)
    response = urllib2.urlopen(token_url)
    html = response.read()
    json_info = json.loads(html)
    return json_info.get('openid')
