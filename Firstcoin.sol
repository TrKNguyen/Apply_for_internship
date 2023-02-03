contract Firstcoin {
    address public minter;
    mapping(address => uint256) public balance;

    constructor() {
        minter = msg.sender;
    }

    event sent(address sender, address receiver, uint256 volume);

    function mint(address receiver, uint256 volume) public {
        require(msg.sender == minter && volume < 1e60);
        balance[receiver] += volume;
    }

    function transfer(address receiver, uint256 volume) public {
        address nw = msg.sender;
        require(balance[nw] >= volume, "Khong du tien de gui");
        balance[nw] -= volume;
        balance[receiver] += volume;
        emit sent(nw, receiver, volume);
    }
}
