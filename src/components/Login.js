import React, { Component } from 'react'

class Login extends Component {
    constructor() {
      super()
  
      this.state = {
        email: '',
        password: ''
      }
    }
  
    render() {
      return (
        <div>
          <h1>This is an example class component to show off the component did mount hook</h1>
        </div>
      )
    }
  }

export default Login