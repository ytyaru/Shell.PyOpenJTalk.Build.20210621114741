#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# PyOpenJTalkをビルドする。
# CreatedAt: 2021-06-21
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	cd "$HERE"

	# PyOpenJTalkのパスと、それをインストールするパッケージの仮想環境パスを指定する。
	PATH_POJT='/tmp/work/'
	PATH_VENV='/tmp/work/test_repo/'
	mkdir -p "$PATH_POJT"
	mkdir -p "$PATH_VENV"

	# PyOpenJTalkリポジトリと、そのサブモジュールを取得する。
	cd "${PATH_POJT}"
	git clone https://github.com/r9y9/pyopenjtalk
	cd pyopenjtalk
	git submodule update -i

	# コードを書き換える
	# ./pyopenjtalk_rewrite_codes_1/...

	# Pythonのパッケージ仮想環境をつくる。
	cd "$PATH_VENV"
	python3 -m venv env
	. "${PATH_VENV}env/bin/activate"
	pip install numpy
	pip install Cython
	pip install six

	# ビルドする。
	cd "${PATH_POJT}pyopenjtalk"
	python3 setup.py install

	# リビルド＆再インストールする。（コードを修正したらこれを実行する）
	#cd "${PATH_POJT}pyopenjtalk"
	#pip uninstall pyopenjtalk
	#python3 setup.py install

	# インポートできるかテストする。PyOpenJTalkをインストールした仮想環境を有効化する。`import pyopenjtalk`するコードを書いて実行する。
	. "${PATH_VENV}env/bin/activate"
	pip install simpleaudio
	python3 test_play.py
}
Run "$@"
