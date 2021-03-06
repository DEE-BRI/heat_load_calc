.. include:: definition.txt

.. raw:: latex

    \clearpage

========================================================================================================================
気象データの指定
========================================================================================================================

気象データをCSVファイルで独自に用意する場合は次のフォーマットに従うこと。

行

1行目・・・列ヘッダー

2行目～8761行目・・・データ

データは1時間ごとに1年間分用意する。つまり、必ず、データの長さ（行数）は8760でなければならない。
また、先頭のデータは、1月1日の0:00とする。

列

1列目
    | 日時。ヘッダー名は空白にすること。"yyyy/m/d hh:mm:ss"の形式で書く。例: "1989/1/1 0:00"。その際、年については閏年で無い年を指定すること。閏年で無い限り、特にどの年を指定しても結果には影響しない。
2列目
    | 外気温度。ヘッダー名は"temperature"。単位は ℃ 。データ数は8760。
3列目
    | 外気絶対湿度。ヘッダー名は"absolute humidity"。単位は kg / kg(DA) 。データ数は8760。
4列目
    | 法線面直達日射量。ヘッダー名は"normal direct solar radiation"。単位は W / |m2| 。データ数は8760。
5列目
    | 水平面天空日射量。ヘッダー名は"horizontal sky solar radiation"。単位は W / |m2| 。データ数は8760。
6列目
    | 夜間放射量。ヘッダー名は"outward radiation"。単位は W / |m2| 。データ数は8760。
7列目
    | 緯度。ヘッダー名は"longitude"。単位は度。この列はデータは1つしか入らない。2つ目のデータ以降は空白とすること。
8列目
    | 経度。ヘッダー名は"latitude"。単位は度。この列はデータは1つしか入らない。2つ目のデータ以降は空白とすること。
    
次にCSVファイルの例を示す。

.. list-table:: 表1 気象データファイルの例
    :header-rows: 1
    :widths: 1,1,1,1,1,1,1,1

    * - 
      - temperature
      - normal direct solar radiation
      - horizontal sky solar radiation
      - outward radiation
      - absolute humidity
      - longitude
      - latitude
    * - 1989/1/1 0:00
      - 19.1
      - 0.0
      - 0.0
      - 22.2
      - 11.3
      - 26.21
      - 127.685
    * - 1989/1/1 1:00
      - 19.7
      - 0.0
      - 0.0
      - 22.2
      - 10.9
      - 
      - 
    * - 1989/1/1 2:00
      - 19.9
      - 0.0
      - 0.0
      - 22.2
      - 10.9
      - 
      - 
    * - 1989/1/1 3:00
      - 21.2
      - 0.0
      - 0.0
      - 16.7
      - 11.2
      - 
      - 

以下、日時が、1989/12/31 23:00 になるまで続く。
