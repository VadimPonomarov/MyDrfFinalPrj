SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorisation',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False
}
