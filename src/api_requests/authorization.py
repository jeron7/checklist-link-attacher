from constants import OAUTH_TOKEN, OAUTH_CONSUMER_KEY

def get_authorization_headers():
    from decouple import config
    oauth_consumer_key = config(OAUTH_CONSUMER_KEY)
    oauth_token = config(OAUTH_TOKEN)
    oauth_string_format = 'OAuth oauth_consumer_key="{0}", oauth_token="{1}"'
    return {'authorization' : oauth_string_format.format(oauth_consumer_key, oauth_token)};