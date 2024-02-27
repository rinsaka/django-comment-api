# django-comment-api アプリケーション
- コメント掲示板の API バージョンです．
- https://rinsaka.com/django4/api/index.html に記載された手順で，[テストの自動化](https://rinsaka.com/django4/api/13.html)までを実装しています．
- ユーザ認証などの機能はありません．
- React などで開発したフロントエンドからの利用を想定して，[OCRS エラーの回避](https://rinsaka.com/django4/api/61.html)も行っています．

## 利用方法
### 仮想環境の構築
- Python に Django, djangorestframework, django-cors-headers という3つのライブラリをインストールすれば動作するはずです．
- base 環境にインストールしてもよいですし，次の通り仮想環境を構築してインストールしてもよいでしょう．

- Python 3.11 の仮想環境を構築し，Django などをインストールします．

```
% conda create -n py311api python=3.11
% conda activate py311api
% pip install -r requirements.txt
```

### データベースのマイグレーションとテストデータの投入

- データベースの内容が Git には含まれていないので，データベースのテーブルを作成し，テストデータを投入します．

```
% python manage.py migrate
% python manage.py loaddata comments/fixtures/comments-data.json
```

### サーバの起動

- 開発用のサーバを起動します．

```
% python manage.py runserver
```

### コマンドラインからの接続

- サーバを起動した状態で別のターミナルから curl コマンドで API にアクセスします．

```
% curl http://127.0.0.1:8000/comments/
{"count":10,"next":"http://127.0.0.1:8000/comments/?page=2","previous":null,"results":[{"id":9,"title":"9個目のコメント","body":"コメントの本文9","updated_at":"2023-11-21T11:20:00"},{"id":10,"title":"10個目のコメント","body":"コメントの本文10","updated_at":"2023-11-21T11:10:00"}]}%
% curl http://127.0.0.1:8000/comments/1/
{"id":1,"title":"最初のコメント","body":"コメントの本文","updated_at":"2023-11-21T11:01:00"}%
```

- 新規投稿の例です．POST メソッドを使います．

```
% curl -X POST -d "title=新規投稿" -d "body=本文です" http://127.0.0.1:8000/comm
ents/
{"id":11,"title":"新規投稿","body":"本文です","updated_at":"2024-02-27T09:41:53.271163"}%
% curl http://127.0.0.1:8000/comments/
{"count":11,"next":"http://127.0.0.1:8000/comments/?page=2","previous":null,"results":[{"id":11,"title":"新規投稿","body":"本文です","updated_at":"2024-02-27T09:41:53.271163"},{"id":9,"title":"9個目のコメント","body":"コメントの本文9","updated_at":"2023-11-21T11:20:00"}]}%
```

- 新規投稿した id=11 のコメントを編集します．PUT メソッドを使います．

```
% curl -X PUT -d "title=タイトル更新" -d "body=本文も更新" http://127.0.0.1:8000
/comments/11/
{"id":11,"title":"タイトル更新","body":"本文も更新","updated_at":"2024-02-27T09:43:30.962596"}%
% curl http://127.0.0.1:8000/comments/
{"count":11,"next":"http://127.0.0.1:8000/comments/?page=2","previous":null,"results":[{"id":11,"title":"タイトル更新","body":"本文も更新","updated_at":"2024-02-27T09:43:30.962596"},{"id":9,"title":"9個目のコメント","body":"コメントの本文9","updated_at":"2023-11-21T11:20:00"}]}%
```

- id = 11 のコメントを削除します．DELETE メソッドを使います．

```
% curl -X DELETE http://127.0.0.1:8000/comments/11/
% curl http://127.0.0.1:8000/comments/
{"count":10,"next":"http://127.0.0.1:8000/comments/?page=2","previous":null,"results":[{"id":9,"title":"9個目のコメント","body":"コメントの本文9","updated_at":"2023-11-21T11:20:00"},{"id":10,"title":"10個目のコメント","body":"コメントの本文10","updated_at":"2023-11-21T11:10:00"}]}%
```
