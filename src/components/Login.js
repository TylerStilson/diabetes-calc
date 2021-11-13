import React, { Component } from 'react'
import axios from 'axios'

class Login extends Component {
    constructor() {
      super()
  
      this.state = {
        email: '',
        password: '',
        f_name: '',
        c_password: ''
      }
    }

    changeHandler = e => {
      this.setState({
          [e.target.name]: e.target.value
      })
  }

    register = async (e) => {
      e.preventDefault()
      const { f_name, email, password, c_password} = this.state
      try {
        const user = await axios.post('api/auth/register', { f_name, email, password, c_password })
        this.props.loginUser(user.data)
        this.props.history.push('/status')
      }
      catch {
        alert('Failed Registration Attempt')
      }
    }

  
    render() {
      return (
        <div>
            <div id="loginHead">
              <h1>Welcome to Calc!</h1>
              <h3>Diabetes Management Made Easy.</h3>
            </div>
            <form onSubmit={ this.register}>
              <input  
                type='text'
                className='input-field'
                autoComplete='off'
                placeholder='First Name'
                name='f_name'
                value={this.state.f_name}
                onChange={this.changeHandler}/>

              <input  
                type='text'
                className='input-field'
                autoComplete='off'
                placeholder='Email'
                name='email'
                value={this.state.email}
                onChange={this.changeHandler}/>

              <input  
                type='text'
                className='input-field'
                autoComplete='off'
                placeholder='Password'
                name='password'
                value={this.state.password}
                onChange={this.changeHandler}/>

              <input  
                type='text'
                className='input-field'
                autoComplete='off'
                placeholder='Confirm Password'
                name='con_password'
                value={this.state.c_password}
                onChange={this.changeHandler}/>

              <input  
                type='submit'
                className='submit-field'
                value="Submit"
                />

            </form>
            <div>

            </div>

          
        </div>
        
      )
    }
  }

export default Login
