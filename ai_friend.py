import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey')
print(open_file('openaiapikey'))


def gpt_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['USER:', 'NILS:']):
    gpt_prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    gpt_response = openai.Completion.create(
        engine=engine,
        prompt=gpt_prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = gpt_response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    print(openai.api_key)
    main_prompt = 'Give me an instruction of how to implement openai api in python'
    response = gpt_completion(main_prompt)
    print(response)

