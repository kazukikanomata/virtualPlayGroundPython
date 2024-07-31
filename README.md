# Python 仮想環境（venv）を使った環境構築マニュアル
このマニュアルでは、Python の venv モジュールを使って仮想環境を構築する手順を説明します。仮想環境は、プロジェクトごとに独立したパッケージやライブラリのセットを管理できるようにするためのツールです。

![セットアップガイド](1.jpg)
リンク：https://www.canva.com/design/DAGMYSdYUYk/RQ3x__u6iszcfdEW3735kw/edit?utm_content=DAGMYSdYUYk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

<b>前提条件</b>

- Python 3.x がインストールされていること。
- 以下のコマンドで確認する。

```
$ python3 --version
```

<b>目的</b>

- 全員のPC上で同じコマンドを試し実行するには、仮想環境が必要不可欠であると思いこれを作成
- 必要最小限の設定で、pythonを動かす環境を実現する。

## 1. プロジェクトディレクトリを作成する
まず、仮想環境を作成するプロジェクト用のディレクトリを作成します。

### ディレクトリを作成する

```
$ mkdir 自分の名前_project
```

### ディレクトに移動する

```
$ cd 自分の名前_project
```

## 2. 仮想環境を作成する
venv モジュールを使用して仮想環境を作成します。仮想環境のディレクトリ名は venv とします。

```
$ python3 -m venv venv
```
## 3. 仮想環境のスイッチをONする
仮想環境のスイッチを入れます。これにより、仮想環境内の Python インタプリタとパッケージが使用されるようになります。

<b>MacOS/Linux</b>

```
$ source venv/bin/activate
```

仮想環境のスイッチを入れると、コマンドラインのプロンプトが (venv) のように変わります。

![プロンプト画面](image1.png)

ターミナルにアップデート表示がでてくるのでアップデートしましょう。

![アップデート](image2.png)


## 4. パッケージをインストールする
仮想環境のスイッチを入れた状態で、必要なパッケージをインストールします。

### マウスやキーボードの操作を自動化するライブラリをインストール

<b>pyautoguiのインストール</b>

```
$ pip install pyautogui
```

参考：https://pypi.org/project/PyAutoGUI/


<b>pynuputのインストール</b>

```
$ pip install pynuput
```

参考：https://pypi.org/project/pynput/


<b>pyinstallerのインストール</b>

＊いまのところ不要

```
$ pip install pyinstaller
```

参考：https://pypi.org/project/pyinstaller/


## 5. Python実行コマンド
仮想環境のスイッチを入れた状態で、以下のコマンドを実行

```
$ python ファイル名
```

## 6. 仮想環境のスイッチをOFFする
仮想環境の使用が終わったら、仮想環境のスイッチを切り元のシェルに戻ります。

```
$ deactivate
```

## パッケージの一覧を保存する
プロジェクトで使用するパッケージの一覧を requirements.txt ファイルに保存します。これにより、他の開発者が同じ環境を再現するのが簡単になります。

```
$ pip freeze > requirements.txt
```

## 他の開発者が同じ環境を再現する方法
他の開発者が同じ環境を再現するためには、requirements.txt ファイルを使ってパッケージをインストールします。

<b>1. 仮想環境を作成して仮想環境のスイッチを入れる</b>

- プロジェクトディレクトリに移動し、仮想環境を作成してスイッチをONする。

```
$ python3 -m venv venv
$ source venv/bin/activate
```


<b>2. パッケージをインストールする</b>

- requirements.txt ファイルからパッケージをインストールします。

```
$ pip install -r requirements.txt
```

<b>3. Pythonを実行</b>

```
$ python ファイル名
```

<b>4. 仮想環境のスイッチをOFFする</b>

```
$ deactivate
```
