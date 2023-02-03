contract Auction {
    address public highestBidder;
    uint256 public highestBid = 0;
    bool ended = false;
    uint256 Auctionendtime;
    mapping(address => uint256) public pendingReturns;
    address payable public benificiary;
    event highestBidchange(address bidder, uint256 amount);
    event Auctionend(address winner, uint256 amount);

    constructor(uint256 timelength, address payable _benificiary) {
        Auctionendtime = block.timestamp + timelength;
        benificiary = _benificiary;
    }

    function bid() public payable {
        require(Auctionendtime >= block.timestamp, "Het thoi gian dau gia");
        require(
            msg.value > highestBid,
            "So tien ban dua ra khong lon hon gia cao nhat"
        );
        highestBidder = msg.sender;
        highestBid = msg.value;
        pendingReturns[highestBidder] += highestBid;
        emit highestBidchange(highestBidder, highestBid);
    }

    function withdraw() public returns (bool) {
        uint256 p = pendingReturns[msg.sender];
        require(
            msg.sender != highestBidder,
            "Dang nam giu gia cao nhat khong duoc rut"
        );
        if (!payable(msg.sender).send(p)) {
            return false;
        }
        pendingReturns[msg.sender] = 0;
        return true;
    }

    function auctionEnd() public {
        require(!ended, "Phien dau gia da duoc ket thuc");
        require(block.timestamp > Auctionendtime, "Chua het thoi gian dau gia");
        ended = true;
        benificiary.transfer(highestBid);
        emit Auctionend(highestBidder, highestBid);
    }
}
