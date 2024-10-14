# Joseph Townsend
# P5HW
# 10/2/2024
# Create a game using loops, functions, and module import


# Import random function
import random

# Define a function to create a character
def create_character():
    print()
    user_name = input("Enter the character's name: ")
    health_points = int(input("Enter the character's health points: "))
    items = input("Enter the character's items (comma-separated): ").split(',')

    # Strip any extra whitespace from the item names
    items = [item.strip() for item in items]

    character = {
        'user_name': user_name,
        'health_points': health_points,
        'items': items
    }

    return character

# Create a non-value returning function    
def display_characters(char_list):
    for char in char_list:
        print(char)  # Print the character dictionary

def simulate_battle(character1, character2):
    if not character1['items'] or not character2['items']:
        print("One of the characters has no items to use.")
        return character1, character2

    # Randomly select an item to use from character1's items
    item_used = random.choice(character1['items'])
    # Randomly determine the effect on health (set to -130 to 130)
    health_effect = random.randint(-100, 100)

    # Apply the health effect to character2
    character2['health_points'] += health_effect

    # Log the action
    print()
    print(f"{character1['user_name']} uses {item_used} on {character2['user_name']}!")
    print(f"It {'increased' if health_effect > 0 else 'decreased'} {character2['user_name']}'s health by {abs(health_effect)}.")

    # Ensure health does not go below zero
    character2['health_points'] = max(0, character2['health_points'])

    return character1, character2

# Creates a function that displays character's values
def display_character(char):
    # Using a for loop to print key-value pairs
    for key, value in char.items():
        print(f'{key}: {value}')

# Creates a function that determines the win condition
def check_victory(character1, character2):
    if character1['health_points'] <= 0:
        print(f"{character2['user_name']} defeated {character1['user_name']} and {character2['user_name']} wins!")
        return True
    elif character2['health_points'] <= 0:
        print(f"{character1['user_name']} defeated {character2['user_name']} and {character1['user_name']} wins!")
        return True
    return False

    # Print one character's attributes
    display_character(char1)
    print("-*-VERSUS-*-")
    display_character(char2)

# Example of how to use the function
if __name__ == "__main__":
    # Create a list
    char_list = []

    # Create 2 characters within a list
    char1 = create_character()
    char2 = create_character()
    char_list.append(char1)
    char_list.append(char2)

    # Call function to attack
    updated_character_a, updated_character_b = simulate_battle(char1, char2)

    # Check if either character has won
    if not check_victory(updated_character_a, updated_character_b):
        print("Both characters are still standing!")
    
    # Display all characters (changed it to print using the dictionary instead indvidually)
    display_characters(char_list)
# Call function to attack
    updated_character_a, updated_character_b = simulate_battle(char1, char2)

    # Check if either character has won
    if not check_victory(updated_character_a, updated_character_b):
        print("Both characters are still standing!")
    
    # Display all characters (changed it to print using the dictionary instead indvidually)
    display_characters(char_list)
