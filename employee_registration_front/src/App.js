import logo from './logo.svg';
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom'
import './App.css';
import  Home from './Components/Home'
import Department from './Components/Department'
import Employee from './Components/Employee'
import Navigation from './Components/Navigation'

function App() {
  return (
    <Router>
      <div className="App">
        <h3>Employee Management Software</h3>
        <Navigation />

        <Switch>
          <Route path="/" exact>
            <Home />
          </Route>
          <Route path="/Department">
            <Department />
          </Route>
          <Route path="/Employee">
            <Employee />
          </Route>
        </Switch>

      </div>
    </Router>
  );
}

export default App;
