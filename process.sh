

gcloud ml speech recognize-long-running \
	"gs://general-rodderscode-co-uk/$@.flac" \
	--language-code='en-gb' \
	--encoding='flac' \
	--async 
