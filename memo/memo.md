# wavファイル保存できない

　`HTS_Engine_save_riff`関数を使えばWevファイルに保存できる。ただしその前に各種ストリームを生成せねばならない。

* [cpp-mecab_get_feature-function-examples.html](https://cpp.hotexamples.com/jp/examples/-/-/Mecab_get_feature/cpp-mecab_get_feature-function-examples.html)

```c
		HTS_Engine_create_sstream(&open_jtalk_.engine);
		HTS_Engine_create_pstream(&open_jtalk_.engine);
		HTS_Engine_create_gstream(&open_jtalk_.engine);
		if (wavfp != NULL)
			HTS_Engine_save_riff(&open_jtalk_.engine, wavfp);
```

　つまり以下の関数をその順序で実行せねばならない。

1. `HTS_Engine_create_sstream`
2. `HTS_Engine_create_pstream`
3. `HTS_Engine_create_gstream`
4. `HTS_Engine_save_riff`

　しかし、[PyOpenJTalk][]にはストリーム系の3関数がエクスポートされておらず呼び出せない。[pyopenjtalk/htsengine/__init__.pxd][]

[pyopenjtalk/htsengine/__init__.pxd]:https://github.com/r9y9/pyopenjtalk/blob/master/pyopenjtalk/htsengine/__init__.pxd

　さらにインポート元の[HTS_engine.h][]にすら定義されていない。ならどこにあるの？

[HTS_engine.h]:https://github.com/r9y9/hts_engine_API/blob/master/src/include/HTS_engine.h

[HTS_hidden.h]:https://github.com/r9y9/hts_engine_API/blob/master/src/lib/HTS_hidden.h

　[HTS_hidden.h][]にそれらしき関数がある。

* `HTS_SStreamSet_create`
* `HTS_PStreamSet_create`
* `HTS_GStreamSet_create`

　ただし引数が多い。構造をよく理解せねばならない予感。

