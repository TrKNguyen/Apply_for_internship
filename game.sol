contract game {
    tk[] public players;
    mapping(address => tk) public players1;
    int256 public cnt = 0;
    enum level {
        ngucap1,
        ngucap2,
        ngucap3
    }
    struct tk {
        address ad_players;
        string name;
        level levelplayer;
        int256 age;
        string sex;
        uint256 timecreate;
    }

    function add(
        string memory fullname,
        int256 age,
        string memory sex
    ) public {
        players.push(
            tk(msg.sender, fullname, level.ngucap1, age, sex, block.timestamp)
        );
        players1[msg.sender] = tk(
            msg.sender,
            fullname,
            level.ngucap1,
            age,
            sex,
            block.timestamp
        );
        cnt++;
    }

    function changelevel(address x) public {
        if (players1[x].timecreate + 150 <= block.timestamp)
            players1[x].levelplayer = level.ngucap2;
    }
}
