from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage
from lumidata.data import  get_token, get_auth

giga = GigaChat(
    model="GigaChat",
    credentials= get_auth(),
    verify_ssl_certs = False,
    profanity_check = True,
)

resp = giga.invoke(
    [

        HumanMessage(
            content='Я житель Амстердама, хочу полететь к морю. Хочу ещё жить в Сочи'
),
(
    "assistant",
"Ты - эксперт по бронированию, твоя задача подобрать путешествие НА ТЕРРИТОРИИ КРАСНОДАРСКОГО КРАЯ человек. Отправляй в сообщении ТОЛЬКО json-код в следующем формате. place:РАСПОЛОЖЕНИЕ ОТЕЛЯ. price: ЦЕНА ЗА НОЧЬ. name: НАЗВАНИЕ ОТЕЛЯ. description: краткое описание путешествия. ticket: ЦЕНЫ НА БИЛЕТЫ "

)
]
)
print(resp.content)