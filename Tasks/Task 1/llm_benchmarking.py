
import pandas as pd
import glob
import os
from openai import OpenAI



openrouter_key = os.environ['OPENROUTER_KEY']


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=openrouter_key,
)

models = ["google/gemma-2-27b-it","google/gemini-flash-1.5-8b","mistralai/mistral-7b-instruct-v0.3","meta-llama/llama-3.3-70b-instruct","qwen/qwen-2.5-7b-instruct","qwen/qwen-2.5-72b-instruct","openai/gpt-4o-mini","microsoft/phi-4","openai/gpt-4o-2024-11-20","google/palm-2-chat-bison-32k"]

def experiments(original, edited, m):
  completion = client.chat.completions.create(
    # extra_headers={
    #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    #   "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    # },
    model=m,
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": f"""i will provide you an edited autobiographical sentence as well as the original sentence. You need to determine what type of hallucination is injected into the edited sentence from the following list:

  Entity: The edited sentence contains incorrect or misplaced entities (e.g., names, locations, dates) that make the sentence factually inaccurate.
  Relation: The edited sentence misrepresents semantic relationships, such as actions (verbs), connections (prepositions), or cause-effect relationships.
  Sentence: The entire edited sentence contradicts evidence or known facts from the original, resulting in a complete mismatch or falsehood.


  Original Sentence: {original}
  Edited Sentence: {edited}


  respond with one word."""
          },
          # {
          #   "type": "image_url",
          #   "image_url": {
          #     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          #   }
          # }
        ]
      }
    ]
  )

  return completion.choices[0].message.content


path = "dataset/*.xlsx"
list_paths = glob.glob(path)


for i in list_paths:
    df = pd.read_excel(i)
    
    lang = i.split('/')[-1].split('_')[0]
    print(f'{lang} started')
    df = df[df['final_label'] != '0']
    df = df[df['final_label'] != 0]
    labels = {}
    for i in models:
        print(f'{i} started')
        l = []
        model_name = i
        #   model, tokenizer = create_model_and_tokenizer(model_name)
        model_n = model_name.split('/')[-1]
        for index, row in df.iterrows():
            original = row['orig_sentence']
            edited = row['edited_sentence']
            # labels.append(experiments(original, edited, i))

            try:
                label = experiments(original, edited, i).strip()
            except Exception as e:
                label = 0
            l.append(label)

        # print(index, label)






        labels[model_n] = l
        df[model_n] = l
        df.to_excel(f'{lang}_experiments.xlsx', index=False)
