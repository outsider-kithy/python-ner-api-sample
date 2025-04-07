from flask import Flask, request, Blueprint
from transformers import BertJapaneseTokenizer, BertForTokenClassification
from transformers import pipeline
import json

company = Blueprint(
	"company",
	__name__
)

@company.route("/")
def index():
	text = ""
	if request.args.get("q") is not None:
		text = request.args.get("q")
	else:
		text ="No Text"
	
	# モデルの読み込み
	model = BertForTokenClassification.from_pretrained("jurabi/bert-ner-japanese")
	# トークナイザーの読み込み
	tokenizer = BertJapaneseTokenizer.from_pretrained("jurabi/bert-ner-japanese")
	#パイプラインの構築
	ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)
	# 予測
	outputs = ner_pipeline(text)
	print(outputs)

	# entityが「B-法人名」もしくは「I-法人名」のワードを抽出してnames_tokens配列に格納
	names_tokens = []
	for output in outputs:
		if output['entity'] == 'B-法人名' or output['entity'] == 'I-法人名':
			names_tokens.append(output['word'])
		else:
			continue

	# entityが「B-法人名」の後に続く「I-法人名」をentityに持つ単語を結合し、固有名詞として配列resultsに格納
	results = []
	for i in range(len(outputs)):
		if(outputs[i]['entity'] == 'B-法人名'):
			name = outputs[i]['word']
			for j in range(i+1, len(outputs)):
				if outputs[j]['entity'] == 'I-法人名':
					# #を取り除いて結合
					name += outputs[j]['word'].replace("#", "")
				else:
					break
			results.append(name)

	# resultsをjson形式で返す
	return json.dumps(results, ensure_ascii=False)

