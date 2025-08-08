from web3 import Web3

def check_eth_balance(wallet_address):
    INFURA_URL = "https://mainnet.infura.io/v3/a2f93247c1074618a73a0f4a6bd9c9a3"
    THRESHOLD_AMOUNT = 0.01  # Eşik: 0.01 ETH
    
    try:
        w3 = Web3(Web3.HTTPProvider(INFURA_URL))
        
        if not w3.is_connected():
            return False
        balance_wei = w3.eth.get_balance(Web3.to_checksum_address(wallet_address))
        balance_eth = w3.from_wei(balance_wei, 'ether')
        
        return float(balance_eth) >= THRESHOLD_AMOUNT
        
    except Exception as e:
        return False

def main(wallet_address):
    return check_eth_balance(wallet_address)

if __name__ == "__main__":
    print("\n===Belirtilen ETH cüzdanındaki bakiyenin 0.01 ETH'den yüksek olup olmadığı değerini döndürür===\n")
    wallet_address = input("ETH cüzdan adresini girin: ").strip()
    
    if not wallet_address:
        print("Geçerli bir cüzdan adresi giriniz!")
    else:
        result = main(wallet_address)
        print(result) 