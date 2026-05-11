# tk-copy
Dropboxのカメラアップロードから写真と動画を
それぞれのフォルダに名前を変えながらコピーするツール

## pythonのバージョン
3.12.3

## 前提条件
Ubuntu上でDropboxとShotwellを使用  

## 設定
FromDirとToDirの設定  
copytool.pyをエディタで開き次の定数を設定  
例  
FROM_DIR　=>　/home/*username*/Dropbox/カメラアップロード  
TO_DIR_JPG　=>　/home/*username*/photo  
TO_DIR_MP4　=>　/home/*username*/Videos
