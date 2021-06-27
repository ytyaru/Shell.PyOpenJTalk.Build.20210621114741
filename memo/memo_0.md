# 台本

　セリフと音声合成パラメータをテキストで渡すと音声を得られるようにしたい。また、パラメータはセリフ集である台本と別紙にしたい。

```
htsvoiceファイル種別:声パラメータ	セリフ
```
```
メイ:嬉,早,大,響	こんにちは。私はメイです。
メイ:嬉,早,大,響	こんにちは。私はメイです。
メイ:嬉,早,大,響	こんにちは。私はメイです。
```
```
htsvoiceファイル識別名:感情,速度,音量,リバーブ是非	セリフ
htsvoiceファイル識別名:嬉/恥/怒/悲, 早/遅, 大/小, 響	セリフ
```
```
メイ(嬉/恥/怒/悲, 早/遅, 大/小, 響)	セリフ
```


感情|メイ|東北|たくみ
----|----|----|------
普通|mei_normal.htsvoice|tohoku-f01-neutral.htsvoice|takumi_normal.htsvoice
嬉しい|mei_happy.htsvoice|tohoku-f01-happy.htsvoice|takumi_happy.htsvoice
怒り|mei_angry.htsvoice|tohoku-f01-angry.htsvoice|takumi_angry.htsvoice
悲しい|mei_sad.htsvoice|tohoku-f01-sad.htsvoice|takumi_sad.htsvoice
恥ずかしい|mei_bashful.htsvoice|-|-

## パラメータ

```
DefaultVoice
	Speed=1.0, 
	HalfTone=0.0,
	SamplingFrequency=-1,
	FramePeriod=-1,
	AllPass=-1,
	Postfiltering=0.0,
	Threshold=0.5,
	Weight=1.0,
	WeightF0=1.0,
	Volume=0.0,
	BufferSize=0.0
メイ:DefaultVoice
	htsvoice='/tmp/work/...htsvoice'
	Speed=1.0, 
	HalfTone=0.0,
	SamplingFrequency=-1,
	FramePeriod=-1,
	AllPass=-1,
	Postfiltering=0.0,
	Threshold=0.5,
	Weight=1.0,
	WeightF0=1.0,
	Volume=0.0,
	BufferSize=0.0
メイ嬉
	htsvoice='/tmp/work/...htsvoice'
```

# 



* 音声合成(TTS)
	* input
		* text,parameter
		* 台本(text,parameter複数)
	* output
		* メモリ
			* 1text
			* ストリーミング
		* Wavファイル
			* 1
			* 複数
			* 分割・統合
		* 
		* 
			
* ゆっくり動画作成
	* TTM(Text to Movie)


VoiceParameter.txt

:型名
:型名:継承型名

インスタンス名:型名
インスタンス名
	キー名	値
	キー名	値	値	値
	キー名
		複数行値
		複数行値
		複数行値
	キー名	鍵＝値	鍵＝値	鍵＝値
インスタンス名.サブインスタンス名.サブサブ名
	キー名.サブキー名.サブサブキー名	値
[インスタンス配列要素型]
[インスタンス連想配列要素型.キー名]

@/tmp/work/abc.toml
インスタンス名:ファイル名.型名


型名
	キー名	型

Binary
Boolean
Numeric
	整数
	実数（浮動小数点数）
Base64
DateTime
Array/List
Dictionary/HashTable
Table
Text

	
HtsVoice
	RootDir = ''
VoiceFunction(args)
	'速' : Speed += 1.0
	'遅' : Speed -= 0.3
	'大' : Volume += 1.0
	'小' : Volume -= 0.3
MeiFunction()
メイ
	htsvoice='/tmp/work/...htsvoice'
メイ
	htsvoice='/tmp/work/...htsvoice'
	Speed=1.0, 
	HalfTone=0.0,
	SamplingFrequency=-1,
	FramePeriod=-1,
	AllPass=-1,
	Postfiltering=0.0,
	Threshold=0.5,
	Weight=1.0,
	WeightF0=1.0,
	Volume=0.0,
	BufferSize=0.0
メイ-嬉:メイ
メイ-恥:メイ
メイ-怒:メイ
メイ-悲:メイ
メイ(嬉,早/遅,大/小,響)
メイ(嬉/恥/怒/悲, 早/遅, 大/小, 響)	セリフ

sinario.txt

メイ:嬉,早,大,響	こんにちは。私はメイです。

感情|メイ|東北|たくみ
----|----|----|------
普通|mei_normal.htsvoice|tohoku-f01-neutral.htsvoice|takumi_normal.htsvoice
嬉しい|mei_happy.htsvoice|tohoku-f01-happy.htsvoice|takumi_happy.htsvoice
怒り|mei_angry.htsvoice|tohoku-f01-angry.htsvoice|takumi_angry.htsvoice
悲しい|mei_sad.htsvoice|tohoku-f01-sad.htsvoice|takumi_sad.htsvoice
恥ずかしい|mei_bashful.htsvoice|-|-

















