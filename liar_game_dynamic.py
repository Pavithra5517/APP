
import random
import openai

# Replace with your own key or integrate securely
openai.api_key = "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"

categories = {
    "foods": [
    "sushi", "biryani", "ramen", "pizza", "kimchi",
    "tacos", "idli", "pasta", "pho", "butter chicken",
    "dumplings", "vada pav", "croissant", "momos", "fried rice",
    "bibimbap", "noodles", "paneer tikka", "hotdog", "burger",
    "pav bhaji", "malai kofta", "naan", "gimbap", "dal chawal"
],
    "everyday items": [
    "toothbrush", "toothpaste", "mobile phone", "pen", "notebook",
    "wallet", "keys", "water bottle", "earphones", "spectacles",
    "comb", "face mask", "hand sanitizer", "watch", "laptop",
    "charger", "umbrella", "hair tie", "scissors", "soap",
    "towel", "slippers", "backpack", "mirror", "nail cutter"
],
    "cartoon": [
    "Doraemon", "Shinchan", "Tom", "Jerry", "Nobita",
    "Scooby-Doo", "Ben 10", "Powerpuff Girls", "Dexter", "Johnny Bravo",
    "Phineas", "Ferb", "Candace", "Perry the Platypus", "SpongeBob",
    "Patrick Star", "Mr. Krabs", "Avatar Aang", "Zuko", "Toph",
    "Rick", "Morty", "Finn", "Jake", "Steven Universe"
],
    "kdramas": [
    "Goblin", "Itaewon Class", "Crash Landing on You", "Vincenzo", "True Beauty",
    "Business Proposal", "Extraordinary Attorney Woo", "The Glory", "Twenty-Five Twenty-One", "Weak Hero Class 1",
    "My Demon", "King the Land", "Castaway Diva", "Doctor Slump", "Lovely Runner",
    "Queen of Tears", "Marry My Husband", "A Time Called You", "Bloodhounds", "When Life Gives You Tangerines",
    "Undercover High School", "Resident Playbook", "Start-Up", "Hotel Del Luna", "Healer"
],
    "korean actors": [
    "Lee Min Ho", "Kim Soo Hyun", "Park Seo Joon", "Jung Il Woo", "Song Kang",
    "Ahn Hyo Seop", "Nam Joo Hyuk", "Ji Chang Wook", "Lee Jong Suk", "Choi Woo Shik",
    "Kim Seon Ho", "Park Hyung Sik", "Yoo Seung Ho", "Ryu Jun Yeol", "Woo Do Hwan",
    "Shin Hye Sun", "Kim Ji Eun", "Han So Hee", "Kim Tae Ri", "Go Youn Jung",
    "Park Bo Young", "Bae Suzy", "Kim Yoo Jung", "Jeon Yeo Been", "Kim Hye Yoon"
],
   "indian actors": [
    "Shah Rukh Khan", "Amitabh Bachchan", "Ranbir Kapoor", "Hrithik Roshan", "Salman Khan",
    "Aamir Khan", "Vijay", "Ajay Devgn", "Ranveer Singh", "Akshay Kumar",
    "Sidharth Malhotra", "Varun Dhawan", "Shahid Kapoor", "Vicky Kaushal", "Prabhas",
    "Rajinikanth", "Mammootty", "Dhanush", "Karthi", "Nivin Pauly",
    "Allu Arjun", "Mahesh Babu", "Naseeruddin Shah", "Irrfan Khan", "Rishi Kapoor",
    "Deepika Padukone", "Priyanka Chopra", "Alia Bhatt", "Kareena Kapoor", "Katrina Kaif"
],
   "kpop groups": [
    "TVXQ", "Super Junior", "Girls' Generation", "BIGBANG", "SHINee",
    "2NE1", "f(x)", "EXO", "Red Velvet", "GOT7",
    "TWICE", "BLACKPINK", "Seventeen", "MONSTA X", "Stray Kids",
    "ATEEZ", "TXT", "ITZY", "ENHYPEN", "Treasure",
    "LE SSERAFIM", "New Jeans", "Stray Kids", "Ive", "Kep1er", "(G)I-DLE",
    "BTS", "ENHYPEN"
]
}

personalities = [
    "I'm the logical one.",
    "I go with vibes, always.",
    "I read about this once!",
    "Not gonna lie, I'm not sure… or am I?"
]

def get_clue(word):
    prompt = f"Give a simple and short sentence to describe the word '{word}' without saying it directly."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "Some random guess. Who knows?"

def start_game():
    print("\nWelcome to the Liar Game!")

    print("\nCategories:", list(categories.keys()))
    category = input("Pick a category: ").strip().lower()
    while category not in categories:
        category = input("Invalid. Try again: ").strip().lower()

    mode = input("\nChoose mode (liar/fool): ").strip().lower()
    while mode not in ["liar", "fool"]:
        mode = input("Invalid. Choose either 'liar' or 'fool': ").strip().lower()

    word = random.choice(categories[category])
    fool_word = random.choice([w for w in categories[category] if w != word])
    ai_players = ["AI1", "AI2", "AI3"]
    liar_index = random.randint(0, 2)

    print("\nWord has been chosen!")

    clues = []
    for i, ai in enumerate(ai_players):
        personality = random.choice(personalities)
        if mode == "liar" and i == liar_index:
            clue = f"{ai} ({personality}): Umm... It might be green? Or soft? I forgot."
        elif mode == "fool" and i == liar_index:
            fake_clue = get_clue(fool_word)
            clue = f"{ai} ({personality}): {fake_clue}"
        else:
            true_clue = get_clue(word)
            clue = f"{ai} ({personality}): {true_clue}"
        clues.append(clue)

    print("\nHere are the clues:")
    for clue in clues:
        print(clue)

    guess = input("\nWho do you think is the liar/fool? (AI1/AI2/AI3): ").strip().upper()
    if guess == ai_players[liar_index]:
        print("\nCorrect! You caught the odd one out.")
    else:
        print(f"\nOops! It was actually {ai_players[liar_index]}.")

    print(f"The real word was: {word}")
    if mode == "fool":
        print(f"The fool got: {fool_word}")

start_game()
