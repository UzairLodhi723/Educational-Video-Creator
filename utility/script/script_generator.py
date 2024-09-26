from groq import Groq
import json
import re
client = Groq(
   api_key= "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" ,
)
def generate_script(topic):
    prompt = (
        """You are a seasoned content writer for a YouTube Shorts channel, specializing in facts videos. 
        Your facts shorts are concise, each lasting less than 50 seconds (approximately 77 words). 
        They are incredibly engaging and original. When a user requests a specific type of facts short, you will create it.

        For instance, if the user asks for:
        Weird facts
        You would produce content like this:

        Weird facts you don't know:
        - Bananas are berries, but strawberries aren't.
        - A single cloud can weigh over a million pounds.
        - There's a species of jellyfish that is biologically immortal.
        - Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.
        - The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.
        - Octopuses have three hearts and blue blood.

        You are now tasked with creating the best short script based on the user's requested type of 'facts'.

        Keep it brief, highly interesting, and unique.

        Strictly output the script in a JSON format like below, and only provide a parsable JSON object with the key 'script'.

        # Output
        {"script": "Here is the script ..."}
        """
    )

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": topic}
        ]
    )

    content = response.choices[0].message.content
    print(content, "i am content")  # Debugging line

    # Step 1: Find the JSON block using regex, ensuring we correctly extract the JSON object
    json_match = re.search(r'{.*}', content, re.DOTALL)
    
    if not json_match:
        print("No JSON object found in the response.")
        return None

    json_content = json_match.group(0)

    # Step 2: Clean the JSON content by removing unnecessary newlines and handling control characters
    json_content = json_content.replace('\n', ' ').replace('\r', '').replace('\\n', ' ')

    try:
        script = json.loads(json_content)["script"]
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print("Invalid content:", json_content)
        return None  # Handle the error appropriately

    return script