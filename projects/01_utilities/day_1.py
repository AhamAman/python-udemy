"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""
import datetime


# --- THIS IS YOUR UTILITY FUNCTION ---
def generate_profile_card(name: str, age: str, city: str, profession: str, hobby: str) -> str:
    """Takes user details and returns a beautifully framed introduction card."""
    
    # 1. Format the text
    intro = (
        f"Hello! My name is {name.title().strip()}. I'm {age.strip()} years old and live in {city.title().strip()}.\n"
        f"I work as a {profession.title().strip()} and I absolutely enjoy {hobby.strip()} in my free time.\n"
        f"Nice to meet you!\n\n"
        f"Logged on: {datetime.date.today().isoformat()}"
    )
    
    # 2. Build the dynamic frame
    lines = intro.split('\n')
    max_len = max(len(line) for line in lines)
    border = "*" * (max_len + 2)
    
    # 3. Assemble the card
    card = f"{border}\n"
    for line in lines:
        # Ljust(max_len) ensures all lines have the exact same width inside the box
        card += f"{line.ljust(max_len)}\n"
    card += border
    
    return card

# --- THIS IS YOUR MAIN APPLICATION ---
if __name__ == "__main__":
    # Gather inputs
    u_name = input("Name: ")
    u_age = input("Age: ")
    u_city = input("City: ")
    u_prof = input("Profession: ")
    u_hobby = input("Hobby: ")
    
    # Use the utility
    final_card = generate_profile_card(u_name, u_age, u_city, u_prof, u_hobby)
    print("\n" + final_card)