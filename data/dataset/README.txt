wget http://www.trec-cds.org/2021_data/ClinicalTrials.2021-04-27.part1.zip
unzip ClinicalTrials.2021-04-27.part1.zip
rm ClinicalTrials.2021-04-27.part1.zip

wget http://www.trec-cds.org/2021_data/ClinicalTrials.2021-04-27.part2.zip
unzip ClinicalTrials.2021-04-27.part2.zip
rm ClinicalTrials.2021-04-27.part2.zip

wget http://www.trec-cds.org/2021_data/ClinicalTrials.2021-04-27.part3.zip
unzip ClinicalTrials.2021-04-27.part3.zip
rm ClinicalTrials.2021-04-27.part3.zip

wget http://www.trec-cds.org/2021_data/ClinicalTrials.2021-04-27.part4.zip
unzip ClinicalTrials.2021-04-27.part4.zip
rm ClinicalTrials.2021-04-27.part4.zip

wget http://www.trec-cds.org/2021_data/ClinicalTrials.2021-04-27.part5.zip
unzip ClinicalTrials.2021-04-27.part5.zip
rm ClinicalTrials.2021-04-27.part5.zip

cd ..

python get_corpus.py