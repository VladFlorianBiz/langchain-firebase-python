from firebase_functions import https_fn
from firebase_admin import initialize_app
from firebase_functions import https_fn
from firebase_functions.params import SecretParam
from langchain.llms import OpenAI
import os

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

initialize_app()

"""Take the text parameter passed to this HTTP endpoint and use it as the prompt"""
@https_fn.on_request(min_instances=0, max_instances=2)
def on_request_example(req: https_fn.Request) -> https_fn.Response:

    # Grab the text parameter.
    prompt = req.args.get("text")
    if prompt is None:
        return https_fn.Response("No prompt parameter provided", status=400)

    # We can then initialize the wrapper with any arguments.
    llm = OpenAI(temperature=0.9, openai_api_key=OPENAI_API_KEY)
    
    # We can now call it on some input!
    result = llm(prompt)

    return https_fn.Response(result, status=200)