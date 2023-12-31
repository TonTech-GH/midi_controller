#!/bin/sh
# =============================================================
# このフォルダをVSCodeで開く
# =============================================================
# このファイルがあるフォルダの絶対パスを取得
#   - $0がこのファイルの絶対パス
#     - $0にはスペースが含まれる場合があるので""で括っている
#   - dirname でそのディレクトリ名を取得する
#     - ``で囲われた部分はコマンドとして実行される 
CurDir=`dirname "$0"`

# カレントディレクトリをこのファイルがあるフォルダに移動
#   - パスにスペースが含まれる場合があるので""で括っている
cd "$CurDir"

# Pythonスクリプトを実行
export PYTHONPATH="$CurDir"
echo $PYTHONPATH
python3 src/ddj_flx4.py
