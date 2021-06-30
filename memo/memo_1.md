# 構造化テキスト形式

　人が手で簡単に編集できる構造化テキスト形式をつくりたい。

## 既存

* INI
* DSV
* XML
* JSON
* YAML
* TOML

## 要件

* わかりやすいこと。人が目でみてすぐ構造やデータがわかること。
* 編集しやすいこと。人が手ですぐ思い通りに編集できること。
* 解析しやすいこと。プログラムによる構造テキストの読込・書込が簡単であること

### あればうれしい機能

* 外部ファイル参照
* 圧縮ファイル化（ZIP。複数ファイル参照して同一化）
* オブジェクト化（各種プログラミング言語におけるシリアライズ・デシリアライズ）
* コンパイルエラー（対処表示）
* リント成形
* 型定義
* バリデート
* エラー処理

## 構造

* List（Link, Triple, Tree, List, LinkList, Set, Taple, Array）
* KV（Dictionary, Hash）
* Class（Structure, 匿名型）
* Table（Classの配列）

### データ型

* バイナリ（エンディアン）
* テキスト（文字セット）

## テキスト形式

data
```
キー名	値
インスタンス名
	キー名	値
	キー名	値	値	値
	キー名	値, 値, 値
	キー名
		複数行値
		複数行値
		複数行値
	キー名:list
		複数行値
		複数行値
		複数行値
	キー名:text
		複数行値
		複数行値
		複数行値
	インスタンス名	鍵=値	鍵=値	鍵=値
	インスタンス名	鍵=値, 鍵=値, 鍵=値
インスタンス名.サブインスタンス名.サブサブ名
	キー名.サブキー名.サブサブキー名	値
[インスタンス配列要素型]
	キー名	値	
[インスタンス連想配列要素型.キー名]
	キー名	値
インスタンス名:継承元インスタンス名
インスタンス名:継承元インスタンス名１,継承元インスタンス名２,継承元インスタンス名３
インスタンス名:定義した型

<テーブル名>
列名Ａ	列名Ｂ	列名Ｃ
値１Ａ	値１Ｂ	値１Ｃ
値２Ａ	値２Ｂ	値２Ｃ
値３Ａ	値３Ｂ	値３Ｃ

<マトリクス名>
		列名Ａ	列名Ｂ	列名Ｃ
行名１	値１Ａ	値１Ｂ	値１Ｃ
行名２	値２Ａ	値２Ｂ	値２Ｃ
行名３	値３Ａ	値３Ｂ	値３Ｃ

主語　動詞　目的語
主語　動詞　目的語
主語　動詞　目的語

# コメント
# 外部ファイル参照
@/tmp/work/abc.toml
インスタンス名:ファイル名.型名
```

type
```
型名
	キー名	型名
	キー名	型名	デフォルト値	バリデータ
Enum型名
	名前１
	名前２
	名前３
```

* type
	* Binary
		* image(gif,png,jpg,webp)
		* audio(wav,mp3,flac,ogg)
		* movie(avi,mp4,webm)
	* Boolean（`0`/`1`, `f`/`t`(`F`/`T`,`true`/`false`,`True`/`False`,`TRUE`/`FALSE`)）
	* Numeric
		* int	整数（sign/unsign, size=1,2,4,8,...）
		* float	実数（浮動小数点数）
		* decimal（テキスト形式の実数。小数点の桁や値を丸めることなくテキスト形式で保存する）
	* Text
		* Path
		* Url
		* Base64
		* RegEx
		* Base64
		* StructText
			* Dsv
			* Xml
			* Json
			* Yaml
			* Toml
	* DateTime
		* Date `yyyy-MM-dd`
		* Time `HH:mm:ss`
		* Local `yyyy-MM-dd HH:mm:ss`
		* UTC `yyyy-MM-dd HH:mm:ssZ`, `yyyy-MM-dd HH:mm:ss+0900`
	* Color
		* RGB  255,255,255, #FFFFFF, 100%,100%,100%
		* LCh  100%,100%,100%
		* CMYK 100%,100%,100%
	* Ref
		* Null/None/Nil
		* 継承
		* 参照（参照ポインタ／値コピー）
		* ファイル参照（内部、外部）
* Container
	* Array/List
	* Tree
	* Dictionary/HashTable
	* Table

validate
```
number
0 <= ファイル.インスタンス.キー <= 100
ファイル.インスタンス.キー
	0 <= _ <= 100 ||
	-100 <= _ <= -999

datetime
yyyy-MM-ddTHH:mm:ss <= ファイル.インスタンス.キー <= yyyy-MM-ddTHH:mm:ss
ファイル.インスタンス.キー
	yyyy-MM-ddTHH:mm:ss <= _ <= yyyy-MM-ddTHH:mm:ss

text
ファイル.インスタンス.キー = 正規表現          Match
ファイル.インスタンス.キー == 文字列―完全一致 Equal
ファイル.インスタンス.キー -= 文字列―部分一致 In
ファイル.インスタンス.キー ^= 文字列―前方一致 StartsWith
ファイル.インスタンス.キー $= 文字列―後方一致 EndsWith

path
ファイル.インスタンス.キー = ext:txt
ファイル.インスタンス.キー = name:txt
ファイル.インスタンス.キー = file:name.ext
ファイル.インスタンス.キー = parent:dir/dir
ファイル.インスタンス.キー IsMovie,IsAudio,IsImage,Is3dModel...

binary
ファイル.インスタンス.キー IsMovie,IsAudio,IsImage,Is3dModel...

number|text
ファイル.インスタンス.キー = 選択肢１, 選択肢２, 選択肢３
ファイル.インスタンス.キー	選択肢１	選択肢２	選択肢３
ファイル.インスタンス.キー
	選択肢１
	選択肢２
	選択肢３
```

error
```
強制終了
例外スロー
メッセージ出力（ファイル（stdout,stderr,任意FD,任意ファイル））
イベント発火（それを契機に通知システムへ渡したり、メール発信するなど各種出力できる）
無視
```

# テキストから型を推測する

Number
```
[0-9]+[\.]?[0-9]*
```
整数
```
[0-9]+
```
実数
```
[0-9]*[\.]?[0-9]+
```
日時
```
yyyy[\-/]MM[\-/]dd[\-/][ T]HH:mm:dd[Z]?[+\-]TTTT
\d{4,}[\-/]\d{2}[\-/]\d{2}[\-/][ T]\d{2}:\d{2}:\d{2}[Z]?[+\-]TTTT
\d{4,}[\-/]\d{2}[\-/]\d{2}[\-/]
\d{2}:\d{2}:\d{2}
```

