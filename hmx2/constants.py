# ------ Pyth Network ------
DEFAULT_PYTH_PRICE_SERVICE_URL = "https://xc-mainnet.pyth.network"

# ------ Contract Address ------
MULTICALL_ADDRESS = "0xcA11bde05977b3631167028862bE2a173976CA11"
CROSS_MARGIN_HANDLER_ADDRESS = "0xB189532c581afB4Fbe69aF6dC3CD36769525d446"
LIMIT_TRADE_HANDLER_ADDRESS = "0xeE116128b9AAAdBcd1f7C18608C5114f594cf5D6"
VAULT_STORAGE_ADDRESS = "0x56CC5A9c0788e674f17F7555dC8D3e2F1C0313C0"
GLP_MANAGER_ADDRESS = "0x3963FfC9dff443c2A94f21b129D429891E32ec18"
PERP_STORAGE_ADDRESS = "0x97e94BdA44a2Df784Ab6535aaE2D62EFC6D2e303"
CONFIG_STORAGE_ADDRESS = "0xF4F7123fFe42c4C90A4bCDD2317D397E0B7d7cc0"

# ------ ABI Path ------
ERC20_ABI_PATH = "abis/ERC20.json"
CROSS_MARGIN_HANDLER_ABI_PATH = "abis/CrossMarginHandler.json"
LIMIT_TRADE_HANDLER_ABI_PATH = "abis/LimitTradeHandler.json"
VAULT_STORAGE_ABI_PATH = "abis/VaultStorage.json"
GLP_MANAGER_ABI_PATH = "abis/GlpManager.json"
PERP_STORAGE_ABI_PATH = "abis/PerpStorage.json"
CONFIG_STORAGE_ABI_PATH = "abis/ConfigStorage.json"

# ------ Market ------
MARKET_ETH_USD = 0
MARKET_BTC_USD = 1
MARKET_AAPL_USD = 2
MARKET_JPY_USD = 3
MARKET_XAU_USD = 4
MARKET_AMZN_USD = 5
MARKET_MSFT_USD = 6
MARKET_TSLA_USD = 7
MARKET_EUR_USD = 8
MARKET_XAG_USD = 9
MARKET_AUD_USD = 10
MARKET_GBP_USD = 11
MARKET_ADA_USD = 12
MARKET_MATIC_USD = 13
MARKET_SUI_USD = 14
MARKET_ARB_USD = 15
MARKET_OP_USD = 16
MARKET_LTC_USD = 17
MARKET_COIN_USD = 18
MARKET_GOOG_USD = 19
MARKET_BNB_USD = 20
MARKET_SOL_USD = 21
MARKET_QQQ_USD = 22
MARKET_XRP_USD = 23

# ------ Token Profiles ------
TOKEN_PROFILE = {
  "USDC.e": {
    "symbol": "USDC.e",
    "address": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
    "decimals": 6
  },
  "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8": {
    "symbol": "USDC.e",
    "address": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
    "decimals": 6
  },
  "USDT": {
    "symbol": "USDT",
    "address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
    "decimals": 6
  },
  "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9": {
    "symbol": "USDT",
    "address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
    "decimals": 6
  },
  "DAI": {
    "symbol": "DAI",
    "address": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
    "decimals": 18
  },
  "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1": {
    "symbol": "DAI",
    "address": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
    "decimals": 18
  },
  "WETH": {
    "symbol": "WETH",
    "address": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    "decimals": 18
  },
  "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1": {
    "symbol": "WETH",
    "address": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    "decimals": 18
  },
  "WBTC": {
    "symbol": "WBTC",
    "address": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
    "decimals": 8
  },
  "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f": {
    "symbol": "WBTC",
    "address": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
    "decimals": 8
  },
  "sGLP": {
    "symbol": "sGLP",
    "address": "0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf",
    "decimals": 18
  },
  "0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf": {
    "symbol": "sGLP",
    "address": "0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf",
    "decimals": 18
  },
  "ARB": {
    "symbol": "ARB",
    "address": "0x912CE59144191C1204E64559FE8253a0e49E6548",
    "decimals": 18
  },
  "0x912CE59144191C1204E64559FE8253a0e49E6548": {
    "symbol": "ARB",
    "address": "0x912CE59144191C1204E64559FE8253a0e49E6548",
    "decimals": 18
  }
}

