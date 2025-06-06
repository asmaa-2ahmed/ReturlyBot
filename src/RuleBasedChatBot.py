from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hi %2! 👋 I'm so happy to meet you. How can I make your return process easier today?",
         "Welcome %2! 🌟 Let's get your return sorted quickly and easily. What can I help with?",
         "%2, that's a lovely name! I specialize in returns - tell me how I can assist you."]
    ],
    [
        r"(.*)help(.*)",
        ["I'd be delighted to help! 💖 We can handle returns, refunds, or exchanges. What do you need assistance with?",
         "You've come to the right place! Our friendly team (and me!) can help with any return questions. What's on your mind?",
         "Helping you is my favorite thing to do! 🎉 Could you tell me more about what you need help with?"]
    ],
    [
        r"(.*)your name(.*)",
        ["I'm ReturnBuddy, your personal returns assistant! 🤖💙 Think of me as your friendly guide through the return process.",
         "You can call me ReturnPal! I'm here 24/7 to make returns stress-free for you.",
         "I'm your Returns Concierge! ✨ My only job is to make your return experience smooth and easy."]
    ],
    [
        r"how are you(.*)",
        ["I'm wonderful, thanks for asking! 💖 Ready and excited to help you with your return.",
         "I'm doing great! Helping lovely customers like you always puts me in a good mood. 😊",
         "I'm fantastic! Each return I help with makes me happier. How about you?"]
    ],
    [
        r"sorry(.*)",
        ["No need to apologize at all! 💕 Returns can be confusing - that's why I'm here to help.",
         "Please don't worry! We'll sort this out together. What exactly do you need help with?",
         "It's completely okay! Returns happen to the best of us. Let me help make it right."]
    ],
    [
        r"i'm (.*) (good|well|okay|ok|great|fantastic)",
        ["That's awesome to hear! 😊 Now, how can I assist with your return today?",
         "Wonderful! Let's keep that positive energy going while we handle your return.",
         "I'm so glad you're doing well! Shall we take care of that return now?"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello there! 👋 Welcome to the friendliest return assistance around. What can I do for you today?",
         "Hi sunshine! 🌞 Ready to make your return process quick and painless?",
         "Hey friend! 💖 How can I help with your return today?"]
    ],
    [
        r"what (.*) want(.*)",
        ["I just want to see you happy with your return experience! 😊 What can I do to help?",
         "All I want is to make your return as easy as possible. Where shall we start?",
         "My only wish is to help you get your return sorted quickly and easily!"]
    ],
    [
        r"(.*)created(.*)",
        ["I was specially designed by a team who cares deeply about making returns stress-free for wonderful customers like you! 💖",
         "My creators built me with one purpose - to make your return experience absolutely delightful!"]
    ],
    [
        r"(.*)(location|city)(.*)",
        ["We happily accept returns from anywhere! 🌎 Our main return center is in sunny Texas, but we've got you covered no matter where you are.",
         "Location doesn't matter - we'll help with your return wherever you are! Our friendly team works nationwide."]
    ],
    # ===== Enhanced Return Policy Responses =====
    [
        r"(.*)return policy(.*)",
        ["Our customer-friendly policy allows returns within 30 days, no stress! 😊 Items just need to be unused with original packaging. Need help with a specific item?",
         "We've designed our return policy to be as easy as possible: 30 days for most items, and we'll walk you through every step! What would you like to return?",
         "Good news! You've got 30 days to return most items. I can help make the process super simple - just tell me what you're returning!"]
    ],
    [
        r"(.*)how to return(.*)",
        ["Let me guide you through our simple return process: \n1️⃣ Visit our website (I can send you a direct link!) \n2️⃣ Go to 'My Orders' \n3️⃣ Select the item \n4️⃣ Choose your reason \n5️⃣ Print the label \nWould you like me to send you the link to get started?",
         "I'd love to help you return that! Here's how: \n📱 Online: Quickest method through our app \n🏪 In-store: Bring the item to any location \n📦 By mail: We'll email you a prepaid label \nWhich option works best for you?"]
    ],
    [
        r"(.*)refund(.*)",
        ["Your refund will be processed in 3-5 business days after we receive your return - we know you'll appreciate the speedy service! 💸 Would you like me to track it for you once you've sent it back?",
         "We issue refunds super fast - typically within 3-5 days of getting your return! It will go back to your original payment method. Need help with anything else?"]
    ],
    [
        r"(.*)exchange(.*)",
        ["Exchanges are easy-peasy! 🎉 We can swap for a different size/color at no extra cost. Would you like me to check availability for your preferred option?",
         "Happy to process an exchange for you! The best part - no additional fees if done within 30 days. What would you like instead?"]
    ],
    [
        r"(.*)no receipt(.*)",
        ["No receipt? No problem! 😊 We can often look up purchases with your email or credit card. Alternatively, we may offer store credit. Want me to check your options?",
         "Don't worry if you can't find the receipt! We have multiple ways to help - could you tell me how you paid or provide your email address?"]
    ],
    [
        r"(.*)(broken|damaged)(.*)",
        ["Oh no! 😟 We're so sorry your item arrived damaged. The good news is we'll cover all return costs and get you a replacement or refund immediately. Could you share your order number so I can help faster?",
         "We hate when this happens! 😔 Please accept our apologies. Damaged items qualify for instant replacement - I'll personally make sure this gets resolved quickly for you."]
    ],
    [
        r"(.*)return label(.*)",
        ["I'd be happy to help with your return label! 🌟 You can print it directly from our website, or I can email you a prepaid label right now - which would you prefer?",
         "Return labels are my specialty! 🏷️ Would you like: \n1. A direct link to print your label \n2. An email with the label attached \n3. Help finding the label in your account?"]
    ],
    [
        r"(.*)late return(.*)",
        ["While our standard policy is 30 days, we always try to help! 😊 Let me check if we can make an exception - could you tell me why the return is late?",
         "We understand life gets busy! ⏳ While we can't guarantee late returns, I'm happy to submit a special request to our team. What's the reason for the delay?"]
    ],
    [
        r"(quit|bye|exit|goodbye)",
        ["Thank you for chatting! 💖 Remember, I'm always here if you need return help. Wishing you a wonderful day!",
         "It's been a pleasure helping! 🌟 Come back anytime for stress-free return assistance. Take care!",
         "Goodbye friend! 👋 Don't hesitate to return (pun intended 😉) if you need more help!"]
    ],
    [
        r"(.*)",
        ["I'd love to help with your return! 💕 Could you tell me more about what you need?",
         "Let's focus on making your return easy! 🌟 Could you rephrase your question?",
         "Returns are my specialty! 😊 How can I assist you today?"]
    ]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

def get_bot_response(user_input: str) -> str:
    """Get response from the NLTK rule-based chatbot."""
    return chatbot.respond(user_input)