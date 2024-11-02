import random
import time

def invest_in_ghdog():
    print("🚀 Welcome to the GHDOG Coin Investment Simulator! 🚀")
    print("You're about to invest in the next big meme coin... GHDOG!")
    time.sleep(2)

# Starting "investment" and initial coin value
investment = 100  # starting with $100 investment
gh_dog_value = random.uniform(0.001, 0.01)  # GHDOG starts at a low price

# Simulate the market over time
print("\nInvesting $100 in GHDOG... Hold tight and watch the ride! 📈🐶")
time.sleep(2)

for day in range(1, 8):  # Simulate one week
    daily_change = random.uniform(-0.5, 5.0)  # GHDOG is volatile!
    gh_dog_value *= (1 + daily_change / 100)  # Daily percentage change

    # Calculate new investment value
    investment_value = investment * (gh_dog_value / 0.01)

    print(f"Day {day}: GHDOG value is ${gh_dog_value:.6f}")
    print(f"Your investment is now worth: ${investment_value:.2f}")
    time.sleep(1)

# Final outcome
print("\nEnd of the week! Checking your GHDOG fortune...")
time.sleep(2)

if investment_value >= 1000:
    print(f"🎉 Congratulations! Your GHDOG investment skyrocketed to ${investment_value:.2f}!")
    print("You're rich... thanks to GHDOG! 🐶💸")
elif investment_value > 100:
    print(f"Nice! Your GHDOG investment grew to ${investment_value:.2f}.")
    print("Not bad for a meme coin! 🐕💰")
else:
    print(f"Uh-oh! Your GHDOG investment shrank to ${investment_value:.2f}.")
    print("Meme coins... sometimes they bark, sometimes they bite. 🐾💔")
