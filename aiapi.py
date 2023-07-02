import openai
import config

api_key = config.DevelopmentConfig.OPENAI_KEY
openai.api_key = api_key

def generateChatResponse(prompt):
    messages =[]
    messages.append(  {"role": "system", "content": "You are a helpful assistant."})

    question ={}
    question['role'] = 'user'
    question['content'] = prompt
    response = openai.ChatCompletion.create(
    model="text-davinci-003",
    messages=messages,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    try:
        answer = response['choices'][0]['message']['content']
    except:
        answer = "oops!"
    return answer


