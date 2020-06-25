import simplejson as json

json_list = [ "/conent/squash-generation/squash//final/Custom.json",
                "/content/squash-generation/squash/temp/Custom/final_qa_set.json", 
                "/content/squash-generation/squash/temp/Custom/generated_questions.json",
                "/content/squash-generation/squash/temp/Custom/nbest_predictions.json", 
                "/content/squash-generation/squash/temp/Custom/null_odds.json",
                "/content/squash-generation/squash/temp/Custom/predictions.json" ]

for i in json_list:
    with open(i,"a") as f:
        obj = json.load(f)
        f.close()     
    outfile = open(i, "w")
    outfile.write(json.dumps(obj, indent=4, sort_keys=True))
    outfile.close()
