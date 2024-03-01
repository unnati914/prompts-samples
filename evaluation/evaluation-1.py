prompt_template = """
BASIC CONTEXT -
******
You are a seasoned quality control executive.
You deeply review confidence score you strictly review them to perform your task.
Check whether the confidence score provided here is accurate or not with respect to the essay provided below. You can give your results in true or false, true for correct confidence score and false for incorrect confidence score.
******

You are given the essay below : 
*****
essay : {"Corruption today is a world-wide phenomenon and India is one of the most corrupt nations in the world. Corruption is an indication of decadence. A corrupt person is termed immoral and dishonest. Only a person with greatly eroded values indulges in corruption."}

You are given the confidence score below -
********
confidence_score : {0.9}
**********

"""