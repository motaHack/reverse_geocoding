# 概要
* CSV内の緯度経度から市区町村などの行政区分を割り出し、緯度経度と共に行政区分をCSVで出力します。
* 国土地理院のシェープファイルを前提に作っていますがカラム指定次第で実行できるはず
  * https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_3.html#prefecture00

# 検証環境
* Python 3.8.2
* pip3 21.0.1
* conda 4.9.2

# 環境構築
* 国土地理院からシェープファイルを取得し展開（全国版推奨
  * shpとdbfとshxが必要になります 
* `pip3 install shapely`
* `pip3 install geofeather`
* geopandasのインストールhttps://geopandas.readthedocs.io/en/latest/getting_started/install.html 

# 使い方
* 初回に以下のコマンドでshpファイルからfeatherを作成します
 * shpファイルをそのまま使うよりも処理時間が2/3になるのでそうしています
 `python3 make_feather.py filename.shp `
* config.iniで以下を指定して実行
  * 生成されたfeatherのファイル名
  * 出力したいファイル名
  * 解析したいファイル名
  * 緯度経度の入ったカラムの番号
