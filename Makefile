clean:
	rm -rf public
	rm .hugo_build.lock

build:
	hugo

run: build
	hugo serve

new_article:
	touch content/journal/TMP_NEW_ARTICLE.md
	echo "---\ntitle: ''\ndate: ''\n---" > content/journal/TMP_NEW_ARTICLE.md
	nvim content/journal/TMP_NEW_ARTICLE.md
