import streamlit as st
import difflib

st.title("🚆 Railway / Bus Enquiry Chatbot")

responses = {
    "ticket price": "Ticket price from Chennai to Madurai is ₹450.",
    "train timing": "Train departs at 6:30 AM and arrives at 1:00 PM.",
    "platform number": "Platform number is 3.",
    "cancellation policy": "Cancellation allowed before 24 hours with 50% refund.",
    "available seats": "There are 45 seats available.",
    "train number": "Train number is 12637.",
    "arrival time": "Arrival time is 1:00 PM.",
    "departure time": "Departure time is 6:30 AM."
}

def getAccuracy(user_input):
    max_accuracy = 0
    accurate_key = ""

    for key in responses.keys():
        ratio = difflib.SequenceMatcher(None, key, user_input).ratio()

        if ratio > max_accuracy:
            max_accuracy = ratio
            accurate_key = key

    if max_accuracy > 0.6:
        return accurate_key
    else:
        return ""

user_input = st.text_input("Ask your question:")

if st.button("Send"):

    user_input = user_input.lower().strip()

    reply = responses.get(user_input, "")

    if reply == "":
        best_match = getAccuracy(user_input)
        reply = responses.get(best_match, "Sorry, I did not understand.")

    st.success("Bot: " + reply)
