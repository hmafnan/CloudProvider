import React from 'react';
import styled from "styled-components";

import CloudProviderList from "./components/CloudProviderList";
import Header from "./components/Header";

const BodyWrapper = styled.div`
    width: 900px;
    margin: 0 auto;
`;

const App = () => {
  const Providers = async () => {

  }
  return (
    <div className="App">
      <Header/>
      <BodyWrapper>
        <CloudProviderList/>
      </BodyWrapper>
    </div>
  );
}

export default App;
