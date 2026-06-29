import random

adjectives = [
    # Sci-Fi & Cyberpunk
    "cosmic", "neon", "glitchy", "retro", "pixelated", "bionic", "glowing", 
    "quantum", "cyber", "holographic", "stellar", "radioactive", "interstellar",
    
    # Fantasy & Magic
    "mythic", "cursed", "enchanted", "shadowy", "ancient", "arcane", "celestial",
    "ethereal", "haunted", "alchemical", "phantom", "legendary", "spectral",
    
    # Moody & Aesthetic
    "lo-fi", "vaporwave", "gothic", "pastel", "minimalist", "surreal", "melancholic",
    "dreamy", "brutalist", "nostalgic", "psychedelic", "monochrome", "industrial",
    
    # Fun & Quirky
    "funky", "wobbly", "chaotic", "goofy", "chunky", "whimsical", "crunchy",
    "bizarre", "elastic", "magnetic", "kinetic", "clunky", "hyperactive"
]

nouns = [
    "song", "micro-game", "artwork", 
    "podcast episode", "zine", "clothing line", "animation", "website", 
    "comic strip", "ui design", "poetry collection", "3d-model", "app"
]

def generate_idea():
    r_a = random.choice(adjectives)
    r_n = random.choice(nouns)
    s_r_n = random.choice(nouns)

    # A single list of forbidden pairs makes the code much cleaner to read
    invalid_pairs = [
        ("podcast episode", "song"),
        ("song", "podcast episode"),
        ("song", "poetry collection"),
        ("micro-game", "zine"),
        ("ui design", "3d-model")
    ]
    #wording changes
    if (r_a == "pixelated" and r_n == "song") or (r_a == "pixelated" and s_r_n == "song"):
        r_a = "chiptune"

    # Keep picking a new secondary noun until ALL conditions are met
    while (s_r_n == r_n) or ((r_n, s_r_n) in invalid_pairs):
        s_r_n = random.choice(nouns)

    return f"Your next project: A {r_a} {r_n} {s_r_n}!"

print(generate_idea())