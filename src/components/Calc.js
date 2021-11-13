import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

class Calc extends Component {
    constructor() {
      super()
  
      this.state = {
        bloodGlucose: '',
        carbs: ''
      }
    }

    changeHandler = e => {
      this.setState({
          [e.target.name]: e.target.value
      })
  }
  
    render() {
      return (
        <div>
          <form>
            <h1>What is this calculation for?</h1>
            <Button variant="outlined">Correction</Button>
            <Button variant="outlined">Meal</Button>
            <h1>What is your current Blood Glucose?</h1>
            <TextField  type='text'
                        placeholder='120 mg/dL'
                        name='bsLow'
                        value={this.state.bloodGlucose}
                        onChange={this.changeHandler}/>
            <h1>What is the total amount of carbs in your meal?</h1>
            <TextField  type='text'
                        placeholder='____ grams'
                        name='carbs'
                        value={this.state.carbs}
                        onChange={this.changeHandler}/>
            <Button variant="contained" type='submit'>DONE</Button>
          </form>
        </div>
      )
    }
  }

export default Calc