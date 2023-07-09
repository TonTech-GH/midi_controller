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

# カレントディレクトリをVSCodeで開く
code .