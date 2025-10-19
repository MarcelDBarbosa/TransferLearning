# TransferLearning
Um código em Python para exemplificar o uso de Transfer Learning, usando a rede do Keras VGG16 para reconhecer 2 categorias (cavalo ou humano)

Cavalo_ou_humano.ipynb usa a técnica de Transfer Learning para treinar a última camada do modelo VGG16 do Keras para classificar imagens de cavalos ou humanos. O conjunto de dados é baixado da internet, dividido em três grupos (treino, validação e teste). 
Alguns pré-processamentos são feitos para ajustar as imagens ao padrão do modelo.
No final do treinamento é gerado um arquivo com as informações do modelo para utilização posterior.
Após o treinamento ainda é possível escolher outras imagens para realizar a classificação, ou usar o arquivo inferir.py para fazer a classificação usando o arquivo salvo durante o treino.

OBSERVAÇÃO: O projeto pode ser usado com outras imagens, com qualquer número de categorias. A única modificação necessária é na parte da predição, para determinar a correta categoria inferida pelo modelo.


