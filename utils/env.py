from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN_ID = env('ADMIN')

GROUP_ID = -4593145391

ADMIN = 5018312156
