import React, { Component } from 'react';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import BotNav from './components/BotNav';
import ColorSliders from './components/ColorSliders';
import Paper from 'material-ui/Paper';
import ControlSliders from './components/ControlSliders';
import RaisedButton from 'material-ui/RaisedButton';

const divBoxStyle = {
  height: 200,
  width: '100%',
  textAlign: 'center',
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  justifyContent: 'center',
};

const buttonStyle = {
  marginTop:5,
  paddingTop:5,
  paddingBottom:90,
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
}

const muiTheme = getMuiTheme({
  
});

class App extends Component {
  state = {
    redColor: 0,
    greenColor: 0,
    blueColor: 0,
    bgColor: 'white',
    brightness: 100,
    toggleTime: true,
  };
  
  handleColorChange = (e, value, name) => {
    this.setState({[name]: value});
  };

  setDefaults = () => {
    this.setState({
      redColor:255, greenColor:0, blueColor:0,
      brightness:10,
      toggleTime:true,});
  };
  
  handleBrightnessChange = (e,val) => {
    this.setState({brightness:val});
  };
  
  handleToggle = (e,val) => {
    this.setState({toggleTime:val})
  };
  
  fetchCurrent = () => {
    this.setDefaults(); //TODO
  }
  
  sendSettingsJSON = () => {
    let data = {
      'red': this.state.redColor,
      'green': this.state.greenColor,
      'blue': this.state.blueColor,
      'brightness': this.state.brightness / 100,
      'waitTime': this.state.toggleTime ? '60' : '1'
    }
    console.log(data);
  }
  
  render() {
    return (
      <MuiThemeProvider muiTheme={muiTheme}>
        <div>
          <div style={divBoxStyle}>
            <Paper style={{
              height: 150,
              width: 200,
              textAlign: 'center',
              display: 'flex',
              flexDirection: 'row',
              alignItems: 'center',
              justifyContent: 'center',
              backgroundColor:"rgb("+this.state.redColor+","
                +this.state.greenColor+","+this.state.blueColor+")"
            }} zDepth={5} />
          </div>
          <ColorSliders 
            redColor={this.state.redColor} 
            greenColor={this.state.greenColor} 
            blueColor={this.state.blueColor}
            handleColorChange={this.handleColorChange}
          />
          <ControlSliders 
            brightness={this.state.brightness} 
            handleBrightnessChange={this.handleBrightnessChange} 
            toggleTime={this.state.toggleTime} 
            handleToggle={this.handleToggle}
          />
          <div style={buttonStyle}>
            <RaisedButton label="Set" primary={true} onClick={this.sendSettingsJSON} />
          </div>
          
          <BotNav 
            setDefaults={this.setDefaults}
            fetchCurrent={this.fetchCurrent}
          />
        </div>
      </MuiThemeProvider>
    );
  }
}

export default App;