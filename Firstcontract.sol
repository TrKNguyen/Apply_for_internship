//pragma solidity >=7.0.0 <9.0.0


contract firstcontract {
    uint public data; 
    function set(uint x) public {
        data = x;
    }
    function get() public view returns (uint x)
    {
        return data;
    }
}