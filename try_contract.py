from pyetheroll.constants import ChainID
from pyetheroll.etheroll import Etheroll

chain_id = ChainID.ROPSTEN
contract_address = '0xE34bAa928370b68Ebc16384795d148c1E04b4a5B'
#contract_address = '0xe12c6dEb59f37011d2D9FdeC77A6f1A8f3B8B1e8'

etheroll = Etheroll(chain_id, contract_address)