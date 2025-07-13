from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes


# Ask user for mnemonic, use default if empty
default_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
mnemonic = input("Enter BIP39 mnemonic 12 or 24 words (leave empty for default): ").strip()
if not mnemonic:
    mnemonic = default_mnemonic

print(f"Using mnemonic: {mnemonic}")

# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Derive BIP44 account for Tron (coin type 195)
bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)
account = bip44_ctx.Purpose().Coin().Account(0)

# Derive the first address (m/44'/195'/0'/0/0)
address = bip44_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()
print("Tron address (m/44'/195'/0'/0/0):", address)

# Get xpub at account level (m/44'/195'/0')
xpub = account.PublicKey().ToExtended()


print("Tron xpub:", xpub)


# Ask user how many addresses to generate from xpub
try:
    count = int(input("How many Tron addresses to generate from xpub? (default 3): ").strip() or 3)
except ValueError:
    count = 3

# Create a Bip44 context from the xpub
pub_ctx = Bip44.FromExtendedKey(xpub, Bip44Coins.TRON)
print(f"First {count} Tron addresses from xpub (m/44'/195'/0'/0/i):")
for i in range(count):
    addr = pub_ctx.Change(Bip44Changes.CHAIN_EXT).AddressIndex(i).PublicKey().ToAddress()
    print(f"  Address {i}: {addr}")

