import React from "react";
import styled from "styled-components";

const HeaderWrapper = styled.div`
    background-color: #f94f4c;
    color: white;
    height: 55px;
    padding: 8px;
`;

const LogoWrapper = styled.div`
    float: left;
    width: 150px;
    margin-left: 30px;
`;


const Header = () => {
    return (
        <HeaderWrapper>
            <LogoWrapper>
                <a href="#">
                    <img alt="Aiven Logo" width="150" height="35"
                         src="https://downloads.intercomcdn.com/i/o/7690/99852eb0cd241b1697669055/aiven-logo-rgb-nega.png" />
                </a>
            </LogoWrapper>
            <ul className="nav">
                <li className="nav-item">
                    <a className="nav-link active" aria-current="page" href="#" style={{color:'white'}}>Home</a>
                </li>
            </ul>
        </HeaderWrapper>
    )
}

export default Header;