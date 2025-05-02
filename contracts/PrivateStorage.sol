// SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

import "./MpcCore.sol";

contract PrivateStorage {
    ctUint64 public privateNumber;

    constructor() {}

    function setPrivateNumber(itUint64 calldata value) external {
        gtUint64 gtNumber = MpcCore.validateCiphertext(value);

        privateNumber = MpcCore.offBoardToUser(gtNumber, msg.sender);
    }
}