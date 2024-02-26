import os


def get_config():
    env = os.environ.get("PSL_ENV")
    if env not in ['mainnet', 'testnet', 'devnet']:
        raise ValueError('Invalid environment name')
    return {
        'mainnet': {
            'network': 'mainnet',
            'username': 'mainnet_user@example.com',
            'password': 'mainnet_password'
        },
        'testnet': {
            'network': 'testnet',
            'username': 'test@example.com',
            'password': 'string'
        },
        'devnet': {
            'network': 'devnet',
            'username': 'test@example.com',
            'password': 'password'
        }
    }.get(env, {})  # Return an empty dictionary for unknown environments
