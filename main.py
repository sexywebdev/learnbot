import telegram
import requests

def get_wiki_summary(topic):
    # Get the Wikipedia summary for a topic.
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=" + topic
    response = requests.get(url)
    summary = response.json()["query"]["pages"][0]["extract"]
    return summary

def learn_handler(update, context):
    chat_id = update.effective_chat.id
    topic = update.message.text
    summary = get_wiki_summary(topic)
    telegram.send_message(chat_id, summary)

app = telegram.Bot(token="YOUR_TOKEN_HERE")
app.add_handler(telegram.CommandHandler("learn", learn_handler))

app.polling()
