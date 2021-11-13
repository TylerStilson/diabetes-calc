import React, { Component } from 'react'
import logo from '../images/logo.svg'
import calc from '../images/calc.svg'
import { Link } from 'react-router-dom'
import Button from '@mui/material/Button';

class Home extends Component {
    constructor() {
      super()
  
      this.state = {
        email: '',
        password: ''
      }
    }
  
    render() {
      return (
        <div className='main'>
            <img className='logo' src={ calc } alt='calc'/>
            <h1>Welcome to Calc!</h1>
            <h2>Diabetes Management Made Easy.</h2>
            <Link to='/Calc'><Button variant="contained">BOLUS CALCULATION</Button></Link>
            <Link to='/Settings'><Button variant="outlined">CALCULATION SETTINGS</Button></Link>
            <img className='logo' src={ logo } alt='logo'/>
        </div>
      )
    }
  }

export default Home