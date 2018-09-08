## py-spyとは?
[benfred/py-spy: Sampling profiler for Python programs](https://github.com/benfred/py-spy)

- Rust製のpythonプロファイリング・ツール
- 対応しているpythonのバージョンは`2.3-2.7`、`3.3-3.7` と幅広い 

## Install

自分はRustユーザーではないのでpip経由でインストールします。

```
$ pip3 install py-spy
```

## Flask

Flaskで次のようなエントリーポイントを作成してアプリケーションを立ち上げる。

```python
@app.route('/name/<name>.json')
def hello_world(name):
    greet = "Hello %s from flask!" % name
    result = {
        "ResultSet": {
            "Result": {
                "Greeting": greet
            }
        }
    }

    response = Response(json.dumps(result))
    response.headers['Content-Type'] = "application/json"
    response.headers['Last-Modified'] = \
        "Last-Modified: Wed, 21 Jun 2012 07:00:25 GMT"
    return response
```
https://github.com/yuokada/py-spy-sample

```shell
$ python3.6 server.py
```

次に別のターミナルを立ち上げてpy-spyを実行する。

```bash
$ py-spy -h
py-spy 0.1.4
A sampling profiler for Python programs

USAGE:
    py-spy [FLAGS] [OPTIONS] --pid <pid> [python_program]...

FLAGS:
    -d, --dump        Dump the current stack traces to stdout
    -F, --function    Aggregate samples by function name instead of by line number
    -h, --help        Prints help information
    -V, --version     Prints version information

OPTIONS:
    -d, --duration <duration>    The number of seconds to sample for when generating a flame graph [default: 2]
    -f, --flame <flamefile>      Generate a flame graph and write to a file
    -p, --pid <pid>              PID of a running python program to spy on
    -r, --rate <rate>            The number of samples to collect per second [default: 1000]

ARGS:
    <python_program>...    commandline of a python program to run
```
```    
# 20秒間で秒間1万個サンプリングをとって結果をprofile.svgとして出力する。
$ sudo py-spy --flame profile.svg -d 20 -r 10000 -p 77170
Sampling process 10000 times a second for 20 seconds
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 200000/200000
Wrote flame graph 'profile.svg'. Samples: 200000 Errors: 0
```

### py-spyからアプリを立ち上げる方法について
`py-spy` からアプリを起動する方法も紹介されているが
`py-spy`が終了する時にサーバープロセスが残り続ける問題があった。

```
$ sudo py-spy --flame profile.svg -d 20 -r 10000 \
  -- python3.6 server.py
```


## Request

`py-spy`を立ち上げたらさらに別のターミナルから`ab`コマンドでサーバーにリクエストを送ってプロファイリングを取得する。
プロファイリングの時間が20秒なので5万リクエスト程度でプロファイリング中はずっとリクエストを受けている状態になる。

```shell
$ ab -n 50000 "http://127.0.0.1:8888/name/john.json"
```

## SVGでの結果の確認

生成された`profile.svg`をブラウザで開けば結果を確認出来る。

<img width="1205" alt="detail_2018-09-08 13.51.34.jpg" src="https://qiita-image-store.s3.amazonaws.com/0/4981/113724b9-4068-01dd-8c98-09bf9fdbcb9f.jpeg">

svgの右上に検索機能があるのでそこに今回実装したエントリーポイントの関数名`hello_world`を入力するとそこがピンク色にハイライトされる。

<img width="1201" alt="search_2018-09-08 13.55.23.jpg" src="https://qiita-image-store.s3.amazonaws.com/0/4981/4b157eab-57f1-dcf7-a506-6f5ae7728d54.jpeg">

プロファイリングの結果から今回実装したアプリケーションは非常にシンプルなもののためアプリケーション全体としては全く時間を占めていないことが分かった。

## まとめ

`py-spy`は手軽に導入出来て幅広いpythonのバージョンに対応していることから
`2.X`から`3.x`への移行時などにパフォーマンス・レグレッションが起きたりしていないか確認などに使えそうという感想が得られた。
