from ipynb.fs.full.jean.common import foreach_type
from ipynb.fs.full.jean.common._3factorize import appls
from ipynb.fs.full.jean.common._3factorize import to_factorize, yesno_cols, yesno_en_cols

nominal = to_factorize + yesno_cols + yesno_en_cols + ['Status']

to_drop = ['Numer dokumentu', 'Student', 'Osoba przyjmująca', 'Osoba przypisana', 'Liczba załączników', 'Semestr rejestracji']

splitted = foreach_type(appls, lambda df, _: df.drop(to_drop + ['Rodzaj wniosku'], 'columns'))

general, reg, study_payment, repetition, extension, confirmation, holiday = tuple(splitted)
