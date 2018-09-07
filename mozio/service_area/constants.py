from django.utils.translation import ugettext_lazy as _

ACCESS_TOKEN_EXPIRY = 5  # In minutes

LANGUAGE_CHOICE = (
    ('man', _('mandarin')),
    ('spa', _('spanish')),
    ('eng', _('english')),
    ('hin', _('hindi')),
    ('ara', _('arabic')),
    ('por', _('portuguese')),
    ('ben', _('bengali')),
    ('rus', _('russian')),
    ('jap', _('japanese')),
    ('pun', _('punjabi')),
)

LANGUAGE_CHOICE_DICT = {
    'man': 'mandarin',
    'spa': 'spanish',
    'eng': 'english',
    'hin': 'hindi',
    'ara': 'arabic',
    'por': 'portuguese',
    'ben': 'bengali',
    'rus': 'russian',
    'jap': 'japanese',
    'pun': 'punjabi',
}


LANGUAGE_CHOICE_REVERSE_DICT = {
    'mandarin': 'man',
    'spanish': 'spa',
    'english': 'eng',
    'hindi': 'hin',
    'arabic': 'ara',
    'portuguese': 'por',
    'bengali': 'ben',
    'russian': 'rus',
    'japanese': 'jap',
    'punjabi': 'pun'
}

CURRENCY_CHOICE = (
    ('USD', _('U.S.DOLLARS')),
    ('EUR', _('EUROS')),
    ('JPY', _('JAPANESE YEN')),
    ('GBP', _('GREAT BRITAIN POUND')),
    ('AUD', _('AUSTRALIAN DOLLARS')),
    ('CAD', _('CANADIAN DOLLARS')),
    ('CHF', _('SWISS FRANC')),
    ('CNY', _('CHINESE YUAN')),
    ('INR', _('INDIAN RUPEE')),
)
