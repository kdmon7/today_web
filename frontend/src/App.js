import logo from './logo.svg';
import './App.css';
import { BrowserView, MobileView } from 'react-device-detect';

<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
/>

function App() {
  return (
    <div className="App">
      <BrowserView>
        PC버전 테스트
      </BrowserView>
      <MobileView>
        모바일버전 테스트
      </MobileView>
    </div>
  );
}

export default App;
