from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Выбрать регион", callback_data="regions")],
    [InlineKeyboardButton(text="Поддержать проект(пожертвование)", callback_data="donat")],
    [InlineKeyboardButton(text="Пожелание и предложение", callback_data="feedback")]
])




kb_regions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Краснодарский край", callback_data='categories')],
    [InlineKeyboardButton(text="Ростовская область", callback_data='categories')],
    [InlineKeyboardButton(text="Москва и М. область", callback_data='categories')],
    [InlineKeyboardButton(text="Краснодарский край", callback_data='categories')],
    [InlineKeyboardButton(text="Республика Крым", callback_data='categories')],
    [InlineKeyboardButton(text="Волгоградская область", callback_data='categories')],
    [InlineKeyboardButton(text="Ставропольский край", callback_data='categories')],
    [InlineKeyboardButton(text="Другие регионы", callback_data='categories')],

])
kb_categories = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1.Мастер-классы и Сборы', callback_data='master-class')],
        [InlineKeyboardButton(text='2.Турниры', callback_data='tournaments')],
        [InlineKeyboardButton(text='3.Ищу партнер(а/шу)', callback_data='find_partner')],
        [InlineKeyboardButton(text='4.Одежда', callback_data='clothes')],
        [InlineKeyboardButton(text='5.Обувь (б/у, объявления)', callback_data='second_shoes')],
        [InlineKeyboardButton(text='6.Ищу попутчиков на турнир', callback_data='companion')],
        [InlineKeyboardButton(text='7. Ищу ЗАЛ для танцев', callback_data='find_room')],
        [InlineKeyboardButton(text='8.PRO-AM', callback_data='pro-am')],
        [InlineKeyboardButton(text='9. Танцевальный магазин(новые вещи); ПОШИВ; Аренда костюма', callback_data='shop')],
        [InlineKeyboardButton(text='10. Ищу работу', callback_data='work')],
        [InlineKeyboardButton(text='11. Клубы по Спортивным Бальным Танцам', callback_data='clubs')],
        [InlineKeyboardButton(text='12. Обсуждения(ФОРУМ), Полезности; Музыка', callback_data='forums')],
        [InlineKeyboardButton(text='К выбору региона', callback_data='regions')],
        [InlineKeyboardButton(text='обратная связь', callback_data='feedback')],
    ]
)

master_class = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/masterclass_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

tournaments = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/turnir_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

find_partners = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/look4partner_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

clothes = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/odezda_dg')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

shoes = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/obuv_dg')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

companies = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/companion_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

find_room = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/zal_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

pro_am = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/proam_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

shop = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/newthing_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

work = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/job_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

clubs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/danceclub_dg_kk')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])

forums = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ссылка на канал', url='https://t.me/danceguide_forum')],
    [InlineKeyboardButton(text='Вернутся к выбору региона', callback_data='regions')],
    [InlineKeyboardButton(text='Вернутся к выбору категорий в текущем регионе', callback_data="categories")]
])



