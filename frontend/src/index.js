import React from "react";
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";

import './assets/scss/style.scss';

// pages for this product
//import Components from "./views/components/components.jsx";
import Header from "./components/header/header";
import App from "./App";
import { BrowserRouter } from "react-router-dom/cjs/react-router-dom.min";
ReactDOM.render(
    <React.StrictMode>
      <BrowserRouter>
        <Header />
        <App />
      </BrowserRouter>
    </React.StrictMode>,
    document.getElementById("root")
  );