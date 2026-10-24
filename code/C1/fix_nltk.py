import nltk
import os
# os.environ["NLTK_ALLOW_PROXIED_URLOPEN"] = "1"
#
# nltk.download('punkt', force=True)
# nltk.download('averaged_perceptron_tagger', force=True)

# 测试分词
tokens = nltk.word_tokenize("Hello, this is a test sentence.")
print("分词结果:", tokens)

# 测试词性标注
tags = nltk.pos_tag(tokens)
print("词性标注:", tags)

# 分词器已下载成功。