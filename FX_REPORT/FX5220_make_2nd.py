import pandas as pd
from datetime import datetime

pd.options.display.float_format="{:,.2f}".format

def generate_report():
  dt = str(input('기준일자를 yyyymmdd 형식으로 입력해주세요 : '))
  dt_trans = datetime.striptime(dt, '%Y%m%d')

  path = input('이번 기준년월 파일의 경로를 입력해주세요 : ')
  file = input('이번 기준년월 파일명을 file_name.csv 형식으로 입력해주세요 : ')
  path_file = path + '/' + file

  raw = pd.read_csv(path_file, sep=',', encoding = 'euc-kr')
  raw_copied = raw.copy()
  raw_copied.rename(columns={raw_copied.columns[0], '계좌번호'}, inplace = True)

  
