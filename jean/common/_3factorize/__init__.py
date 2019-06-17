from ipynb.fs.full.jean.common._2dual_status import appls

yesno_map = {
    'NIE': 0,
    'TAK': 1
}
yesno_en_map = {
    'NO': 0,
    'YES': 1
}

to_factorize = [
    'Student', 'Tryb studiów', 'Typ studiów', 'Język wykładowy', 'Kierunek',
    'Osoba przyjmująca', 'Osoba przypisana', 'Semestr rejestracji',
    'Semestr aktualny', 'Brakujace przedmioty',
    'Informacje o pracach dyplomowych'
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
appls[to_factorize] = appls[to_factorize].stack().rank(method='dense').unstack()

for c in yesno_cols: 
    appls[c] = appls[c].map(yesno_map)
for c in yesno_en_cols: 
    appls[c] = appls[c].map(yesno_en_map)
