
types = [
    'Wniosek ogólny', 'Podanie o rejestrację',
    'Wniosek o rozłożenie opłaty za studia na raty',
    'Wniosek o zmniejszenie opłaty za powtarzanie',
    'Wniosek o przedłużenie terminu złożenia pracy dyplomowej',
    'Potwierdzenie opłaty', 'Podanie o urlop'
]

def foreach_type(df, f):
    appl_types = df['Rodzaj wniosku']
    return map(lambda t: f(df[appl_types == t], t), types)

def print_type(type_): print(f'================={type_}=================')
