from models.summary_model.model import SummaryModel,tokenizer

trained_model = SummaryModel.load_from_checkpoint("models\\summary_model\\best-checkpoint.ckpt")
trained_model.freeze()

def summarize(text):
  text_encoding = tokenizer(
  text,
  max_length=512,
  padding="max_length",
  truncation=True,
  return_attention_mask=True,
  add_special_tokens=True,
  return_tensors="pt"
)

  generated_ids = trained_model.model.generate(
    input_ids=text_encoding["input_ids"],
    attention_mask=text_encoding["attention_mask"],
    max_length=150,
    num_beams=2,
    repetition_penalty=2.5,
    length_penalty=1.0,
    early_stopping=True
  )

  preds = [
    tokenizer.decode(gen_id, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    for gen_id in generated_ids
  ]

  return "".join(preds)