import json
from ibm_watson import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions, EntitiesOptions, KeywordsOptions, RelationsOptions, CategoriesOptions


def nlu(text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='DX1bPz2BUsRdJDQn2UzfM_ubb5gScv_ZN0pawURFFvNt',
        url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api'
    )

    response = natural_language_understanding.analyze(
        text = text,
        language = 'it',
        features=Features(concepts=ConceptsOptions(),
                          entities = EntitiesOptions(),
                          keywords = KeywordsOptions(),
                          relations = RelationsOptions(),
                          categories = CategoriesOptions())).get_result()
    #print(json.dumps(response, indent = 2))
    for i in range(0, len(response['entities'])):
        #if response['entities'][i]['relevance'] > 0.5:
        text = response['entities'][i]['text']
        type = response['entities'][i]['type']
        print('entita: ' + text + ' ' + type)

    for i in range(0, len(response['keywords'])):
        #if response['entities'][i]['relevance'] > 0.5:
        text = response['keywords'][i]['text']
        print('keyword: ' + text)

    for i in range(0, len(response['relations'])):
        #if response['entities'][i]['relevance'] > 0.5:
        relation = response['relations'][i]['type']
        entity1_text = response['relations'][i]['arguments'][0]['entities'][0]['text']
        entity1_type = response['relations'][i]['arguments'][0]['entities'][0]['type']

        entity2_text = response['relations'][i]['arguments'][1]['entities'][0]['text']
        entity2_type = response['relations'][i]['arguments'][1]['entities'][0]['type']
        print(entity1_text + ' (' + entity1_type + ') ' + relation + ' ' + entity2_text + ' (' + entity2_type + ') ' )

    for i in range(0, len(response['concepts'])):
        #if response['entities'][i]['relevance'] > 0.5:
        text = response['concepts'][i]['text']
        print('concept: ' + text)

    for i in range(0, len(response['categories'])):
        #if response['entities'][i]['relevance'] > 0.5:
        label = response['categories'][i]['label']
        print('category ' + label)

text = 'cos\'e una "terra nullius"'
risposta1 = 'una terra contesa tra due stati'
risposta2 = 'una terra non occupata da uno stato'
risposta3 = 'un terreno instabile'
nlu(text)
print('-----------------')
nlu(risposta1)
print('-----------------')
nlu(risposta2)
print('-----------------')
nlu(risposta3)
