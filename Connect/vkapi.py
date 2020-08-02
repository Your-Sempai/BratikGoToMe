import vk_api
import requests
from other import token, id
from vk_api.bot_longpoll import VkBotLongPoll

session = requests.Session()
vk = vk_api.VkApi(token=token)
vk._auth_token()
longpoll = VkBotLongPoll(vk, id)