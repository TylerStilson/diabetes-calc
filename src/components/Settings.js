import React, { Component } from 'react';
import setting from '../images/setting.svg';
import Button from '@mui/material/Button';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';
import { Link } from 'react-router-dom';
import calc from '../images/calc.svg'

class Settings extends Component {
    constructor() {
        super()

        this.state = {
            glucose: '',
            correctionFactor: '',
            carbRatio: '',
            precision: ''
        }
    }    

    changeHandler = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    render() {
        return (
            <div className='main'>
                
                <img className='logo2' src={ calc } alt='calc'/>
                <form className='form' onSubmit={ this.calculate }>
                    <h1 className='h1'>Calculation Settings</h1>
                    <h2 className='h2'>These settings will be used to calculate your bolus.</h2>
                    <img className='setting' src={ setting } alt='setting'/>
                    <h2 className='h3'>What is your target blood glucose?</h2>
                    <TextField  type='text'
                                placeholder='120 mg/dL'
                                name='glucose'
                                value={this.state.glucose}
                                onChange={this.changeHandler}
                                style={{width: '350px'}}/>
                    <h2 className='h3'>What is your correction factor?</h2>
                    <TextField  type='text'
                                placeholder='1u: 45 mg/dL'
                                name='correctionFactor'
                                value={this.state.correctionFactor}
                                onChange={this.changeHandler}
                                style={{width: '350px'}}/>
                    <h2 className='h3'>What is the carb ratio used for a food bolus?</h2>
                    <TextField  type='text'
                                placeholder='1u: 15 mg/dL'
                                name='carbRatio'
                                value={this.state.carbRatio}
                                onChange={this.changeHandler}
                                style={{width: '350px'}}/>
                    <h2 className='h3'>How precise is your insulin dosage?</h2>
                    <FormControl sx={{ m: 1, minWidth: 120 }}>
                        <InputLabel id="demo-simple-select-helper-label">Precision</InputLabel>
                        <Select
                            labelId="demo-simple-select-helper-label"
                            id="demo-simple-select-helper"
                            value={this.state.precision}
                            label="Precision"
                            onChange={this.changeHandler}
                            style={{width: '340px'}}
                        >
                        <MenuItem value="">
                        </MenuItem>
                        <MenuItem value={1}>1 unit</MenuItem>
                        <MenuItem value={0.5}>0.5 unit</MenuItem>
                        <MenuItem value={0.25}>0.25 unit</MenuItem>
                        </Select>
                    </FormControl>
                    <div className='space'> </div>
                    <Link to='/'><Button className='saveB' variant="contained" type='submit'>SAVE</Button></Link>
                    <div className='space'> </div>
                </form>
                
            </div>
        )
    }
}

export default Settings
