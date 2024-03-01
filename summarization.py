prompt_template = """
You are a summarization system that can provide summaries with associated confidence scores.
In clear and concise language, provide three short summaries of the following essay, along with their confidence scores.
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.

essay : {"Corruption today is a world-wide phenomenon and India is one of the most corrupt nations in the world. Corruption is an indication of decadence. A corrupt person is termed immoral and dishonest. Only a person with greatly eroded values indulges in corruption."}
"""