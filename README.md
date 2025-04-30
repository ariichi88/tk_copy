# tk-copy
Dropboxのカメラアップロードから写真と動画を
それぞれのフォルダに名前を変えながらコピーするツール

## pythonのバージョン
3.12.3

## 前提条件
Ubuntu上でDropboxとShotwellを使用  

## 準備
Shotwell 設定で「ライブラリのディレクトリで新規ファイルを監視する」にチェックを入れてください
> 現在上記設定をしても自動的にインポートできなくなってます（Ubuntu24.04LTS）
Dropbox カメラアップロードを使用してください  

## インストール
GitHubからクローン  
```
git clone git@github.com:ariichi88/tk-copy.git
```
copytool.pyをパスの等っている場所にコピー 
```
cp copytool.py /hoge/fuga
```
FromDirとToDirの設定  
copytool.pyをエディタで開き次の定数を設定  
例  
FROM_DIR　=>　/home/*username*/Dropbox/カメラアップロード  
TO_DIR_JPG　=>　/home/*username*/photo  
TO_DIR_MP4　=>　/home/*username*/Videos

実行権（パーミッション）の変更 
```
chmod +x copytool.py
```

## 最後に
Ubuntuを使用していてDropboxとShotwellを使用している人しか関係しませんが良ければ使ってみてください。  