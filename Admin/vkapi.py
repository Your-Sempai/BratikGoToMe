import vk_api
import requests
from other import admin_token, admin_id
from vk_api.bot_longpoll import VkBotLongPoll

session = requests.Session()
vk = vk_api.VkApi(token=admin_token)
vk._auth_token()
longpoll = VkBotLongPoll(vk, admin_id)



