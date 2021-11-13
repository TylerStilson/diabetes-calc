import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/Home'
import Settings from './components/Settings'
import Calc from './components/Calc'
import './styles/App.css'
import './styles/reset.css'

function App() {
  return (
    <Router>
        <div>
          <Switch>
              <Route exact path='/' component={ Home } />
              <Route path='/Settings' component={ Settings } />
              <Route path='/Calc' component={ Calc } />
          </Switch>
        </div>
      </Router>
  );
}

export default App;
