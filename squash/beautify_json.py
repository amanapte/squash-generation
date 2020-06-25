import simplejson as json

json_list = [ "./final/Custom.json",
                "./temp/Custom/final_qa_set.json", 
                "./temp/Custom/generated_questions.json",
                "./temp/Custom/nbest_predictions.json", 
                "./temp/Custom/null_odds.json",
                "./temp/Custom/predictions.json" ]

for i in json_list:
    with open(i,"a") as f:
        obj = json.load(f)
        f.close()     
    outfile = open(i, "w")
    outfile.write(json.dumps(obj, indent=4, sort_keys=True))
    outfile.close()