# ------ Collaterals ------
COLLATERAL_USDCe = TOKEN_PROFILE["USDC.e"]["address"]
COLLATERAL_USDT = TOKEN_PROFILE["USDT"]["address"]
COLLATERAL_DAI = TOKEN_PROFILE["DAI"]["address"]
COLLATERAL_WETH = TOKEN_PROFILE["WETH"]["address"]
COLLATERAL_WBTC = TOKEN_PROFILE["WBTC"]["address"]
COLLATERAL_sGLP = TOKEN_PROFILE["sGLP"]["address"]
COLLATERAL_ARB = TOKEN_PROFILE["ARB"]["address"]

COLLATERALS = [COLLATERAL_USDCe, COLLATERAL_USDT, COLLATERAL_DAI,
               COLLATERAL_WETH, COLLATERAL_WBTC, COLLATERAL_sGLP, COLLATERAL_ARB]

# ------ Assets ------
ASSET_ETH = "ETH"
ASSET_BTC = "BTC"
ASSET_AAPL = "AAPL"
ASSET_JPY = "JPY"
ASSET_XAU = "XAU"
ASSET_AMZN = "AMZN"
ASSET_MSFT = "MSFT"
ASSET_TSLA = "TSLA"
ASSET_EUR = "EUR"
ASSET_XAG = "XAG"
ASSET_AUD = "AUD"
ASSET_GBP = "GBP"
ASSET_ADA = "ADA"
ASSET_MATIC = "MATIC"
ASSET_SUI = "SUI"
ASSET_ARB = "ARB"
ASSET_OP = "OP"
ASSET_LTC = "LTC"
ASSET_COIN = "COIN"
ASSET_GOOG = "GOOG"
ASSET_BNB = "BNB"
ASSET_SOL = "SOL"
ASSET_QQQ = "QQQ"
ASSET_XRP = "XRP"
ASSET_USDC = "USDC"
ASSET_USDT = "USDT"
ASSET_DAI = "DAI"
ASSET_GLP = "GLP"

ASSETS = [ASSET_ETH, ASSET_BTC, ASSET_AAPL, ASSET_JPY, ASSET_XAU, ASSET_AMZN,
          ASSET_MSFT, ASSET_TSLA, ASSET_EUR, ASSET_XAG, ASSET_AUD, ASSET_GBP,
          ASSET_ADA, ASSET_MATIC, ASSET_SUI, ASSET_ARB, ASSET_OP, ASSET_LTC,
          ASSET_COIN, ASSET_GOOG, ASSET_BNB, ASSET_SOL, ASSET_QQQ, ASSET_XRP,
          ASSET_USDC, ASSET_USDT, ASSET_DAI, ASSET_GLP]

# ------ Asset IDs Map ----
COLLATERAL_ASSET_ID_MAP = {
  COLLATERAL_USDCe: ASSET_USDC,
  COLLATERAL_USDT: ASSET_USDT,
  COLLATERAL_DAI: ASSET_DAI,
  COLLATERAL_WETH: ASSET_ETH,
  COLLATERAL_WBTC: ASSET_BTC,
  COLLATERAL_sGLP: ASSET_GLP,
  COLLATERAL_ARB: ASSET_ARB
}

# Address
ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"

# Math
MAX_UINT = 2 ** 256 - 1
BPS = 10000

EXECUTION_FEE = 3 * 10 ** 14

SECONDS = 1
MINUTES = 60
HOURS = 3600
DAYS = 86400
YEARS = 31536000