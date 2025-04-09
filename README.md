# sirokuma

sirokuma(しろくま)は、セキュリティログ基盤のための、ポーリング動作を前提としたログ収集ライブラリです。

## 読み方・由来

ポーリングする人(poller) x ホッキョクグマ(polar)

## 使い方

### オブジェクト

sirokuma は以下のようなオブジェクトから構成されています。

| オブジェクト |    インポートパス    |                                      説明                                      |
| :----------: | :------------------: | :----------------------------------------------------------------------------: |
|   Sirokuma   |  sirokuma.Sirokuma   |                     Stream の実行を司る、メインのクラス。                      |
|    Source    |   sirokuma.Source    |                   ログの収集元を抽象化したインターフェイス。                   |
| Destination  | sirokuma.Destination |                   ログの保存先を抽象化したインターフェイス。                   |
|    Stream    |   sirokuma.Stream    | Source と Destination をグルーピングし、実行管理のためのタグを管理するクラス。 |

### Source と Destination

Source と Destination は、Amazon S3 や標準入出力などの主要なログの保存場所を抽象化したサブパッケージを持つ想定で作っています。  
以下のようなインポートパスで使えます。

```python
# テキストファイルからの読み出し
from sirokuma.source.file import File
# 標準出力への書き込み
from sirokuma.destination.stdout import Stdout
```

サブパッケージの開発にあたっては、ABC を使った抽象基底クラス（インターフェイス）である Source と Stream を継承して作成します。  
Source の戻り値は、`typing.IO[bytes]`を満たす必要があります。

### 基本的な使い方

examples/01_how-to-use/main.py を参考に説明します。

- Sirokuma に、Stream のリストを与えて宣言します。
- 各 Stream は、引数として以下のオブジェクトを持ちます。
  - Source: ログの収集元
  - Destination: ログの保存先
  - 任意のタグの配列

```python
import sirokuma
from sirokuma.source.file import File
from sirokuma.destination.stdout import Stdout
from sirokuma.stream import Stream


poller = sirokuma.Sirokuma([
    Stream(
            File('land_animals.txt'),
            Stdout(),
            ['land'],
        ),
    Stream(
            File('sea_animals.txt'),
            Stdout(),
            ['sea'],
        ),
    Stream(
            File('sky_animals.txt'),
            Stdout(),
            ['sky'],
        ),
    ])
```

Stream のタグを指定して実行します。実行方法は以下の 3 パターンです。

- `run_any_tags_matched()`: 実行時に指定したタグのうち、**いずれか**にマッチしている Stream を実行する。
- `run_all_tags_matched()`: 実行時に指定したタグのうち、**全て**にマッチしている Stream を実行する。
- `run_all()`: **タグに関係なく、全ての Stream を実行する。** フールプルーフのために、`kakugo=True`を指定する必要がある。

```python
tags = ['land', 'sea']

print(f'# tags: {tags}')
print('# run_any_tags_matched runs streams matched ANY specified tags.')
poller.run_any_tags_matched(tags)

print('# run_all_tags_matched runs streams matched ALL specified tags.')
poller.run_all_tags_matched(tags)

print('# run_all runs all streams. You need kakuko to do that.')
poller.run_all(kakugo=True)
```

### クラウドにおける使い方

examples/02_usecase-on-cloud/main.py を参考に説明します。

sirokuma で作った Python ファイルをクラウドサービス上のコンテナサービスや関数実行サービスでホストし、それらを Amazon EventBridge などのスケジューラで定期実行することを想定して作っています。タグの指定は、スケジューラが実行時引数として指定することを想定しています。
