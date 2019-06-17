import pandas as pd

from ipynb.fs.full.jean.common._1load import appls

reasonable_status = {
    'Zamknięty - decyzja negatywna': 0,
    'Zamknięty - odrzucony formalnie': 0,
    'Decyzja pozytywna - wymagany podpis studenta': 1, 
    'Zamknięty - decyzja pozytywna': 1
}

appls = appls[appls.Status.isin(reasonable_status)]
appls['Status'] = appls['Status'].map(reasonable_status)

appls['Data złożenia'] = pd.DatetimeIndex(appls['Data złożenia'])
appls['Data zamknięcia'] = pd.to_datetime(appls['Data zamknięcia'], errors='coerce')
appls['month'] = appls['Data złożenia'].dt.month
