"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

import datetime

def generate_bio(name: str, profession: str, passion: str, emoji: str, website: str, style: str) -> str:
    """Core Utility: Accepts cleaned inputs and maps them to a layout design."""
    if style == "1":
        return f"{emoji} {name} | {profession}\n💡 {passion}\n🔗 {website}"
    elif style == "2":
        return f"{emoji} {name}\n🚀 {profession}\n🔥 {passion}\n🌐 {website}"
    elif style == "3":
        edge = emoji * 4
        return f"{edge}\n✨ {name}\n💼 {profession}\n📝 {passion}\n🔗 {website}\n{edge}"
    else:
        # Safety net fallback
        return f"{emoji} {name} | {profession}\n💡 {passion}\n🔗 {website}"

def main():
    print("--- 📱 SOCIAL MEDIA BIO GENERATOR 📱 ---\n")
    
    # 1. Gather & Clean Inputs with smart defaults
    name = input("Enter your name: ").strip().title()
    profession = input("Enter your profession: ").strip().title()
    passion = input("Enter your passion in one line: ").strip()
    
    emoji = input("Enter your favorite emoji (Press Enter for 🚀): ").strip() or "🚀"
    website = input("Enter your website/handle (Press Enter to skip): ").strip() or "linkin.bio/me"

    # 2. Bulletproof Menu Selection Loop
    print("\nChoose your style:")
    print("1. Simple & Clean Lines")
    print("2. Professional Stack")
    print("3. Emoji Border Sandwich")
    
    while True:
        style = input("Enter 1, 2 or 3: ").strip()
        if style in ["1", "2", "3"]:
            break
        print("❌ Invalid selection. Choose 1, 2, or 3.")

    # 3. Generate the Bio Core Data
    bio = generate_bio(name, profession, passion, emoji, website, style)

    # 4. Display Card with Auto-Sizing Box Frame
    lines = bio.split("\n")
    max_len = max(len(line) for line in lines)
    horizontal_border = "━" * (max_len + 4)

    print("\nYour Stylish Bio Blueprint:\n")
    print(f"┏{horizontal_border}┓")
    for line in lines:
        print(f"┃  {line.ljust(max_len)}  ┃")
    print(f"┗{horizontal_border}┛\n")

    # 5. File System Exporter
    save = input("💾 Save bio to a text file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"{name.lower().replace(' ', '_')}_bio.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(bio)
            f.write(f"\n\n[Generated on: {datetime.date.today().isoformat()}]")
        print(f"✨ Success! File saved cleanly as '{filename}'")

# Runs the program only if this specific file is executed directly
if __name__ == "__main__":
    main()