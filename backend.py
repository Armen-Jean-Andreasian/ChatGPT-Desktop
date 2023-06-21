import openai


class ChatBot:
    def __init__(self):
        self._api = "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"
        openai.api_key = self._api

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,  # the length of bot answers 2000-4000
            temperature=0.5  # 0-1 close to 0 more accurate less diverse answers
        )
        result = response.choices[0].text
        return result
