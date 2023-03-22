# !pip install transformers

# importing the libraries
from transformers import AutoModelForCausalLM, AutoTokenizer

# load the model and tokenizer
model_name = "bert-large-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# input prompt 
prompt = "The quick brown fox ran "

# predict the next sentence
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output_ids = model.generate(input_ids, max_length=50, do_sample=True)
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output_text)