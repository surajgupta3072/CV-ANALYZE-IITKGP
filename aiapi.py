import openai
import config

api_key = config.DevelopmentConfig.OPENAI_KEY
openai.api_key = api_key

def generateChatResponse(prompt):
    messages =[]
    messages.append(  {"role": "system", "content": "Please review my CV and provide specific feedback on how I can improve it. I am particularly interested in your suggestions regarding the content, formatting, and overall presentation. Your detailed comments will greatly help me in making my CV more effective and impactful."})

    question ={}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = "oops!"
    return answer


