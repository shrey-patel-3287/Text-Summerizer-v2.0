from simplet5 import SimpleT5

def generate_headline(text):

    model = SimpleT5()

    model.load_model("t5","models\\headline_model", use_gpu=False)

    headline = model.predict(text)[0]

    return headline