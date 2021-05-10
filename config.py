import json
from questionary import prompt

questions = [
    {
        'type': 'confirm',
        'message': 'Do you want to create a new config.json file?',
        'name': 'continue',
        'default': True,
    },
    {
        'type': 'path',
        'name': 'path',
	'complete_style': 'READLINE_LIKE',
	'message': "What is the path to the tfsecurity cam directory?",
    },
    {
        'type': 'text',
        'name': 'TOKEN',
        'message': "Enter your Telegram Bot API Token:",
    },
    {
        'type': 'text',
        'name': 'chat_id',
        'message': 'Enter your Telegram chat id:',
    },
    {
        'type': 'text',
        'name': 'confidence',
        'message': 'Enter the desired confidence interval for the object detection model 0-1 (0.7 recommended):',
    },
]


answers = prompt(questions)

with open("config.json", "w") as outfile: 
    json.dump(answers, outfile)

print("New config.json file created")
