from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, how can I assist you with your return today?",
         "Hi %2! Do you need help with a return or exchange?",
         "%2, thank you for reaching out about your return."]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you with returns, refunds, and exchanges. What do you need?",
         "Sure! Our return policy allows returns within 30 days. Do you have a specific question?",
         "How can I assist you with your return today?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm your Return Assistant Bot. How can I help with your return?",
         "You can call me ReturnBot! I specialize in return policies.",
         "I'm here to help with returns—what do you need?"]
    ],
    [
        r"how are you (.*) ?",
        ["I'm here and ready to assist with your return!",
         "Doing great! Let me help you process your return smoothly."]
    ],
    [
        r"sorry (.*)",
        ["No worries! Let’s get your return sorted.",
         "It’s okay—I’m here to help. What’s your return concern?"]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Glad to hear it! How can I assist with your return today?",
         "Great! Do you have a return request?"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello! Need help with a return or refund?",
         "Hi there! Our return window is 30 days. How can I help?"]
    ],
    [
        r"what (.*) want ?",
        ["I want to help you with your return! What’s your issue?",
         "I’m here to assist with returns—what do you need?"]
    ],
    [
        r"(.*)created(.*)",
        ["I was designed to help customers with returns and refunds.",
         "My purpose is to assist with return policies. How can I help?"]
    ],
    [
        r"(.*) (location|city) ?",
        ["We process returns from all locations. Where are you returning from?",
         "Our returns center is in Texas, but we accept returns nationwide."]
    ],
    [
        r"(.*)raining in (.*)",
        ["No weather issues here! How can I assist with your return?",
         "Let’s focus on your return—what do you need help with?"]
    ],
    [
        r"how (.*) health (.*)",
        ["I’m always operational to help with returns!",
         "No health issues here—ready to process your return!"]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I’m focused on returns, but I hope your team wins! How can I help with your return?"]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["I specialize in returns—can I assist with yours?"]
    ],
    # ===== **RETURN POLICY-SPECIFIC RESPONSES** =====
    [
        r"(.*)return policy(.*)",
        ["Our return policy allows returns within **30 days** of purchase. Items must be unused and in original packaging.",
         "You can return most items within 30 days with a receipt. Need help processing one?",
         "Returns accepted within 30 days for a full refund. Exclusions may apply."]
    ],
    [
        r"(.*)how to return(.*)",
        ["You can start a return online via our website or visit a store. Would you like a step-by-step guide?",
         "1. Log into your account 2. Go to 'Orders' 3. Select 'Return Item' 4. Print the label. Need more details?"]
    ],
    [
        r"(.*)refund(.*)",
        ["Refunds are processed within **3-5 business days** after we receive your return.",
         "Once we get your return, your refund will be issued to your original payment method."]
    ],
    [
        r"(.*)exchange(.*)",
        ["We offer exchanges for the same item in a different size/color. Would you like to proceed?",
         "Exchanges are free if initiated within 30 days. Need help with one?"]
    ],
    [
        r"(.*)no receipt(.*)",
        ["Without a receipt, we may offer store credit at the current selling price.",
         "Do you have the credit card used for purchase? We can look it up!"]
    ],
    [
        r"(.*)broken(.*)|(.*)damaged(.*)",
        ["If your item arrived damaged, we’ll cover return shipping. Please contact us with order details.",
         "We apologize! Damaged items qualify for a free replacement or refund."]
    ],
    [
        r"(.*)return label(.*)",
        ["You can print a return label from our website under 'Order History'. Need a direct link?",
         "We’ll email you a prepaid return label if eligible. Check your inbox!"]
    ],
    [
        r"(.*)late return(.*)",
        ["Returns after 30 days may not qualify for a refund, but we can check for exceptions.",
         "Contact our support team—they might approve a late return as a courtesy."]
    ],
    [
        r"(quit|bye|exit)",
        ["Thank you for chatting! Visit our Returns page for more help.",
         "Have a great day! Reach out if you need more return assistance."]
    ],
    [
        r"(.*)",
        ["I’m here to help with returns—could you clarify your question?",
         "For return-related questions, visit our Returns FAQ or ask me directly!"]
    ],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

def get_bot_response(user_input: str) -> str:
    """Get response from the NLTK rule-based chatbot."""
    return chatbot.respond(user_input)