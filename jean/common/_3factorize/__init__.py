import pandas as pd
from sklearn import preprocessing
from ipynb.fs.full.jean.common._2dual_status import appls

to_factorize = [
    'Tryb studiów', 'Typ studiów', 'Język wykładowy', 'Kierunek',
    'Osoba przyjmująca', 'Semestr rejestracji',
    'Semestr aktualny', 'Brakujace przedmioty'
]

yesno_cols = [
    'Słowo rodzin lub famil w uzasadnieniu',
    'Słowo zdrow lub health w uzasadnieniu',
    'Słowo bardzo proszę w uzasadnieniu', 'Słowo losow w uzasadnieniu',
    'Słowo prac lub work w uzasadnieniu',
    'Słowo obiecuję lub promise w uzasadnieniu',
    'Słowo zobowiązuję w uzasadnieniu'
]

yesno_en_cols = [
    'Słowo regulamin w uzasadnieniu', 
    'Słowo formaln w uzasadnieniu',
    'Słowo postęp w uzasadnieniu',
    'Złożone odwołanie'
]


le = preprocessing.LabelEncoder()

apply_encoder = lambda df, labels: df.apply(le.fit(labels).transform).astype('bool')

appls[yesno_cols] = apply_encoder(appls[yesno_cols], ['NIE', 'TAK'])
appls[yesno_en_cols] = apply_encoder(appls[yesno_en_cols], ['NO', 'YES'])

DATETIME_COLS = ['Data złożenia', 'Data zamknięcia']
appls[DATETIME_COLS] = appls[DATETIME_COLS].apply(lambda col: pd.to_datetime(col, format='%d.%m.%y %H:%M', errors='coerce'))
appls[['submitted', 'closed']] = appls[DATETIME_COLS].applymap(lambda dt: dt.dayofyear)
