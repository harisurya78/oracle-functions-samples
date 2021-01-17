#
# oci-objectstorage-create-par-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import nltk
from newspaper import Article
article = Article('https://edition.cnn.com/2021/01/16/europe/trump-has-trashed-the-transatlantic-alliance-intl/index.html')
article.download()
article.parse()
article.nlp()
article.authors
print(article.keywords)
print(article.summary)
