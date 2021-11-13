import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import calculator from '../images/calculator.svg';
import { Link } from 'react-router-dom';

class Calc extends Component {
    constructor() {
      super()
  
      this.state = {
        bloodGlucose: '',
        carbs: '',
        meal: true
      }
    }

    changeHandler = e => {
      this.setState({
          [e.target.name]: e.target.value
      })
  }
  
  toggleMealOn = () => {
    this.setState({
      meal: true
    })
  }

  toggleMealOff = () => {
    this.setState({
      meal: false
    })
  }
  
    render() {
      return (
        <div>
          <img className='calculator' src={ calculator } alt='calculator'/>
          { this.state.meal ? 
          <form>
            <h1>What is this calculation for?</h1>
            <Button variant="outlined" onClick={ this.toggleMealOn }>Meal</Button>
            <Button variant="outlined" onClick={ this.toggleMealOff }>Correction</Button>
            <h1>What is your current Blood Glucose?</h1>
            <TextField  type='text'
                        placeholder='120 mg/dL'
                        name='bsLow'
                        value={this.state.bloodGlucose}
                        onChange={this.changeHandler}
                        style={{width: '350px'}}/>
            <h1>What is the total amount of carbs in your meal?</h1>
            <TextField  type='text'
                        placeholder='____ grams'
                        name='carbs'
                        value={this.state.carbs}
                        onChange={this.changeHandler}
                        style={{width: '350px'}}/>
          </form>
          :
          <form>
            <h1>What is this calculation for?</h1>
            <Button variant="outlined" onClick={ this.toggleMealOn }>Meal</Button>
            <Button variant="outlined" onClick={ this.toggleMealOff }>Correction</Button>
            <h1>What is your current Blood Glucose?</h1>
            <TextField  type='text'
                        placeholder='120 mg/dL'
                        name='bsLow'
                        value={this.state.bloodGlucose}
                        onChange={this.changeHandler}/>
          </form>
        }
        <Link to='/'><Button variant="contained" type='submit'>DONE</Button></Link>
        </div>
      )
    }
  }

export default Calc