import pandas as pd
from pandas import DataFrame, Series


def __verify_seq__(group):
    tmp = 0
    for seq in group['SEQ'].sort_values():
        if seq - tmp == 1:
            tmp = seq
        else:
            print(f'[verify_seq]\n{group}')
            break


def __verify_type_id__(group):
    type_ids = group['TYPE_ID']  # type: Series
    if type_ids.where(lambda type_id: type_id == 8).count() == 0: print(f'[verify_type_id]\n{group}')


targets = pd.read_csv('EVENT_DETAIL.csv', encoding="SHIFT-JIS")
groups = targets.groupby('EVENT_ID')  # type: DataFrame

for name, group in groups:
    __verify_seq__(group)
    __verify_type_id__(group)
