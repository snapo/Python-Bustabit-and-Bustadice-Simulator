import binascii
import hashlib
import hmac
import math
import statistics
import time

# Define the starting object Hash
salt = b"0000000000000000004d6ec16dafe9d8370958664c1dc422f452892264c59526"
seed = "94809b699a42899197d863be47fe12fe15ae06bd481821c74b060868a7812260"
hashobj = hmac.new(salt, binascii.unhexlify(seed), hashlib.sha256)

numberslist = []
start = time.time()

# Generate 10,000,000 numbers
for i in range(10000000):
    intversion = int(hashobj.hexdigest()[0:int(52/4)], 16)
    X = 99 / (1 - (intversion / (2 ** 52)))
    number = max(1, math.floor(X) / 100)
    numberslist.append(number)
    seed = hashlib.sha256(seed.encode()).hexdigest()
    hashobj = hmac.new(salt, binascii.unhexlify(seed), hashlib.sha256)

end = time.time()

# Generate next 1000 draws for testing
test_draws = []
for i in range(1000):
    intversion = int(hashobj.hexdigest()[0:int(52/4)], 16)
    X = 99 / (1 - (intversion / (2 ** 52)))
    number = max(1, math.floor(X) / 100)
    test_draws.append(number)
    seed = hashlib.sha256(seed.encode()).hexdigest()
    hashobj = hmac.new(salt, binascii.unhexlify(seed), hashlib.sha256)

# Fixed strategy simulation
bankroll = 1000.0
fixed_multiplier = 1.5
bet_fraction = 0.01

stats = {
    'starting_bankroll': 1000.0,
    'final_bankroll': 0.0,
    'total_wins': 0,
    'total_losses': 0,
    'total_wagered': 0.0,
    'total_payout': 0.0,
    'net_profit': 0.0,
    'max_bankroll': 1000.0,
    'min_bankroll': 1000.0,
    'win_payouts': [],
    'loss_amounts': [],
    'bankroll_history': [1000.0]
}

# Run 1000 bets
for i, number in enumerate(test_draws):
    # Calculate bet amount (1% of current bankroll)
    bet_amount = bet_fraction * bankroll
    stats['total_wagered'] += bet_amount
    
    # Check if we win (drawn number >= multiplier)
    if number >= fixed_multiplier:
        # Calculate payout (bet * (multiplier - 1))
        payout = bet_amount * (fixed_multiplier - 1)
        bankroll += payout
        stats['total_wins'] += 1
        stats['total_payout'] += payout
        stats['win_payouts'].append(payout)
    else:
        bankroll -= bet_amount
        stats['total_losses'] += 1
        stats['loss_amounts'].append(bet_amount)
    
    # Update statistics
    stats['bankroll_history'].append(bankroll)
    stats['max_bankroll'] = max(stats['max_bankroll'], bankroll)
    stats['min_bankroll'] = min(stats['min_bankroll'], bankroll)

# Final calculations
stats['final_bankroll'] = bankroll
stats['net_profit'] = bankroll - stats['starting_bankroll']
stats['win_rate'] = stats['total_wins'] / 10  # Percentage
stats['expected_value'] = (stats['total_payout'] - sum(stats['loss_amounts'])) / stats['total_wagered']

# Print comprehensive results
print("================ FIXED STRATEGY RESULTS ================")
print(f"Starting Bankroll: ${stats['starting_bankroll']:.2f}")
print(f"Final Bankroll: ${stats['final_bankroll']:.2f}")
print(f"Net Profit: ${stats['net_profit']:.2f}")
print(f"Profit Margin: {(stats['net_profit']/stats['starting_bankroll'])*100:.2f}%")
print(f"\nGames Played: {len(test_draws)}")
print(f"Wins: {stats['total_wins']} ({stats['win_rate']:.1f}%)")
print(f"Losses: {stats['total_losses']} ({100 - stats['win_rate']:.1f}%)")
print(f"\nTotal Amount Wagered: ${stats['total_wagered']:.2f}")
print(f"Total Payout: ${stats['total_payout']:.2f}")
print(f"Total Losses: ${sum(stats['loss_amounts']):.2f}")
print(f"Expected Value per $ wagered: {stats['expected_value']:.4f}")

# Risk analysis
max_drawdown = (stats['max_bankroll'] - stats['min_bankroll']) / stats['max_bankroll'] * 100
print(f"\nMax Bankroll: ${stats['max_bankroll']:.2f}")
print(f"Min Bankroll: ${stats['min_bankroll']:.2f}")
print(f"Max Drawdown: {max_drawdown:.2f}%")

# Payout analysis
if stats['win_payouts']:
    avg_win = sum(stats['win_payouts']) / len(stats['win_payouts'])
    median_win = sorted(stats['win_payouts'])[len(stats['win_payouts']) // 2]
    print(f"\nAverage Win Amount: ${avg_win:.2f}")
    print(f"Median Win Amount: ${median_win:.2f}")
    print(f"Largest Win: ${max(stats['win_payouts']):.2f}")
else:
    print("\nNo wins recorded")

if stats['loss_amounts']:
    avg_loss = sum(stats['loss_amounts']) / len(stats['loss_amounts'])
    median_loss = sorted(stats['loss_amounts'])[len(stats['loss_amounts']) // 2]
    print(f"Average Loss Amount: ${avg_loss:.2f}")
    print(f"Median Loss Amount: ${median_loss:.2f}")
    print(f"Largest Loss: ${max(stats['loss_amounts']):.2f}")
else:
    print("No losses recorded")

# Performance metrics
growth_factor = stats['final_bankroll'] / stats['starting_bankroll']
print(f"\nBankroll Growth Factor: {growth_factor:.4f}x")
print(f"Compound Growth Rate: {(growth_factor ** (1/len(test_draws)) - 1) * 100:.4f}% per game")

# Initial dataset statistics
print("\n================ INITIAL DATA STATISTICS ================")
print(f"Generated 10,000,000 numbers in {end - start:.2f} seconds")
print(f"Highest Number: {max(numberslist)}")
print(f"Arithmetic Mean: {statistics.mean(numberslist):.4f}")
print(f"Harmonic Mean: {statistics.harmonic_mean(numberslist):.4f}")
print(f"Median: {statistics.median(numberslist):.4f}")
print(f"Test Draw Range: {min(test_draws)} - {max(test_draws)}")
print(f"Test Draw Mean: {statistics.mean(test_draws):.4f}")
print(f"Test Draw Win Probability (≥{fixed_multiplier}): {sum(1 for n in test_draws if n >= fixed_multiplier)/len(test_draws)*100:.2f}%")
print("=======================================================")
