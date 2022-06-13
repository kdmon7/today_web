import React from "react";

import '../src/assets/scss/app.scss'
import { Route, Switch } from "react-router-dom";

import Home from "./pages/Home";
import Shop from "./pages/Shop";
import Login from "./pages/Login";
import Products from "./pages/Products";

function App() {
  return (
    <div className="App">
        <Switch>
          <Route path="/Home" component={Home}/>
          <Route path="/Shop" component={Shop}/>
          <Route path="/Login" component={Login}/>
          <Route path="/Products" component={Products}/>
        </Switch>
    </div>
  );
}

export default App;
