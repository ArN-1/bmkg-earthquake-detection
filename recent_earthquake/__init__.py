# Latest earthquake detection application

import requests

def data_extraction():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        content = requests.get('https://bmkg.go.id', headers=headers)
    except Exception:
        return None

    if content.status_code == 200:
        print(content.text)



        """
          tanggal : 02 Desember 2023
           waktu : 20:42:04 WIB
          magnitudo : 5.0
          kedalaman : 108 km
          lokasi : LS = 3.53 BT =  102.01
          pusat gempa : Pusat gempa berada di laut 23 km BaratDaya Bengkulu Utara
          dirasakan : Dirasakan (Skala MMI): II-III Kota Bengkulu, II Mukomuko
    
          """
        hasil = dict()
        hasil['tanggal'] = '02 Desember 2023'
        hasil['waktu'] = '20:42:04 WIB'
        hasil['magnitudo'] = 5.0
        hasil['kedalaman'] = '108 km'
        hasil['lokasi'] = {'ls' : 3.53, 'bt' : 102.01}
        hasil['pusat'] =  'Pusat gempa berada di laut 23 km BaratDaya Bengkulu Utara'
        hasil['dirasakan'] =  'Dirasakan (Skala MMI): II-III Kota Bengkulu, II Mukomuko'
        return hasil
    else:
        return None


def show_data(result):
  if result is None:
    print("======Cannot find data======")
    return



  print("Gempa Terakhir berdasarkan BMKG")
  print(f"tanggal : {result['tanggal']}")
  print(f"waktu : {result['waktu']}")
  print(f"waktu : {result['waktu']}")
  print(f"magnitudo : {result['magnitudo']}")
  print(f"kedalaman : {result['kedalaman']}")
  print(f"lokasi : LS =  {result['lokasi']['ls']}, BT = {result['lokasi']['bt']} ")
  print(f"pusat : {result['pusat']}")
  print(f"dirasakan : {result['dirasakan']}")




