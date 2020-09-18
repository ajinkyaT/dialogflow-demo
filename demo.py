from time import sleep

import dialogflow_v2 as dialogflow

from output_information import print_information

project_id = 'resume-help-utcu'
session_id = 13579876
language_code = 'en'


def get_response(input_text: str):
    text_input = dialogflow.types.TextInput(text=input_text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response


session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)
response = get_response('hello')
print(response.query_result.fulfillment_text)

para_list = []
default_input = [
    'AJ',
    '2019',
    '6 million',
]

for item in default_input:
    print(item)
    response = get_response(item)
    print(f'Response: {response.query_result.fulfillment_text}')
    if response.query_result.all_required_params_present:
        para_list.append(response.query_result.parameters.fields)
    sleep(2)

print_information(para_list)