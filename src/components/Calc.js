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
        meal: true,
        result: ''
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
        <main>
          
          <h1 className='h4'>7 units</h1>
          
          <img className='calculator' src={ calculator } alt='calculator'/>
          { this.state.meal ? 
          <form className='form2'>
            <h1 className='h3'>What is this calculation for?</h1>
            <div className='buttonO'>
              <Button className='meal' variant="outlined" onClick={ this.toggleMealOn }>Meal</Button>
              <Button className='corr' variant="outlined" onClick={ this.toggleMealOff }>Correction</Button>
            </div>
            <h1 className='h3'>What is your current Blood Glucose?</h1>
            <TextField  type='text'
                        placeholder='120 mg/dL'
                        name='bsLow'
                        value={this.state.bloodGlucose}
                        onChange={this.changeHandler}
                        style={{width: '350px'}}/>
            <h1 className='h3'>What is the total amount of carbs in your meal?</h1>
            <TextField  type='text'
                        placeholder='____ grams'
                        name='carbs'
                        value={this.state.carbs}
                        onChange={this.changeHandler}
                        style={{width: '350px'}}/>
          </form>
          :
          <form>
            <h1 className='h3'>What is this calculation for?</h1>
            <div className='buttonO'>
              <Button className='meal' variant="outlined" onClick={ this.toggleMealOn }>Meal</Button>
              <Button className='corr' variant="outlined" onClick={ this.toggleMealOff }>Correction</Button>
            </div>
            <h1 className='h3'>What is your current Blood Glucose?</h1>
            <TextField  type='text'
                        placeholder='120 mg/dL'
                        name='bsLow'
                        value={this.state.bloodGlucose}
                        onChange={this.changeHandler}/>
          </form>
        }
        <div className='space'> </div>
        <Link to='/'><Button className='saveB' variant="contained" type='submit' onClick={ this.showTotal }>DONE</Button></Link>
        <div className='space'> </div>
        </main>
      )
    }
  }

export default Calc
