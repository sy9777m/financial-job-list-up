# pip install requests pandas bs4 openpyxl

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


def job_list_up():
    job_table = pd.DataFrame(columns=['job', 'link'])
    for p in range(1, 11):
        res = requests.get('http://www.kofia.or.kr/brd/m_96/list.do', params={
            'page': str(p),
            'multi_itm_seq': '0',
            'itm_seq_1': '0',
            'itm_seq_2': '0'
        })

        soup = bs(res.text, 'html.parser')
        temp_list = soup.findAll('td', attrs={'class': 'left'})
        for i in temp_list:
            job = i.a.text
            link = 'http://www.kofia.or.kr/brd/m_96' + i.a['href'][1:]
            temp_series = pd.Series([job, link], index=job_table.columns)
            job_table = job_table.append(temp_series, ignore_index=True)

    job_table.to_excel('job_table.xlsx', index=False)


if __name__ == '__main__':
    job_list_up()