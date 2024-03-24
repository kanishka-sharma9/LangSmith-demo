from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# os.environ['LANGCHAIN_TRACKING_V2']='True'
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(messages=[
    ('system',"you are a helpful coding assistant.please respond to the user's question using only the provided context."),
    ('user',"question:{question}\n\ncontext:{context}")

])

question="can you summarize the speech to be under 200 words?"
context="""
Ladies and gentlemen,

Today, I stand before you to discuss a game that transcends mere entertainment and delves into the realms of myth, emotion, and the very essence of humanity itself. I speak of none other than "God of War," a masterpiece of storytelling and gaming prowess that has captivated hearts and minds around the globe.

At its core, "God of War" is more than just a game; it's an epic saga that explores the depths of human nature, the consequences of our actions, and the eternal struggle between gods and mortals. Developed by Santa Monica Studio and released in 2005, this iconic franchise has undergone a remarkable evolution, culminating in the 2018 release that redefined what a video game could achieve.

The protagonist, Kratos, is a character whose journey is as tragic as it is compelling. Once a Spartan warrior consumed by rage and vengeance, he becomes a symbol of redemption and the quest for atonement. Throughout the series, we witness his transformation from a merciless warrior to a complex and deeply conflicted individual burdened by the weight of his past.

But "God of War" is not just about Kratos; it's about the relationships he forms along the way, particularly with his son, Atreus. The bond between father and son serves as the emotional anchor of the narrative, weaving themes of love, sacrifice, and the desire for a better future. As players guide Kratos and Atreus through the richly realized world of Norse mythology, they experience not only the thrill of epic battles but also the intimacy of familial moments and the resonance of profound philosophical questions.

What sets "God of War" apart is its meticulous attention to detail and its commitment to storytelling excellence. From its breathtaking visuals to its haunting musical score, every aspect of the game is crafted with precision and care. The Norse mythology setting adds layers of depth and intrigue, inviting players to explore a world teeming with gods, monsters, and ancient mysteries.

Yet, for all its grandeur and spectacle, "God of War" never loses sight of its characters' humanity. Kratos, with his flaws and scars, serves as a reminder that even the mightiest among us are not immune to weakness or doubt. His journey is a testament to the resilience of the human spirit and the capacity for growth and change, even in the face of insurmountable odds.

Moreover, "God of War" challenges players to confront difficult truths about themselves and the world around them. Through its themes of power, hubris, and the cyclical nature of violence, the game prompts us to reflect on our own actions and the impact they have on those around us. In a world plagued by conflict and division, "God of War" offers a message of hope—that redemption is possible, and that even the gods themselves are not beyond the reach of compassion and forgiveness.

In conclusion, "God of War" stands as a towering achievement in the world of gaming—a testament to the power of storytelling, the artistry of game design, and the enduring appeal of mythology. As we embark on this epic journey alongside Kratos and Atreus, let us remember that our actions have consequences, that our choices shape our destinies, and that even in the darkest of times, there is always a glimmer of hope. Thank you.

God of War, a game that transcends mere entertainment and delves into the realms of myth, emotion, and the very essence of humanity itself."""

model=ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)
parser=StrOutputParser()
chain=prompt | model | parser

response=chain.invoke({
    'question':question,
    'context':context,
})

print((response))