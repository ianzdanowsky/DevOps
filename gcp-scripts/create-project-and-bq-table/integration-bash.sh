#!/bin/bash

# Ao executar o script passe dois parâmetros, primeiro o nome e ID do projeto, depois o environment para label, exemplo:
# bash script projeto_exemplo_123 dev

gcloud projects create $1 --folder=84591264540 --labels=env=$2 --name=$1

sleep 5

gcloud config set project $1

gcloud services enable bigquery.googleapis.com

bq mk --dataset --location=US $1:chromedash 

bq mk --table $1:chromedash.all_chromebooks \
ou:STRING,chromebook:STRING,ultimo_uso:TIMESTAMP,email_u_usuario:STRING,regiao:STRING,municipio:STRING,inep:STRING,nome_escola:STRING,local_mapa:STRING,latitude:STRING,longitude:STRING,tempo:BIGNUMERIC,sn:STRING,mac_address:STRING,ou_chrome:STRING,device_id:STRING,model:STRING,modelo:STRING,nivel_ensino:STRING,serie:STRING,tipo:STRING,turma:STRING,escola:STRING,data:DATETIME,ativo:INTEGER,inativo:INTEGER